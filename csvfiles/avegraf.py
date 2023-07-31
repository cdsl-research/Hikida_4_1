import pandas as pd
import matplotlib.pyplot as plt

def create_multiseries_bar_chart(csv_file_path, pic):
    # CSVファイルを読み込みます
    df = pd.read_csv(csv_file_path)

    x_axis = df.iloc[:, 0]

    # DataFrameの残りの列をy軸として抽出します
    y_axes = df.iloc[:, 1:]
    #print(y_axes.iloc[:, 1:0])

    # 複数系列の棒グラフを作成します
    #y_axes.plot(kind='bar', stacked=True)
    # 複数系列の棒グラフを作成します

    #y_axes.plot(kind='bar', position=1, width=0.2, align='center', label="Series 1")
    #y_axes.plot(kind='bar', position=2, width=0.2, align='center', label="Series 2")
    #y_axes.plot(kind='bar', position=3, width=0.2, align='center', label="Series 3")

    plt.bar(x_axis -20, y_axes.iloc[:, 0], width=20, align='center', label="carts")
    plt.bar(x_axis , y_axes.iloc[:, 2], width=20, align='center', label="front-end")
    plt.bar(x_axis +20, y_axes.iloc[:, 3], width=20, align='center', label="orders")

    # グラフのタイトルと軸ラベルを設定します
    plt.xlabel("users", fontsize=22)
    plt.ylabel("memory usage(%)", fontsize=22)
    plt.ylim(0, 100)
    plt.tick_params(labelsize=20)
    plt.legend(fontsize=20)

    plt.xticks(x_axis, [100, 200, 300])

    fig = plt.gcf()
    fig.set_size_inches(8.7, 6)   

    # グラフを表示します
    plt.savefig(pic)

if __name__ == "__main__":
    # CSVファイルのパスを指定してください
    csv_file_path = "/home/hikida/promethe/csvfiles/memave.csv"

    pic = "/home/hikida/promethe/csvfiles/0731_mem_ave.png"

    # 複数系列の棒グラフを作成します
    create_multiseries_bar_chart(csv_file_path, pic)
