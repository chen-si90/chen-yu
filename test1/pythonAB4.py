#4
a=int(input('请输入每学分学费金额：'))
b=int(input('请输入你每个月生活费：'))
total_credits=17
total_tuition=total_credits*a
total_cost=b*5+total_tuition
studentl=total_cost*0.6
print(f'本学期你能够贷款{studentl:.2f}元')
