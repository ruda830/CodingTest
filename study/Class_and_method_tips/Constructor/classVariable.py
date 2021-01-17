
class TestClass_myself:
    """
    #クラス変数
    このクラスに依存する変数。
    """
    """
    例えば、
    i =TestClass_myself(), my =TestClass_myself, me=TestClass_myself
    の時、i,my,meインスタンス間でも共通して使える変数
    """
    val = []
    # xx = 50 <-ここで書いてもまったく意味がない。

    def __init__(self, xx): #クラス()と使う際に、代入する引数xx
        """
        #インスタンス変数
        生成したインスタンスでのみ使える変数。別のインスタンス間で共有できない。

        """
        self.val.append(1)
        self.val.append(2)
        self.val.append(3)
        self.val.append(xx)

        print("init:" + str(self.val))

    def test_method1(self, yy):
        print("test_method2:" + str(self.val) + yy)

#クラス()
testClass_myself = TestClass_myself(44) # > init:[1,2,3,44]



testClass_myself.test_method1("11") # > test_method2:[1,2,3,44]11