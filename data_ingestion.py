import pandas as pd
import os

folder = "Data/Raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        df = pd.read_csv(f"{folder}/{file}")

        print("\nFile:", file)
        print("\nShape:", df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:", df.duplicated().sum())