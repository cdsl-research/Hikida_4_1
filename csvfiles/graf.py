import pandas as pd
import matplotlib.pyplot as plt

# 名前
# tit = "Pod cpu usage"いらない
xlab = "time(s)"
ylab = "CPU usage(%)"
pic = "/home/hikida/promethe/csvfiles/0711_CPU_300_3.png"
csv = "/home/hikida/promethe/csvfiles/cpu_req0711_300_3.csv"

# CSVファイルからデータを読み込み
data = pd.read_csv(csv)

# x軸、y軸のデータを抽出
d = 5
x = data[data.columns.values[0]]
ylist = []
"""
for col in data.columns.values:
    if col == "carts" or col == "front-end":
        ylist.append(col) 
y_cols = ylist
"""
y_cols = data.columns.values[1:-1]
# グラフを描画
for y in y_cols:
    Y = data[y]
    plt.plot(x, Y, label=y)

# グラフにタイトルやラベルを設定
# plt.title(tit)
plt.xlabel(xlab, fontsize=20)
plt.ylabel(ylab, fontsize=20)
plt.legend(fontsize=16, ncol=4, bbox_to_anchor=(0.48, 1.15), loc = 9, frameon=False)
plt.grid(axis = "y")
plt.tick_params(labelsize=20)                                                           # 値の文字フォント

plt.xlim(1, (len(data)-1) * d)                                                          # xを1からにすることで原点0を１つにする
plt.ylim(0)
# グラフを表示
fig = plt.gcf()
fig.set_size_inches(8.7, 6)                                                             # 黄金比

# グラフを保存
plt.savefig(pic)

# plt.show()