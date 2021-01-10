'''
if __name__ == '__main__'の使い方
ファイルを直接実行する場合はTrueになって実行される。
importで実行された場合はFalseになって実行されない。
'''


print(__name__)

def greeting(name):
    print('Hello', name)


#モジュール直接実行した時だけ、実行したいコードを下に。
#インタプリタでモジュールを読み込んだ場合実行しない。
if __name__ == '__main__':
    greeting('Taro')
    print(__name__)