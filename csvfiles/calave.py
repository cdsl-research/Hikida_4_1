import pandas as pd

def calculate_column_means(csv_file_path):
    # CSVファイル
    df = pd.read_csv(csv_file_path)

    # timeを削除
    df = df.drop(df.columns[0], axis=1)

    # 各列の平均値
    means = df.mean()

    return means

if __name__ == "__main__":
    # CSVファイルのパス
    csv_file_path = "/home/hikida/promethe/csvfiles/cpu_req0711_300_1.csv"

    # 平均値を計算
    column_means = calculate_column_means(csv_file_path)

    print(column_means)
