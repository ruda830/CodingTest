# これはclassVariableのコメントを極力減らし、可読性を上げたものです。

class TestClass_myself:
    # このクラスに依存する変数。
    val = []

    def __init__(self, xx):  # クラス()と使う際に、代入する引数xx

        # 生成したインスタンスでのみ使える変数。
        self.val.append(1)
        self.val.append(2)
        self.val.append(3)
        self.val.append(xx)
        print("クラス(xx)時に生成される：" + str(self.val))

    def test_method1(self, yy):  # メゾット()と使う際に、代入する引数yy
        print("メゾットtest_method2(11)選択時に生成される:" + str(self.val) + yy)


testClass_myself = TestClass_myself(44)  # > init:[1,2,3,44]

#仮に
#testClass_myself = TestClass_myself() ->「xxが無い」とエラー

testClass_myself.test_method1("11")  # > test_method2:[1,2,3,44]11