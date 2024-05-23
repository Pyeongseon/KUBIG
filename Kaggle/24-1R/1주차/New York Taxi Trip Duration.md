**1주차 주제: Clustering
Dataset:**  [nyc-taxi-trip-duration](https://www.kaggle.com/c/nyc-taxi-trip-duration)
**커널 필사**:  [Dynamics of New York city - Animation](https://www.kaggle.com/drgilermo/dynamics-of-new-york-city-animation)

1. **이론 발표 (강지윤) / 포스팅 (이동주) : Clustering 원리 및 기법 소개**
    
    **Clustering이란?**
    
    - 개체 간 서로 유사한 그룹을 찾거나 서로 다른 개체 그룹을 나누는 것
    - 각기 다른 클러스터 간의 거리는 Maximize, 한 클러스터 내의 요소간 거리는 minimize하는 것이 핵심
    - 클러스터링의 종류
        - 거리 기반: K-means, Hierarchical clustering
        - 밀도 기반: DBSCAN,
    
    **K-means Clustering**
    
    - 클러스터 개수인 k 값을 설정해준 후 랜덤으로 정해진 centroid를 기준으로 군집을 나누는 방식
    - Distance가 가장 가까운 클러스터에 매핑을 할 때 error(=distance)를 최소화하는 방식
    - Centroid 설정 → Eucledian Distance Matrix (기준: SSE or WCSS) → 거리를 최소화하도록 Centroid 재설정 반복
    - Optimal ‘K’를 찾는 방법: Elbow Method / Silhouette Score
    - K-means의 장단점
        - 장점: 다양한 데이터셋에 적용하고 실행하기 쉬움
        - 단점: Local optimum에 수렴할 가능성 존재, 거리 기반이므로 outlier에 취약, 학습에 영향을 끼치는 클러스터의 개수 K를 지정해줘야 함
    
    **Hierarchical Clustering**
    
    - 비슷한 군집끼리 묶어가며 최종적으로는 하나의 케이스가 될 때까지 군집을 묶는 방식
    - 두 클러스터 사이 거리를 측정해 거리가 가까운 클러스터끼리 묶는 방식
    - K-means와 달리 클러스터 개수를 지정하지 않아도 됨
        - single link
        - complete link
        - group average
        - n개의 군집으로 나누고 싶다면 Y축을 기준으로 manual하게 설정
    
    **DBSCAN**
    
    - 밀도 기반의 클러스터링으로, 점이 세밀하게 몰려 있어 밀도가 높은 부분을 클러스터링하는 방식
    - Points
        - Core point: 이 점을 중심으로 epsilon 반경내 minPts이상 수의 점이 있음
        - Border point: 군집에는 속하지만 core point는 아닌 점
        - Noise point: 어느 클러스터에도 속하지 않는 점
    - DBSCAN의 장점
        - K-means와 달리 클러스터 개수 지정하지 않아도 됨
        - 밀도에 따라 클러스터를 연결하므로 기하학적인 모양을 가진 군집도 잘 찾아낼 수 있음
        - Noise point를 통해 outlier 검출 가능
    
    **Spectral clustering**
    
    - Globular-shaped cluster를 보는 경향성이 있는 K-means 의 한계를 극복하고자 similarity graph를 사용하는 방식
