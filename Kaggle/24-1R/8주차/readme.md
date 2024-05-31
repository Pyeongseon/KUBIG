**8주차 주제: Anomaly Detection**
1. Imbalance Dataset (Sampling, Cost-sensitive, Overfitting,)
2. Sampling (Undersampling: RandomUnderSampler, Oversampling: SMOTE)
3. Sampling ‘during’ cross validation, not sampling ‘before’ cross validation

**Dataset**

[Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

**1. 이론 공부 (배지원)** 

**1) Credit Card Fraud Detection System**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/35de452e-6f88-4acb-b090-3faae819cdba/331de169-a5c9-4206-ae4b-46440c8c376a/Untitled.png)

- Real world: **고객의 신뢰를 망치지 않는 것이 중요, 사기는 탐지하되 고객의 편의성은 망치지 않는 것이 중요**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/35de452e-6f88-4acb-b090-3faae819cdba/0e565aea-ca18-41bd-9fae-312db77c861c/Untitled.png)

**2) Credit Card Fraud Scenario**

- **Card-present 오프라인**: physical card is needed, such as transactions at a store (also referred to as a point-of-sale - POS) or transactions at a cashpoint (for instance at an automated teller machine - ATM)
    - Lost or stolen card:
    - Counterfeited card (A fake card)
    - Card not received : intercepted by a fraudster, delivered to a different address, fraudster manages to order a new card without the knowledge of the legitimate customer (for example by accessing fraudulently their bank account)
    - 현재는 칩 내장 카드(EMV 기술) 덕분에 CP 시나리오 예방 -> CNP가 더 악용됨
- **Card-not-present (CNP) 온라인**: physical card does not need to be used, which encompasses payments performed on the Internet, by phone, or by mail.
    - 악용 data: the card number, card expiration date, card security code, and personal billing information (such as the cardholder’s address)
- **Fraud Scenario Generation**
    
    시나리오 1: **금액 기준**
    
    - 금액이 220을 초과하는 모든 거래는 사기 (실제 시나리오에서 영감을 얻은 것 X)
    - 그보다는 모든 기본 사기 탐지기가 탐지해야 하는 명백한 사기 패턴으로써, 사기 탐지 기술의 구현을 검증하는 데 유용
    
    시나리오 2: **terminal의 손상; a criminal use of a terminal, through phishing**
    
    - 매일 두 대의 단말기 목록이 무작위로 추첨되는데, 다음 28일 동안 이 단말기에서 발생하는 모든 거래는 사기 거래로 표시됨
    - 단말기의 사기 거래 횟수를 추적하는 기능을 추가하면 감지할 수 있음.
    - 단말기는 28일 동안만 손상되므로 이 시나리오를 효율적으로 처리하려면 개념 이동을 포함하는 추가 전략을 설계해야 함
    
    시나리오 3: **고객명의도용, card-not-present fraud**
    
    - 매일 3명의 고객 목록이 무작위로 추첨되고 이후 14일 동안 해당 고객의 거래 중 1/3에 5를 곱한 금액이 사기 거래로 표시됨
    - 고객은 계속해서 거래를 하고, 사기범은 자신의 이익을 극대화하기 위해 더 높은 금액의 거래를 하는 패턴.
    - 이 시나리오를 탐지하려면 고객의 지출 습관을 추적하는 기능을 추가해야 함
    - 시나리오 2의 경우 카드가 일시적으로만 손상되었으므로 concept drift을 포함하는 추가 전략도 설계해야 함.

---

**3) ML in Credit Card fraud Detection**

- **Class imbalance** : 실제 데이터 세트에서 사기 거래의 비율은 일반적으로 1% 미만 → imbalanced learning (sampling or loss weighting)
- **Concept drift** : 사기 수법이 시간에 따라 변화함. 시간에 따른 거래 및 사기 분포의 변화 / 신용카드 사용자의 지출 습관은 주중, 주말, 휴가 기간에 따라 다르며, 사기꾼들은 오래된 수법이 구식이 되면 새로운 수법을 채택 → online learning(temporal changes in statistical distributions), real world에서는 delayed feedbacks 때문에 더 부각되는 문제점
- **Near real-time requirements**: high-volume 데이터(millions of transactions per day)에 빠른 동작 필요 → classification times as low as tens of milliseconds → 병렬화 & scalability
- **Categorical features** : 범주형 변수가 많은 데이터셋 특징 (ID of a customer, a terminal, the card type 등) → feature aggregation, graph-based transformation, or deep-learning approaches such as feature embeddings.
- **Sequential modeling** : sequential stream data → 목표: '예상' '행위'를 characterize 하기, '언제' 비정상행위 일어나는지 탐지
    - modeling1: 기간으로 feature 합치기 (e.g. 평균/빈도)
    - modeling2: relying on sequential prediction models, LMTS같이 앞뒤의 맥락을 고려 (such as hidden Markov models: 은닉된 state를 추론, or recurrent neural networks for example).
        - 지출내역을 통해 과거의 행동을 유추하는 문제
        - 오늘 하려는 행동은 과거에 무엇을 했는지에 영향을 받으며, 과거에 했던 행동은 과거로 돌아가지 않는 한 다시는 관측할 수 없기 때문에 과거의 행동은 은닉된 state에 해당
        - Q={Study,Friend,Game}, 지출내역은 카드명세서를 통해 과거의 내역이더라도 직접적으로 관측할 수 있기 때문에 observation에 해당한다. Y={1,2,3,4} 값이 클 수록 돈을 많이 사용했다는 것을 의미한다.
        - 지출 내역이 1 1 4 2일 때, 이러한 지출 내역이 나타날 확률 계산
        - 지출 내역이 1 1 4 2일 때, 이러한 지출 내역이 나타날 확률이 가장 큰 과거의 행동 추론
        - 지출내역이 1, 3, 2, 1, 2인 경우, Viterbi algorithm을 이용하여 찾은 최적의 state는 study, friend, game, study, game이 된다. 따라서, 우리는 과거의 지출내역이 1, 3, 2, 1, 2인 경우, 가장 높은 확률로 과거 5일동안 공부, 친구 만나기, 게임, 공부, 게임을 했었다고 생각할 수 있다.
- **Class overlap:** raw information 만으로는 정상/비정상 탐지가 어려움 → feature engineering 으로 contextual information를 raw payment information에 추가해줘야 함
- **Performance measures** : 아직까지 합의 X, but 사기 거래의 탐지를 극대화하는 동시에 잘못 예측된 사기(오탐)의 수를 최소화할 수 있어야 합니다 minimizing the number of incorrectly predicted frauds (false positives)
- **Lack of public datasets** : 명백한 기밀 유지의 이유로 실제 신용카드 거래는 공개적으로 공유할 수 없음. 공개적으로 공유되는 데이터 세트는 2016년에 Kaggle에 하나 올라옴.

---

**4) Overfitting during Cross Validation**

- Cross validation 전에 undersample, oversample하면 안됨
- 이유: validation set에 "data leakage"
- 결과: precision, recall 이 좋은 것은 overfitting 때문이었음.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/35de452e-6f88-4acb-b090-3faae819cdba/89f052bd-6420-4542-a50c-d8a7d5c42e4d/Untitled.png)

- 5 batch로 split -> 4/5가 training, 1/5가 validation
- test set은 touch되면 안됨
- cross validation 도중에 synthetic data creation을 하는 것은 괜찮음. Before은 안됨
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/35de452e-6f88-4acb-b090-3faae819cdba/594f658d-4f9b-42b3-86b3-d6aec3ac2887/Untitled.png)
    
    - cross validation 전에 SMOTE를 하면 안됨.
        - oversample을 한 상태에서 validation set을 정해버리면 training set에 validation set과 동일한 데이터가 있을 수 있음 ⇒ overfitting이 됨.
        - 노란색으로 노란색을 예측하게 됨
    - cross validation 도중에 SMOTE를 해야 함.
        - cross validation을 해서 만들어진 해당 iteration의 validation, train set이 있고 그 때 train set에서 oversample을 하는 것임.
        - 주황색으로 노란색을 예측하게 됨
        - synthetic data는 training data에서만 만들어져야 하고, validation set에 영향을 주면 안됨.

---

- [0530 Anomaly detection (배지원)](https://www.notion.so/0530-Anomaly-Detection-a637a7c429d64c51b53c37986bae46d4?pvs=21)

**2. 코드 필사 (Credit Fraud || Dealing with Imbalanced Dataset)**

[Credit Fraud  || Dealing with Imbalanced Datasets](https://www.kaggle.com/code/janiobachmann/credit-fraud-dealing-with-imbalanced-datasets)

**3. 코드 리뷰 (강지윤)** 

[](https://github.com/MatildaBae/KUBIG_DataAnalysis_team2/tree/7dbb530b6ceb98dd0d3d3a5f7def997005984b5d/9주차)
