##コンストラクタ
#対象のクラスのインスタンスを初期化する

class TestClass2:
    val = []

    def __init__(self):
        print("init:" + str(self.val))
        # > init:[]

        self.val.append(1)
        self.val.append(2)
        self.val.append(3)

        print("init:" + str(self.val))
        # > init:[1, 2, 3]

    def test_method1(self):
        print("test_method2:" + str(self.val))
        # > test_method2:[1,2,3]

#インスタンスを生成しないと使えない
testClass2 = TestClass2()
testClass2.test_method1()




class TestClass3:
    val = []

    def __init__(self, val1, val2):
        #初期化

        #リスト名.append(追加要素)　構文
        self.val.append(val1)
        self.val.append(val2)
        print("init:" + str(self.val))

testClass3 = TestClass3(1,2)
# > init:[1, 2]



#アウトプット用------------------------------------------------------
class TestClass_myself:
    val = []

    def __init__(self, xx):

        self.val.append(1)
        self.val.append(2)
        self.val.append(3)
        self.val.append(xx)

        print("init:" + str(self.val))

    def test_method1(self, yy):
        print("test_method2:" + str(self.val) + yy)


testClass_myself = TestClass_myself(44)
# > init:[1,2,3,44]
testClass_myself.test_method1("11")
# > test_method2:[1,2,3,44]11