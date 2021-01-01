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
        self.hatu_money = 410
        self.kasan_money = 0
        self.teisoku_money = 0


    def hatu(self, hatu_money):
        hatu_money = 410

    def kasan(self, kasan_money):
        kasan_money += 80

    def teisoku(self, teisoku_money):
        teisoku_money += 80

#hatu_money, kasan_money, teisoku引数にいる？
    def unchin(self, unchin, hatu_money):
        unchin = hatu_money + kasan_money + teisoku
        return unchin

    def taxi_step(self):
        print("タクシー乗ったよ")

taxi = Taxi()
while True:
    action = int(input("走った距離を教えてください："))
    if action > 1052:
        #ここが上手くかけない
        taxi.hatu()
    else:
        print("計算できません")


    taxi.unchin(200)
    taxi.taxi_step()






