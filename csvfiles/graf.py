import pandas as pd
import matplotlib.pyplot as plt

# 名前
# tit = "Pod cpu usage"いらない
xlab = "time(s)"
ylab = "CPU usage(%)"
pic = "/home/hikida/promethe/csvfiles/0509a.png"
csv = "/home/hikida/promethe/csvfiles/cpu_req0509a.csv"

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
plt.xlabel(xlab, fontsize=14)
plt.ylabel(ylab, fontsize=14)
plt.legend(fontsize=11, ncol=4, bbox_to_anchor=(0.5, 1.15), loc = 9, frameon=False)
plt.grid(axis = "y")
plt.tick_params(labelsize=13)

plt.xlim(0, (len(data)-1) * d)
plt.ylim(0)
# グラフを表示
fig = plt.gcf()
# fig.set_size_inches(6, 6)

# グラフを保存
plt.savefig(pic)

# plt.show()