**7주차 주제: NLP 
1. Preprocessing (Tokenization, Stopwords, Stemming/Lemmatization, Vectorization) -TF-IDF, CountVectorizer(Bag of Words)
2. Topic Modelling (LDA)**

**Dataset**

[Spooky Author Identification](https://www.kaggle.com/competitions/spooky-author-identification)

**1. 이론 공부 (이동주)** 

**1) Count 기반 단어 표현:** 

- **BagofWords(BoW):** 출현 빈도(frequency)에만 집중하는 텍스트 데이터 수치화 표현 방법
- **Document-Term Matrix(DTM):** 서로 다른 문서들의 BoW들을 결합→ 다수의 문서에서 등장하는 각 단어들의 빈도를 행렬
- **TF-IDF(Term Frequency-Inverse Document Frequency)**

**2) Topic Modelling**: 문서 집합에서 토픽을 찾아내는 프로세스

- **Latent Dirichlet Allocation(LDA)**
    - 각 문서의 토픽 분포와 각 토픽 내의 단어 분포를 추정하는 방법 (빈도수 기반의 BoW, DTM, TF-IDF 행렬이 input)
    - 기준 1: 문서 내 단어들이 어떤 토픽에 해당하는지 확인
        
        $P(topic(t)| document(d))$
        
    - 기준 2: 타 문서 내 단어 토픽 분포 비교
        
        
        $P(word(w)|topic(t))$
        
- **Non-negative matrix factorization (NNMF) :**
    - 모든 원소 값이 모두 양수일 때 하나의 행렬을 두개의 기반 양수 행렬로 분해하는 기법
    - 예시: V(4*6)이라는 행렬을 W(4*2) * H(2*6) 으로 분해

[240523 이론 (이동주)](https://www.notion.so/240523-5028e254c98943c6aff5a7fbe37ecf56?pvs=21)

**2. 코드 필사 (Teaching notebook for total imaging newbies)**

[Spooky NLP and Topic Modelling tutorial](https://www.kaggle.com/code/arthurtok/spooky-nlp-and-topic-modelling-tutorial)

**3. 코드 리뷰 (배지원)** 

[](https://github.com/MatildaBae/KUBIG_DataAnalysis_team2/tree/cd2f0fc6dc6fc72bbc45c6e170b3ea4603965f4d/8주차)
