
#書き途中
##　tryのテスト
##　function.pyの条件分岐verを用いた。


def calc(func, num=1):

    #↓関数内で定義されている下のnumが一番優先に実行。
    num = 555
    cost = func(num)
    return cost

def apple_cost(num):
    #りんごの金額を買う個数で決定
    return 100*num

def orange_cost(num):
    return 50*num



#3個買う
num = 3
#apple = 0
orange = 0
#リンゴと言われたときにapple_costを返す。オレンジと言われたときにorange_costを返す。
select = input('リンゴかオレンジどちらが欲しいですか。')
if select == 'リンゴ':
    apple = 200  # この200は後に書いてあるcalc(apple_cost, num)に上書きされる。
    apple = calc(apple_cost, num)



elif select == 'オレンジ':
    orange = 200
    orange = calc(orange_cost, num)
else:
    result = print('入力が間違っています')
    pass #このままcalc関数を実行せずに下を実行



total_cost = apple + orange
msg = '購入金額は{}円です'.format(total_cost)
print(msg)
