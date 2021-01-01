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


    def hatu(self):
        #ここは今後の拡張を考えてメゾット化
        self.hatu_money = 410

    def kasan(self):
        self.kasan_money += 80

    def teisoku(self):
        self.teisoku_money += 80

    def unchin(self):
        return print(self.hatu_money + self.kasan_money + self.teisoku_money)

    def taxi_step(self):
        print("タクシー乗車中")


if __name__ == '__main__':

    taxi = Taxi()
    while True:
        action = int(input("走った距離を教えてください："))
        #走行距離と料金の計算。int(1052 + (走行距離-1052)/237)ずつ80円増
        if action <= 1052:
            #ここが上手くかけない
            taxi.hatu()
        else:

            print("計算できません")


        taxi.unchin()
        taxi.taxi_step()
        break


#ここからメモ--------------------------------------------------
"""
#本当はgoukeiの変数を使いたい。
#hatu_money, kasan_money, teisoku引数にいる？←いらないっぽい
    def unchin(self, goukei):
        goukei = self.hatu_money + self.kasan_money + self.teisoku
        return goukei                        
"""
"""
kasanの計算コードが2パターンある。と思う。
１．メゾットkasanに条件分岐　　変数にnかけるか。
class taxi:
    def __init__(self):
        self.n = int((走行距離-1052)/237)
    def kasan(self):
        if n<0:
            pass
        else:
            self.kasan_money += 80 * n

２．__main__下に、条件分岐　　メゾットをn回呼び出すか。
n = int((走行距離-1052)/237)
if n<0:
    hatu()
    unchin()
else:
    kasan()がn回呼び出し
    unchin()
"""


