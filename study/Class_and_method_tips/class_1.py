###classの勉強

##クラス定義
class TestClass:
    pass

#利用したい場合、関数の実行と同じように()付けてインスタンス生成
x = TestClass()



#-----------------------------------
#同じ名前で再定義すると上書きされるっぽい


#クラス内の関数はメゾットと呼ぶ
#第一引数にそのクラスのインスタンスを表すオブジェクト、selfを受け取る

class TestClass:
    x = "変数1"

    def test_method1(self):
        print(self.x)

    def test_method2(self, arg1):
        print("引数1:" + arg1)


testClass = TestClass()
testClass.test_method1()
# > 変数1

#testClass.test_method2()←これだとmissing required argumentと出る。
testClass.test_method2("引数Test")
# > 引数1:引数Test