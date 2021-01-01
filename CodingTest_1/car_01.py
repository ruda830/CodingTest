'''
01. ミッションの内容を理解しよう(自分なりに仕様を整理しよう)
所要時間：約1~4H
a,いくつかの走行距離において、それぞれ料金がいくらになるか計算してみよう。
b,低速走行時間が含まれていた場合、料金がどうなるか考えてみよう。
c,深夜料金になる22時をまたいだ場合、料金がどうなるか考えてみよう

'''

'''
a.
円と距離を分離して考えた方がいい。
'''

class Taxi:

    def __init__(self):
        self.hatu_money = 0
        self.kasan_money = 0
        self.teisoku_money = 0


    def hatu(self, hatu_money):
        hatu_money = 410

    def kasan(self, kasan_money):
        kasan_money += 80

    def teisoku(self, teisoku_money):
        teisoku_money += 80


    def unchin(self, unchin):
        unchin = hatu_money + kasan_money + teisoku
        return goukei

    def taxi_step(self):
        print("タクシー乗ったよ")

taxi = Taxi()
while True:
    action = input("走った距離を教えてください：")
    if action >= 1052:
        return hatu()
    else:
        print("計算できません")


    taxi.unchin()
    taxi.taxi_step()






