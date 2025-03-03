# REFERENCES PARAMETERS
CONFIG = {
    "epochs": 10,
    "batch_size": 32,
    "num_classes": 5,
    # "num_models": 1,
    "num_models": 2,
    "dataset": "kdd",
    "train_data": "train+",
    "test_data": "test+",
    "train_sampling_method": "zero",
    "test_sampling_method": "e_025",
    "output_dim": 121,
    # "num_process": 1,
    "num_process": 1,
    "model_type": "cnn",
    "experiment_count": 1,
    # "experiment_count": 10,
    "shuffle": False,
    "save_report": False,
    "input_shape": (121, ),
    "benchmark_dir": "/content/nsl_kdd_few_shot/benchmark",
    #"experiment_id": "playground",
    # "experiment_id": "base",
    "experiment_id": "farther",
    # "experiment_id": "farther_with_train",
    # "experiment_id": "closer",
}

"""
# REFERENCES PARAMETERS
CONFIG = {
    "epochs": 100,
    "batch_size": 50 * 26,
    "num_classes": 5,
    # "num_models": 1,
    "num_models": 12,
    "dataset": "kdd",
    "train_data": "train+",
    "test_data": "test+",
    "train_sampling_method": "zero",
    "test_sampling_method": "e_025",
    "output_dim": 121,
    # "num_process": 1,
    "num_process": 12,
    "model_type": "cnn",
    "experiment_count": 1,
    # "experiment_count": 10,
    "shuffle": False,
    "save_report": False,
    "input_shape": (121, ),
    "benchmark_dir": "/content/nsl_kdd_few_shot/benchmark",
    "experiment_id": "playground",
    # "experiment_id": "base",
    "experiment_id": "farther",
    # "experiment_id": "farther_with_train",
    # "experiment_id": "closer",
}
"""
LABEL_TO_NUM = {
    "normal": 0,
    "probe": 1,
    "dos": 2,
    "u2r": 3,
    "r2l": 4,
}

LABELS = list(LABEL_TO_NUM.keys())

# NSL-KDD dataset
# Names of the 41 features
FULL_FEATURES = [
    "duration",
    "protocol_type",
    "service",
    "flag",
    "src_bytes",
    "dst_bytes",
    "land",
    "wrong_fragment",
    "urgent",
    "hot",
    "num_failed_logins",
    "logged_in",
    "num_compromised",
    "root_shell",
    "su_attempted",
    "num_root",
    "num_file_creations",
    "num_shells",
    "num_access_files",
    "num_outbound_cmds",
    "is_host_login",
    "is_guest_login",
    "count",
    "srv_count",
    "serror_rate",
    "srv_serror_rate",
    "rerror_rate",
    "srv_rerror_rate",
    "same_srv_rate",
    "diff_srv_rate",
    "srv_diff_host_rate",
    "dst_host_count",
    "dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
    "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate",
    "label",
    "difficulty",
]

# Names of all the attacks names (including NSL KDD)
ENTRY_TYPE = {
    "normal": [
        "normal",
    ],
    "probe": [
        "ipsweep",
        "nmap",
        "portsweep",
        "satan",
        "saint",
        "mscan",
    ],
    "dos": [
        "back",
        "land",
        "neptune",
        "pod",
        "smurf",
        "teardrop",
        "apache2",
        "udpstorm",
        "processtable",
        "mailbomb",
    ],
    "u2r": [
        "buffer_overflow",
        "loadmodule",
        "perl",
        "rootkit",
        "xterm",
        "ps",
        "sqlattack",
        "httptunnel",  # こっち？
    ],
    "r2l": [
        "ftp_write",
        "guess_passwd",
        "imap",
        "multihop",
        "phf",
        "spy",
        "warezclient",
        "warezmaster",
        "snmpgetattack",
        "named",
        "xlock",
        "xsnoop",
        "sendmail",
        # "httptunnel",
        "worm",
        "snmpguess",
    ]
}

ENTRY_TYPE_REVERSE = {
    "normal": "normal",
    "ipsweep": "probe",
    "nmap": "probe",
    "portsweep": "probe",
    "satan": "probe",
    "saint": "probe",
    "mscan": "probe",
    "back": "dos",
    "land": "dos",
    "neptune": "dos",
    "pod": "dos",
    "smurf": "dos",
    "teardrop": "dos",
    "apache2": "dos",
    "udpstorm": "dos",
    "processtable": "dos",
    "mailbomb": "dos",
    "buffer_overflow": "u2r",
    "loadmodule": "u2r",
    "perl": "u2r",
    "rootkit": "u2r",
    "xterm": "u2r",
    "ps": "u2r",
    "sqlattack": "u2r",
    "httptunnel": "u2r",  # こっち？
    "ftp_write": "r2l",
    "guess_passwd": "r2l",
    "imap": "r2l",
    "multihop": "r2l",
    "phf": "r2l",
    "spy": "r2l",
    "warezclient": "r2l",
    "warezmaster": "r2l",
    "snmpgetattack": "r2l",
    "named": "r2l",
    "xlock": "r2l",
    "xsnoop": "r2l",
    "sendmail": "r2l",
    # "httptunnel": "r2l",
    "worm": "r2l",
    "snmpguess": "r2l",
}

TRAIN_SAMLE_NUM_PER_LABEL = {
    "a": [537, 28, 11, 23, 29, 0, 0, 7, 0, 329, 1, 21, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
    "b": [44, 44, 44, 44, 44, 0, 0, 44, 44, 44, 44, 44, 44, 0, 0, 0, 0, 43, 43, 43, 43, 0, 0, 0, 0, 43, 43, 43, 43, 43, 43, 43, 43, 0, 0, 0, 0, 0, 0, 0],
    "c": [200, 50, 50, 50, 50, 0, 0, 33, 33, 34, 33, 34, 33, 0, 0, 0, 0, 50, 50, 50, 50, 0, 0, 0, 0, 25, 25, 25, 25, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0],
    "d": [96, 71, 63, 69, 71, 0, 0, 59, 25, 92, 46, 68, 59, 0, 0, 0, 0, 29, 20, 12, 20, 0, 0, 0, 0, 19, 34, 21, 18, 14, 9, 59, 26, 0, 0, 0, 0, 0, 0, 0],
    "e": [200, 52, 46, 50, 52, 0, 0, 34, 14, 53, 26, 39, 34, 0, 0, 0, 0, 73, 48, 29, 50, 0, 0, 0, 0, 19, 34, 21, 18, 14, 9, 59, 26, 0, 0, 0, 0, 0, 0, 0],
    "f": [267, 58, 52, 56, 58, 0, 0, 43, 18, 67, 33, 50, 43, 0, 0, 0, 0, 34, 23, 13, 24, 0, 0, 0, 0, 15, 28, 17, 14, 11, 7, 48, 21, 0, 0, 0, 0, 0, 0, 0],
    "zero": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    # only normal
    # 10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

    # 1000
    # 94, 71, 63, 69, 71, 0, 0, 59, 25, 92, 46, 68, 59, 0, 0, 0, 0, 30, 20, 12, 21, 0, 0, 0, 0, 19, 34, 21, 18, 14, 9, 59, 26, 0, 0, 0, 0, 0, 0, 0,

    # 1000 per major label
    # 200, 52, 46, 50, 52, 0, 0, 34, 15, 52, 26, 39, 34, 0, 0, 0, 0, 73, 48, 29, 50, 0, 0, 0, 0, 19, 34, 21, 18, 14, 9, 59, 26, 0, 0, 0, 0, 0, 0, 0,

    # 1000 log per major and minor
    # 267, 58, 52, 56, 58, 0, 0, 43, 18, 67, 33, 50, 43, 0, 0, 0, 0, 34, 23, 13, 24, 0, 0, 0, 0, 15, 28, 17, 14, 11, 7, 48, 21, 0, 0, 0, 0, 0, 0, 0

    # 2000
    # 192, 141, 126, 138, 141, 0, 0, 118, 51, 183, 91, 136, 117, 0, 0, 0, 0, 59, 40, 24, 41, 0, 0, 0, 0, 38, 69, 43, 36, 28, 19, 117, 52, 0, 0, 0, 0, 0, 0, 0,

    # 2000 per major label
    # 400, 103, 92, 101, 104, 0, 0, 68, 29, 105, 53, 78, 67, 0, 0, 0, 0, 144, 97, 58, 101, 0, 0, 0, 0, 38, 68, 43, 36, 28, 19, 116, 52, 0, 0, 0, 0, 0, 0, 0,

    # 3000
    # 286, 212, 189, 206, 212, 0, 0, 177, 76, 275, 137, 204, 176, 0, 0, 0, 0, 89, 60, 36, 62, 0, 0, 0, 0, 57, 103, 64, 54, 42, 28, 176, 79, 0, 0, 0, 0, 0, 0, 0,

    # 3000 x e^1
    # 240, 188, 172, 184, 188, 0, 0, 164, 93, 232, 136, 182, 163, 0, 0, 0, 0, 102, 81, 61, 83, 0, 0, 0, 0, 79, 112, 84, 76, 67, 55, 163, 95, 0, 0, 0, 0, 0, 0, 0,

    # 3000 per major label
    # 600, 155, 138, 151, 156, 0, 0, 102, 44, 157, 79, 117, 101, 0, 0, 0, 0, 217, 145, 87, 151, 0, 0, 0, 0, 57, 103, 64, 54, 41, 28, 175, 78, 0, 0, 0, 0, 0, 0, 0,

    # 4000
    # 382, 282, 252, 275, 283, 0, 0, 237, 102, 366, 183, 272, 234, 0, 0, 0, 0, 118, 79, 48, 83, 0, 0, 0, 0, 76, 138, 86, 72, 55, 38, 234, 105, 0, 0, 0, 0, 0, 0, 0,

    # 4000 per major label
    # 800, 207, 185, 202, 208, 0, 0, 136, 58, 211, 105, 156, 134, 0, 0, 0, 0, 290, 193, 116, 201, 0, 0, 0, 0, 75, 137, 85, 71, 55, 38, 234, 105, 0, 0, 0, 0, 0, 0, 0,

    # 5000
    # 478, 353, 315, 344, 353, 0, 0, 296, 127, 458, 229, 340, 293, 0, 0, 0, 0, 148, 99, 60, 103, 0, 0, 0, 0, 95, 172, 107, 90, 69, 47, 293, 131, 0, 0, 0, 0, 0, 0, 0,

    # 5000 per major label
    # 1000, 258, 231, 252, 259, 0, 0, 170, 73, 263, 131, 195, 168, 0, 0, 0, 0, 360, 242, 146, 252, 0, 0, 0, 0, 94, 171, 107, 89, 69, 47, 292, 131, 0, 0, 0, 0, 0, 0, 0,
}

TEST_SAMLE_NUM_PER_LABEL = {
    "a": [47, 0, 0, 0, 3, 1, 4, 1, 0, 23, 0, 3, 0, 3, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 1],
    "b": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2],
    "c": [20, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1],
    "d": [7, 3, 3, 3, 5, 4, 5, 4, 1, 6, 2, 5, 1, 5, 0, 5, 4, 2, 0, 0, 2, 2, 2, 0, 3, 1, 5, 0, 2, 0, 0, 0, 5, 3, 2, 1, 1, 2, 0, 4],
    "e": [20, 3, 2, 3, 4, 4, 4, 2, 1, 4, 1, 3, 1, 3, 0, 3, 2, 3, 1, 1, 3, 3, 3, 1, 5, 0, 4, 0, 2, 0, 0, 0, 4, 3, 1, 1, 1, 1, 0, 3],
    "f": [27, 3, 3, 3, 4, 4, 4, 3, 1, 4, 2, 3, 1, 3, 0, 3, 3, 2, 0, 0, 2, 2, 2, 0, 4, 0, 4, 0, 1, 0, 0, 0, 3, 3, 1, 1, 0, 1, 0, 3],
    "zero": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    "e_025": [
        5,
        1, 0, 1, 1, 1, 1,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 0, 0, 1, 1, 1, 0, 1,
        0, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1
    ],
    "e_050": [10, 1, 1, 2, 2, 2, 2, 1, 0, 2, 1, 1, 0, 2, 0, 2, 1, 2, 0, 0, 1, 1, 2, 0, 4, 0, 2, 0, 1, 0, 0, 0, 2, 1, 1, 0, 0, 1, 0, 2],
    "e_075": [15, 2, 2, 2, 3, 3, 3, 2, 0, 3, 1, 2, 1, 2, 0, 2, 2, 2, 1, 1, 2, 2, 2, 1, 4, 0, 3, 0, 1, 0, 0, 0, 3, 2, 1, 1, 0, 1, 0, 3],
    "e_100": [20, 3, 2, 3, 4, 4, 4, 2, 1, 4, 1, 3, 1, 3, 0, 3, 2, 3, 1, 1, 3, 3, 3, 1, 5, 0, 4, 0, 2, 0, 0, 0, 4, 3, 1, 1, 1, 1, 0, 3],

    # const
    # 20, 4, 0, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 4, 4, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 4,

    # 25
    # 2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1,

    # 25 per major label
    # 5, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1,

    # 50
    # 3, 2, 2, 2, 2, 2, 2, 2, 1, 3, 1, 2, 1, 2, 0, 2, 2, 1, 0, 0, 1, 1, 1, 0, 2, 0, 2, 0, 1, 0, 0, 0, 2, 2, 1, 1, 1, 1, 0, 2,

    # 50 per major label
    # 10, 1, 1, 2, 2, 2, 2, 1, 0, 2, 1, 1, 1, 2, 0, 1, 1, 2, 1, 1, 1, 1, 1, 0, 3, 0, 2, 0, 1, 0, 0, 0, 2, 1, 1, 1, 0, 1, 0, 1,

    # 50 log per major and minor
    # 16, 2, 1, 2, 2, 2, 2, 1, 0, 2, 1, 2, 0, 2, 0, 2, 1, 1, 0, 0, 1, 1, 1, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1,

    # 75
    # 5, 2, 2, 2, 3, 3, 3, 3, 1, 4, 2, 3, 1, 3, 1, 3, 3, 2, 1, 1, 1, 1, 1, 1, 2, 1, 4, 0, 1, 1, 0, 0, 3, 3, 1, 1, 1, 1, 1, 3,

    # 75 per major label
    # 15, 2, 2, 2, 3, 3, 3, 2, 1, 2, 1, 2, 1, 2, 0, 2, 2, 2, 1, 1, 2, 2, 2, 1, 4, 0, 3, 0, 1, 0, 0, 0, 3, 2, 1, 1, 1, 1, 0, 2,

    # 100
    # 6, 3, 3, 3, 4, 4, 4, 4, 1, 6, 2, 4, 2, 4, 1, 4, 4, 2, 1, 1, 2, 2, 2, 1, 3, 1, 5, 0, 2, 1, 0, 0, 4, 3, 2, 1, 1, 2, 1, 4,

    # 100 x e^1
    # 4, 3, 3, 3, 3, 3, 4, 3, 2, 4, 3, 3, 2, 4, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 2, 4, 1, 2, 2, 0, 0, 4, 3, 2, 2, 2, 2, 2, 3,

    # 100 per major label
    # 20, 3, 3, 3, 4, 3, 4, 2, 1, 3, 2, 3, 1, 3, 0, 3, 2, 3, 1, 1, 3, 3, 3, 1, 5, 1, 4, 0, 1, 1, 0, 0, 3, 2, 1, 1, 1, 1, 1, 3,

    # 100 log per major and minor
    # 27, 3, 3, 3, 4, 4, 4, 3, 1, 4, 2, 3, 1, 3, 0, 3, 3, 2, 0, 0, 2, 2, 2, 0, 4, 0, 4, 0, 1, 0, 0, 0, 3, 3, 1, 1, 0, 1, 0, 3,

    # 200
    # 12, 6, 6, 7, 9, 8, 9, 8, 3, 11, 5, 9, 3, 9, 1, 9, 7, 4, 1, 1, 3, 3, 4, 1, 6, 2, 9, 1, 4, 1, 0, 0, 9, 7, 4, 3, 2, 4, 1, 8,

    # 300
    # 18, 10, 8, 10, 13, 11, 14, 12, 4, 17, 7, 13, 5, 13, 2, 13, 11, 6, 2, 2, 5, 5, 5, 2, 10, 3, 14, 1, 6, 2, 0, 0, 14, 10, 6, 5, 3, 5, 2, 11,

    # Full
    # normal 9711

    # ipsweep 141
    # nmap 73
    # portsweep 157
    # satan 735
    # saint 319
    # mscan 996

    # back 359
    # land 7
    # neptune 4657
    # pod 41
    # smurf 665
    # teardrop 12
    # apache2 737
    # udpstorm 2
    # processtable 685
    # mailbomb 293

    # buffer_overflow 20
    # loadmodule 2
    # perl 2
    # rootkit 13
    # xterm 13
    # ps 15
    # sqlattack 2
    # httptunnel 133

    # ftp_write 3
    # guess_passwd 1231
    # imap 1
    # multihop 18
    # phf 2
    # spy 0
    # warezclient 0
    # warezmaster 944
    # snmpgetattack 178
    # named 17
    # xlock 9
    # xsnoop 4
    # sendmail 14
    # worm 2
    # snmpguess 331
}

# for k in TRAIN_SAMLE_NUM_PER_LABEL:
#   TRAIN_SAMLE_NUM_PER_LABEL[k] = list(map(lambda x: int(x * 0.1), TRAIN_SAMLE_NUM_PER_LABEL[k]))

SAMPLE_NUM_PER_LABEL = {
    # normal
    "normal": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][0], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][0]},
    # probe
    "ipsweep": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][1], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][1]},
    "nmap": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][2], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][2]},
    "portsweep": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][3], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][3]},
    "satan": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][4], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][4]},
    "saint": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][5], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][5]},
    "mscan": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][6], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][6]},
    # dos
    "back": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][7], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][7]},
    "land": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][8], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][8]},
    "neptune": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][9], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][9]},
    "pod": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][10], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][10]},
    "smurf": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][11], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][11]},
    "teardrop": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][12], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][12]},
    "apache2": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][13], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][13]},
    "udpstorm": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][14], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][14]},
    "processtable": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][15], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][15]},
    "mailbomb": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][16], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][16]},
    # u2r
    "buffer_overflow": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][17], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][17]},
    "loadmodule": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][18], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][18]},
    "perl": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][19], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][19]},
    "rootkit": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][20], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][20]},
    "xterm": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][21], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][21]},
    "ps": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][22], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][22]},
    "sqlattack": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][23], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][23]},
    "httptunnel": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][24], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][24]},
    # r2l
    "ftp_write": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][25], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][25]},
    "guess_passwd": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][26], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][26]},
    "imap": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][27], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][27]},
    "multihop": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][28], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][28]},
    "phf": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][29], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][29]},
    "spy": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][30], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][30]},
    "warezclient": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][31], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][31]},
    "warezmaster": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][32], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][32]},
    "snmpgetattack": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][33], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][33]},
    "named": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][34], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][34]},
    "xlock": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][35], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][35]},
    "xsnoop": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][36], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][36]},
    "sendmail": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][37], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][37]},
    "worm": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][38], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][38]},
    "snmpguess": {"train": TRAIN_SAMLE_NUM_PER_LABEL[CONFIG["train_sampling_method"]][39], "test": TEST_SAMLE_NUM_PER_LABEL[CONFIG["test_sampling_method"]][39]},
}

# ***** KDD STRING FEATURES VALUES *****
SERVICE_VALUES = [
    "http",
    "smtp",
    "finger",
    "domain_u",
    "auth",
    "telnet",
    "ftp",
    "eco_i",
    "ntp_u",
    "ecr_i",
    "other",
    "private",
    "pop_3",
    "ftp_data",
    "rje",
    "time",
    "mtp",
    "link",
    "remote_job",
    "gopher",
    "ssh",
    "name",
    "whois",
    "domain",
    "login",
    "imap4",
    "daytime",
    "ctf",
    "nntp",
    "shell",
    "IRC",
    "nnsp",
    "http_443",
    "exec",
    "printer",
    "efs",
    "courier",
    "uucp",
    "klogin",
    "kshell",
    "echo",
    "discard",
    "systat",
    "supdup",
    "iso_tsap",
    "hostnames",
    "csnet_ns",
    "pop_2",
    "sunrpc",
    "uucp_path",
    "netbios_ns",
    "netbios_ssn",
    "netbios_dgm",
    "sql_net",
    "vmnet",
    "bgp",
    "Z39_50",
    "ldap",
    "netstat",
    "urh_i",
    "X11",
    "urp_i",
    "pm_dump",
    "tftp_u",
    "tim_i",
    "red_i",
    # "icmp",
    "http_2784",
    "harvest",
    "aol",
    "http_8001",
]

FLAG_VALUES = [
    "OTH",
    "RSTOS0",
    "SF",
    "SH",
    "RSTO",
    "S2",
    "S1",
    "REJ",
    "S3",
    "RSTR",
    "S0",
]

PROTOCOL_TYPE_VALUES = [
    "tcp",
    "udp",
    "icmp",
]

_COLUMNS = [
    "label",
    "src_bytes", "dst_bytes", "duration", "logged_in", "dst_host_count", "dst_host_srv_count", "serror_rate", "tcp", "udp", "SH", "REJ",
    "land", "wrong_fragment", "num_failed_logins", "num_compromised", "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "srv_serror_rate", "same_srv_rate", "OTH", "RSTO", "S3",
    "urgent", "hot", "root_shell", "su_attempted", "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "rerror_rate", "diff_srv_rate", "RSTOS0", "S2", "RSTR",
    "count", "srv_count", "num_root", "num_file_creations", "dst_host_serror_rate", "dst_host_srv_serror_rate", "srv_rerror_rate", "srv_diff_host_rate", "SF", "S1", "S0",
    "is_host_login", "is_guest_login", "num_shells", "num_access_files", "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "http", "smtp", "finger", "domain_u", "auth",
    "telnet", "ftp", "eco_i", "ntp_u", "ecr_i", "other", "private", "pop_3", "ftp_data", "rje", "time",
    "mtp", "link", "remote_job", "gopher", "ssh", "name", "whois", "domain", "login", "imap4", "daytime",
    "ctf", "nntp", "shell", "IRC", "nnsp", "http_443", "exec", "printer", "efs", "courier", "uucp",
    "klogin", "kshell", "echo", "discard", "systat", "supdup", "iso_tsap", "hostnames", "csnet_ns", "pop_2", "sunrpc",
    "uucp_path", "netbios_ns", "netbios_ssn", "netbios_dgm", "sql_net", "vmnet", "bgp", "Z39_50", "ldap", "netstat", "urh_i",
    "X11", "urp_i", "pm_dump", "tftp_u", "tim_i", "red_i", "icmp", "http_2784", "harvest", "aol", "http_8001",
]

COLUMNS = [
    "label",  # -1
    "duration",  # 0
    "tcp",  # 1 PROTOCOL
    "udp",  # 2 PROTOCOL
    "icmp",  # 3 PROTOCOL
    "http",  # 4 SERVICE
    "smtp",  # 5 SERVICE
    "finger",  # 6 SERVICE
    "domain_u",  # 7 SERVICE
    "auth",  # 8 SERVICE
    "telnet",  # 9 SERVICE
    "ftp",  # 10 SERVICE
    "eco_i",  # 11 SERVICE
    "ntp_u",  # 12 SERVICE
    "ecr_i",  # 13 SERVICE
    "other",  # 14 SERVICE
    "private",  # 15 SERVICE
    "pop_3",  # 16 SERVICE
    "ftp_data",  # 17 SERVICE
    "rje",  # 18 SERVICE
    "time",  # 19 SERVICE
    "mtp",  # 20 SERVICE
    "link",  # 21 SERVICE
    "remote_job",  # 22 SERVICE
    "gopher",  # 23 SERVICE
    "ssh",  # 24 SERVICE
    "name",  # 25 SERVICE
    "whois",  # 26 SERVICE
    "domain",  # 27 SERVICE
    "login",  # 28 SERVICE
    "imap4",  # 29 SERVICE
    "daytime",  # 30 SERVICE
    "ctf",  # 31 SERVICE
    "nntp",  # 32 SERVICE
    "shell",  # 33 SERVICE
    "IRC",  # 34 SERVICE
    "nnsp",  # 35 SERVICE
    "http_443",  # 36 SERVICE
    "exec",  # 37 SERVICE
    "printer",  # 38 SERVICE
    "efs",  # 39 SERVICE
    "courier",  # 40 SERVICE
    "uucp",  # 41 SERVICE
    "klogin",  # 42 SERVICE
    "kshell",  # 43 SERVICE
    "echo",  # 44 SERVICE
    "discard",  # 45 SERVICE
    "systat",  # 46 SERVICE
    "supdup",  # 47 SERVICE
    "iso_tsap",  # 48 SERVICE
    "hostnames",  # 49 SERVICE
    "csnet_ns",  # 50 SERVICE
    "pop_2",  # 51 SERVICE
    "sunrpc",  # 52 SERVICE
    "uucp_path",  # 53 SERVICE
    "netbios_ns",  # 54 SERVICE
    "netbios_ssn",  # 55 SERVICE
    "netbios_dgm",  # 56 SERVICE
    "sql_net",  # 57 SERVICE
    "vmnet",  # 58 SERVICE
    "bgp",  # 59 SERVICE
    "Z39_50",  # 60 SERVICE
    "ldap",  # 61 SERVICE
    "netstat",  # 62 SERVICE
    "urh_i",  # 63 SERVICE
    "X11",  # 64 SERVICE
    "urp_i",  # 65 SERVICE
    "pm_dump",  # 66 SERVICE
    "tftp_u",  # 67 SERVICE
    "tim_i",  # 68 SERVICE
    "red_i",  # 69 SERVICE
    "http_2784",  # 70 SERVICE
    "harvest",  # 71 SERVICE
    "aol",  # 72 SERVICE
    "http_8001",  # 73 SERVICE
    "OTH",  # 74 FLAG
    "RSTOS0",  # 75 FLAG
    "SF",  # 76 FLAG
    "SH",  # 77 FLAG
    "RSTO",  # 78 FLAG
    "S2",  # 79 FLAG
    "S1",  # 80 FLAG
    "REJ",  # 81 FLAG
    "S3",  # 82 FLAG
    "RSTR",  # 83 FLAG
    "S0",  # 84 FLAG
    "src_bytes",  # 85
    "dst_bytes",  # 86
    "land",  # 87
    "wrong_fragment",  # 88
    "urgent",  # 89
    "hot",  # 90
    "num_failed_logins",  # 91
    "logged_in",  # 92
    "num_compromised",  # 93
    "root_shell",  # 94
    "su_attempted",  # 95
    "num_root",  # 96
    "num_file_creations",  # 97
    "num_shells",  # 98
    "num_access_files",  # 99
    "is_host_login",  # 100
    "is_guest_login",  # 101
    "count",  # 102
    "srv_count",  # 103
    "serror_rate",  # 104
    "srv_serror_rate",  # 105
    "rerror_rate",  # 106
    "srv_rerror_rate",  # 107
    "same_srv_rate",  # 108
    "diff_srv_rate",  # 109
    "srv_diff_host_rate",  # 110
    "dst_host_count",  # 111
    "dst_host_srv_count",  # 112
    "dst_host_same_srv_rate",  # 113
    "dst_host_diff_srv_rate",  # 114
    "dst_host_same_src_port_rate",  # 115
    "dst_host_srv_diff_host_rate",  # 116
    "dst_host_serror_rate",  # 117
    "dst_host_srv_serror_rate",  # 118
    "dst_host_rerror_rate",  # 119
    "dst_host_srv_rerror_rate",  # 120
    "difficulty",  # 121
]

[
    # (1)
    "duration",
    # (2)
    "src_bytes",
    "dst_bytes",
    # (4)
    "land",
    "wrong_fragment",
    "urgent",
    "hot",
    # (5)
    "num_failed_logins",
    "logged_in",
    "num_compromised",
    "root_shell",
    "su_attempted",
    # (4)
    "num_root",
    "num_file_creations",
    "num_shells",
    "num_access_files",
    # (2)
    "is_host_login",
    "is_guest_login",
    # (2)
    "count",
    "srv_count",
    # (7)
    "serror_rate",
    "srv_serror_rate",
    "rerror_rate",
    "srv_rerror_rate",
    "same_srv_rate",
    "diff_srv_rate",
    "srv_diff_host_rate",
    # (10)
    "dst_host_count",
    "dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
    "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate",
    # SERVICE (71)
    "http",
    "smtp",
    "finger",
    "domain_u",
    "auth",
    "telnet",
    "ftp",
    "eco_i",
    "ntp_u",
    "ecr_i",
    "other",
    "private",
    "pop_3",
    "ftp_data",
    "rje",
    "time",
    "mtp",
    "link",
    "remote_job",
    "gopher",
    "ssh",
    "name",
    "whois",
    "domain",
    "login",
    "imap4",
    "daytime",
    "ctf",
    "nntp",
    "shell",
    "IRC",
    "nnsp",
    "http_443",
    "exec",
    "printer",
    "efs",
    "courier",
    "uucp",
    "klogin",
    "kshell",
    "echo",
    "discard",
    "systat",
    "supdup",
    "iso_tsap",
    "hostnames",
    "csnet_ns",
    "pop_2",
    "sunrpc",
    "uucp_path",
    "netbios_ns",
    "netbios_ssn",
    "netbios_dgm",
    "sql_net",
    "vmnet",
    "bgp",
    "Z39_50",
    "ldap",
    "netstat",
    "urh_i",
    "X11",
    "urp_i",
    "pm_dump",
    "tftp_u",
    "tim_i",
    "red_i",
    "icmp",
    "http_2784",
    "harvest",
    "aol",
    "http_8001",
    # PROTOCOL (2)
    "tcp",
    "udp",
    # FLAG (11)
    "OTH",
    "RSTOS0",
    "SF",
    "SH",
    "RSTO",
    "S2",
    "S1",
    "REJ",
    "S3",
    "RSTR",
    "S0",
]
