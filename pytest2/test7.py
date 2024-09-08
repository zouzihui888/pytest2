# 请补充你的代码
in_money = float(input('请输入股票的买入价格（每股）：'))
out_money = float(input('请输入股票的卖出价格（每股）：'))
make_money = int(input('请输入持有的股票数量：'))
income = float((out_money - in_money) * make_money)
print(f'总收益为：{income:.2f} 元')