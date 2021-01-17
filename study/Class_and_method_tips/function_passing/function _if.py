##　function.pyの条件分岐ver。場合によって受け取る関数を変える。


def calc(func, num=1):
    #funcという関数を入れる引数を用意。→apple_cost関数を代入

    cost = func(num)
    return cost

def apple_cost(num):
    #りんごの金額を買う個数で決定
    return 100*num

def orange_cost(num):
    return 50*num



#3個買う
num = 3
apple = 0
orange = 0
#リンゴと言われたときにapple_costを返す。オレンジと言われたときにorange_costを返す。
select = input('リンゴかオレンジどちらが欲しいですか。')
if select == 'リンゴ':

    apple += calc(apple_cost, num)


elif select == 'オレンジ':

    orange += calc(orange_cost, num)
else:
    result = print('入力が間違っています')



total_cost = apple + orange
msg = '購入金額は{}円です'.format(total_cost)
print(msg)
