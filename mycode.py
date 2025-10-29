import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Data:
    def __init__(self):
        self.test = ("./data/kdd99_test.csv")
        self.train = ("./data/kdd99_train.csv")
        
    def read_data(self, dir):
        data = pd.read_csv(dir)
        return data
    
    def make_feature(self, df):
        x = df.drop(columns = ["Attack Type"])
        return x
    
    def make_label(self, df):
        y = df["Attac Type"]
        return y
    
    def remove_duplicated(self, df):
        df = df.drop_duplicats()
        return df
    
    def remove_nan(self, df):
        df = df.dropna()
        return df
    
    def pca(self, df, k = 1):
        x = df - df.mean(axis = 0)
        cov_matrix = np.cov(x)
        eigen_val, eigen_vec = np.linalg.eig(cov_matrix)
        idx = np.argsort(eigen_val)[::-1]
        eigen_vec = eigen_vec[:, idx]
        p_c = eigen_vec[: , :k]
        x_pca = np.dot(x, p_c)
        return x_pca

    def pearson(self, x):
        drop_set = set() #나중에 제거해야할 feature 이름저장하는 빈 집합
        corr_matrix = x.corr().abs() #x의 모든 feature간의 피어슨 상관계수 계산후 절대값
        for i, col in enumerate(corr_matrix.columns): #index번호 i와 열이름 순서대로 추출
            if col not in drop_set:
                for j, col2 in enumerate(corr_matrix.columns):
                    if i < j: #mask, 대칭행렬이므로 상삼각행렬만 계산
                        corr_value = corr_matrix.iloc[i, j]
                        if corr_value >= 0.9:
                            #iloc으로 index번호로 접근, loc은 행 열 이름으로 접근
                            if x[col].var() >= x[col2].var():
                                
                                drop_set.add(col2)
                            else:
                                drop_set.add(col)
        
        print("remove feature: ", drop_set)
        print(len(drop_set))
        x = x.drop(columns= list(drop_set)) #set으로 저장한 결과를 list반환후 col 이름으로 제공
        return x
                        

class baysian:
    def __init__(self):
        pass
    
    #각 클래스의 확률
    def probability(self, y):
        count = 0
        for i in y:
            if i == 1:
                count += 1
        p_y_1 = count / len(y)
        p_y_0 = 1 - (count / len(y))
        return p_y_1 , p_y_0
    
    #연속형 베이지안은 가우시안 분포로 예측
    #정답이 1과 0 인 x 분포의 평균 표준편차를 각각 구함
    def condition_p(self, x, y):
        x = np.array(x, dtype=float)
        y = np.array(y, dtype=int)
        x_y1 = x[y == 1]
        x_y0 = x[y == 0]

        mean_y1 = np.mean(x_y1, axis=0)
        std_y1  = np.std(x_y1, axis=0)
        mean_y0 = np.mean(x_y0, axis=0)
        std_y0  = np.std(x_y0, axis=0)

        # 🔹 표준편차 0 보정
        std_y1 = np.where(std_y1 == 0, 1e-6, std_y1)
        std_y0 = np.where(std_y0 == 0, 1e-6, std_y0)

        return mean_y1, std_y1, mean_y0, std_y0
    
    def gaussian_prob(self, x, mean, std):
        x = np.array(x, dtype=float) #x를 numpy로 변환후 float으로 설정.
        exponent = np.exp(-((x - mean) ** 2) / (2 * std ** 2))
        prob = (1 / (np.sqrt(2 * np.pi) * std)) * exponent
        return np.where(np.isnan(prob), 1e-12, prob)  # 🔹 NaN 방지
    #np.where(condition, A, B) 조건 따라 값 선택후 배열 반환 true면 1e-12, 아니면 prob
    

    def predict(self, x_train, y_train, new_x):
        p_y1, p_y0 = self.probability(y_train)

        mean_y1, std_y1, mean_y0, std_y0 = self.condition_p(x_train, y_train)

        p_x_y1 = self.gaussian_prob(new_x, mean_y1, std_y1)
        p_x_y0 = self.gaussian_prob(new_x, mean_y0, std_y0)

        log_post_y1 = np.sum(np.log(p_x_y1 + 1e-12), axis=1) + np.log(p_y1)
        log_post_y0 = np.sum(np.log(p_x_y0 + 1e-12), axis=1) + np.log(p_y0)

        y_hat = (log_post_y1 > log_post_y0).astype(int)
        return y_hat

class eval:
    def __init__(self):
        pass

    def metrics_np(self, y_true, y_pred):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)

        TP = np.sum((y_true == 1) & (y_pred == 1))
        TN = np.sum((y_true == 0) & (y_pred == 0))
        FP = np.sum((y_true == 0) & (y_pred == 1))
        FN = np.sum((y_true == 1) & (y_pred == 0))

        eps = 1e-10

        accuracy = (TP + TN) / (TP + TN + FP + FN + eps)
        accuracy  = (TP + TN) / (TP + TN + FP + FN + eps)
        precision = TP / (TP + FP + eps)
        recall    = TP / (TP + FN + eps)
        f1_score  = 2 * precision * recall / (precision + recall + eps)

        return accuracy, precision, recall, f1_score

    
        
#이산형 분포는 세서 계산하지만 연속형 분포의경우에는 정규분포로 변환후 조건부확률 계산해야함.

    
    
        