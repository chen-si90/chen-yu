# 请补充你的代码
weight=int(input("请输入您的体重（公斤）："))
height=float(input("请输入您的身高（米）："))
bmi = weight / (height ** 2) 
print(f"您的BMI值为：{bmi:.2f}") 
if bmi<18.5:
    print("体重过轻")
elif bmi>=18.5 and bmi<24.9:
    print("体重正常")
elif bmi>=25 and bmi<29.9:
    print('体重超重')
else:
    print('肥胖')
