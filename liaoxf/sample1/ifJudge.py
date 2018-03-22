height = float(input('请输入身高(m) :'))
weight = float(input('请输入体重(kg):'))
print('您的身高是 %.2f米 体重是 %.1f公斤' % (height, weight))
bmi = weight / (height * height)
if bmi > 32:
    bmides = '严重肥胖'
elif bmi >= 28:
    bmides = '肥胖'
elif bmi >= 25:
    bmides = '过重'
elif bmi >= 18.5:
    bmides = '正常'
else:
    bmides = '过轻'
print('bmi系数是 %.1f 您的体重检测结果为: %s' % (bmi, bmides))
