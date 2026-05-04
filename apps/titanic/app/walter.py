import pandas as pd

class Walter:
    def __init__(self):
        pass

    def get_data(self):
        df = pd.read_csv("Titanic-Dataset.csv")         
        print(df.head(10))


    


