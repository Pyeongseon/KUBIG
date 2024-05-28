import tensorflow as tf
from keras import backend as K
import numpy as np
from classifications import calc_centers_for_support_tensor
from constants import CONFIG

class CenterLoss:
    def __init__(self):
        # Initialize the variables outside the function to ensure they are singleton
        self.center_loss_var = K.variable(0.0)
        self.softmax_euclidean_loss_var = K.variable(0.0)
        self.center_separate_loss_var = K.variable(0.0)

    def compute_loss(self, y_true, y_pred):
        SUPPORT_SIZE = int(CONFIG["test_sampling_method"][2:])

        indices = np.arange(CONFIG["batch_size"])
        train_indices = np.where(indices % (SUPPORT_SIZE + 1) == 0)[0]
        train_y_true = tf.gather(y_true, indices=train_indices)
        train_y_pred = tf.gather(y_pred, indices=train_indices)

        support_indices = np.arange(1, SUPPORT_SIZE + 1)
        support_y_true = tf.gather(y_true, indices=support_indices)
        support_y_pred = tf.gather(y_pred, indices=support_indices)

        centers = calc_centers_for_support_tensor(
            K.concatenate([train_y_true, support_y_true], axis=0),
            K.concatenate([train_y_pred, support_y_pred], axis=0),
        )

        loss = 0.0  # Initialize loss

        loss += 1.0 * self.__center_loss(
            support_y_true,
            support_y_pred,
            centers
        )
        loss += 0.5 * self.__softmax_euclidean_loss(
            K.concatenate([train_y_true, support_y_true], axis=0),
            K.concatenate([train_y_pred, support_y_pred], axis=0),
            centers
        )
        if CONFIG["experiment_id"].startswith("farther"):
            loss += 1.0 * self.__center_separate_loss(centers)

        return loss

    def __center_loss(self, y_true, y_pred, centers):
        y_true_value = K.argmax(y_true)

        K.set_value(self.center_loss_var, 0.0)
        loss = self.center_loss_var
        for label in range(CONFIG["num_classes"]):
            center = centers[label]
            indices = tf.where(tf.equal(y_true_value, label))
            pred_per_class = tf.gather_nd(y_pred, indices=indices)
            distances_per_class = self.__euclidean(pred_per_class, center)
            if CONFIG["experiment_id"].startswith("farther"):
                square_distances = K.pow(tf.subtract(distances_per_class, 0.5), 2)
                sum = K.sum(square_distances)
                loss = tf.add(loss, sum)
            else:
                square_distances = tf.pow(distances_per_class, 2)
                sum = K.sum(square_distances)
                loss = tf.add(loss, sum)

        return loss

    def __softmax_euclidean_loss(self, y_true, y_pred, centers):
        y_true_value = K.argmax(y_true)

        K.set_value(self.softmax_euclidean_loss_var, 0.0)
        base_loss = self.softmax_euclidean_loss_var
        for label in range(CONFIG["num_classes"]):
            center = centers[label]
            indices = tf.where(tf.equal(y_true_value, label))
            pred_per_class = tf.gather_nd(y_pred, indices=indices)
            distances_per_class = self.__euclidean(pred_per_class, center)
            sum = K.sum(distances_per_class, axis=-1)
            base_loss = tf.add(base_loss, sum)

        base_distances = K.zeros_like(y_true_value, dtype='float32')
        for label in range(CONFIG["num_classes"]):
            center = centers[label]
            distances_with_all_classes = self.__euclidean(y_pred, center)
            exp_distances = K.exp(-distances_with_all_classes)
            base_distances = tf.add(base_distances, exp_distances)

        log_distances = K.log(base_distances)
        sum_on_batch = K.sum(log_distances)

        return base_loss + sum_on_batch

    def __center_separate_loss(self, centers):
        distances = []
        for label_i in range(CONFIG["num_classes"]):
            for label_j in range(CONFIG["num_classes"]):
                if label_i < label_j:
                    center_i = centers[label_i]
                    center_j = centers[label_j]
                    distance = self.__euclidean(center_i, center_j)
                    distances.append(distance)

        K.set_value(self.center_separate_loss_var, 0.0)
        loss = self.center_separate_loss_var

        for distance in distances:
            distance = tf.pow(tf.subtract(distance, 2.0), 2)
            loss = tf.add(loss, distance)

        return loss

    @staticmethod
    def __euclidean(x, y):
        diff = tf.subtract(x, y)
        square_diff = K.pow(diff, 2)
        d = K.sqrt(K.sum(square_diff, axis=-1))
        return d

    @staticmethod
    def __cosine(x, y):
        x = K.l2_normalize(x, axis=-1)
        y = K.l2_normalize(y, axis=-1)
        c = K.mean(x * y, axis=-1)
        return -c

center_loss_instance = CenterLoss()

def center_loss(y_true, y_pred):
    return center_loss_instance.compute_loss(y_true, y_pred)
