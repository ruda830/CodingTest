###classの勉強

##クラス定義
class TestClass:
    pass

#利用したい場合、関数の実行と同じように()付けてインスタンス生成
x = TestClass()

#------------------
#同じ名前で再定義すると上書きされるっぽい
#------------------

class TestClass:
    x = "変数1"

    #クラス内の関数はメゾットと呼ぶ
    #第一引数にそのクラスのインスタンスを表すオブジェクト、selfを受け取る
    def test_method1(self):
        print(self.x)

    def test_method2(self, arg1):
        print("引数1:" + arg1)


testClass = TestClass()
testClass.test_method1()
#testClass.test_method2()←これだとmissing required argumentと出る。
testClass.test_method2("引数Test")

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

testClass2 = TestClass2()
testClass2.test_method1()

# > init:[]
# > test_method2:[1,2,3]



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