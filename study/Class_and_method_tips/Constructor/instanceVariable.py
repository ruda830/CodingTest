class Blender:
    def __init__(self, ap, bn):
        #インスタンス変数
        self.apple = ap
        self.banana = bn


    def mix(self):
        print(self.apple + "ジュース")
        print(self.banana + "ジュース")

blender1 = Blender("りんご", "バナナ")
blender1.mix()
