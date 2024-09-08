# 请补充你的代码
a=float(input("请输入股票的买入价格（每股）："))
b=float(input("请输入股票的卖出价格（每股）："))
c=int(input("请输入持有的股票数量："))
d=(b-a)*c
print(f'总收益为：{d:.2f} 元')