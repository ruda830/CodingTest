##　関数を受け取る関数を作る

#↓参考にしたURL
#http://tarao-mendo.blogspot.com/2018/09/python-function-object.html

def calc(func, num=1):
    #funcという関数を入れる引数を用意。→apple_cost関数を代入

    cost = func(num)
    return cost

def apple_cost(num):
    #りんごの金額を買う個数で決定
    return 100*num

#================================
#拡張しやすい
def orange_cost(num):
    return 50*num


#================================

#3個買う
num = 3
total_cost = calc(apple_cost, num) + calc(orange_cost, num)
msg = '購入金額は{}円です'.format(total_cost)
print(msg)
