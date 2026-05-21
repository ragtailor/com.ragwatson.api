from pathlib import Path
import pandas as pd

_DATA_DIR = Path(__file__).resolve().parent.parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"


class WalterReader:
    def __init__(self):
        self.median_age = None
        self.median_fare = None

    def get_data(self) -> pd.DataFrame:
        """기존 뼈대 메서드 유지: 1번째 행 데이터 반환"""
        df = pd.read_csv(_CSV_PATH)
        return df.iloc[[0]].astype(object).where(df.iloc[[0]].notna(), None)

    def get_count(self) -> int:
        """기존 뼈대 메서드 유지: 전체 행 개수 반환"""
        df = pd.read_csv(_CSV_PATH)
        return int(df.shape[0])

    def get_dataframe(self) -> pd.DataFrame:
        """전체 데이터프레임 로드"""
        return pd.read_csv(_CSV_PATH)

    def get_features_and_labels(self):
        """학습에 필요한 6개 변수 전처리 및 분리 반환
        
        피처: Pclass, Sex, Age, SibSp, Parch, Fare
        라벨: Survived
        """
        df = self.get_dataframe()
        
        # 1. 누락된(결측치) 데이터 정제
        self.median_age = df["Age"].median()
        self.median_fare = df["Fare"].median()
        
        df["Age"] = df["Age"].fillna(self.median_age)
        df["Fare"] = df["Fare"].fillna(self.median_fare)
        
        # 2. 범주형 데이터 인코딩 (Sex: male -> 0, female -> 1)
        df["Sex"] = df["Sex"].map({"male": 0, "female": 1}).fillna(0).astype(int)
        
        # 3. 독립변수(X)와 종속변수(y) 추출
        features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
        X = df[features]
        y = df["Survived"]
        
        return X, y

    def preprocess_single_passenger(self, passenger_data: dict) -> pd.DataFrame:
        """단일 예측 요청 데이터를 모델 형식에 맞게 전처리"""
        # Pydantic 또는 dict 데이터를 DataFrame으로 변환
        df = pd.DataFrame([passenger_data])
        
        # 성별 변환 (라벨 인코딩)
        if isinstance(df["Sex"].iloc[0], str):
            df["Sex"] = df["Sex"].map({"male": 0, "female": 1}).fillna(0).astype(int)
            
        # 결측치가 들어오는 경우 학습 시 계산된 중간값으로 채움
        if self.median_age is None:
            raw_df = self.get_dataframe()
            self.median_age = raw_df["Age"].median()
            self.median_fare = raw_df["Fare"].median()
            
        df["Age"] = df["Age"].fillna(self.median_age)
        df["Fare"] = df["Fare"].fillna(self.median_fare)
        
        # 예측에 필요한 6개 피처 순서 맞추기
        features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
        return df[features]
