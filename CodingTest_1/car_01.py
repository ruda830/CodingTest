'''
01. ミッションの内容を理解しよう(自分なりに仕様を整理しよう)
所要時間：約1~4H
a,いくつかの走行距離において、それぞれ料金がいくらになるか計算してみよう。
b,低速走行時間が含まれていた場合、料金がどうなるか考えてみよう。
c,深夜料金になる22時をまたいだ場合、料金がどうなるか考えてみよう

'''

'''
a.
'''

class Car:

    def __init__(self):
        self.first_money = 410
        self.accelerate_money = 80

    #def hatu(self, first_money):



    #def kasan(self, accelerate_money):


    def ryoukinn(self, first_money, accelerate_money):

        goukei = first_money + accelerate_money

        return goukei

car = Car()

print(car.ryoukinn(100, 10))







