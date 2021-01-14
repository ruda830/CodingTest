"""
N＊Nのサイズのビンゴカードが、最終的にビンゴしているかどうかを判定する問題です。
入力
3
oox
xoo
oxo

出力
Yes
"""
#入力
N = int(input()) # 入力回数をNとして受け取る
list = [input() for i in range(N)] #print(list) ->['oxox', 'xxox', 'ooxo', 'oooo']
#斜め、横判定用のリスト
alllist = []
for j in range(N):
    alllist += list[j]


#Yes判定
try:
    for i in range(N): #もしtryの上にこれ書くと一つずつYesNo判定されてしまう。
        if list[i].count('o') == N: #横判定
            print('Yes')
            break

        elif alllist[i::N+1].count('o') == N: #斜め判定
            print('Yes')
            break

        elif alllist[i::N].count('o') == N: #縦判定
            print('Yes')
            break


#No判定
finally:
#横判定→斜め判定→縦判定。どれか当てはまったら'Yes'でbreak,当てはまらなかった順から下↓の判定。
#tryの条件と同じにしないと、’Yes'の時に’No’も発動してしまう。でも、かなり変な気がする。

    if list[i].count('o') != N: #必須。なんでiがこの位置にあるのに正確に動くのか分からない。
        #print('No_1')
        if alllist[i::N + 1].count('o') != N:
            #print('No_2')
            if alllist[i::N].count('o') != N:
                print('No_3')


#ここからメモ------------------------------
"""
    if list[i].count('x') >= 1:
        print('debag')
    でもいい。
"""
"""
    for k in range(N):
        if alllist[k::N+1].count('o') == N: #ifの位置ここでいいのかわからん。
            print('Yes')
            break
        else:
            print('debag')
"""
#a = [[str(c) for c in l.strip()] for l in sys.stdin]


"""
入力場合分け
4
oxox
xxox
ooxo
ooox

4
oxox
xoox
oxoo
ooxo

4
oxox
xxox
ooxo
oooo
4
oooo
oxox
xxox
ooxo

4
ooxo
oxox
xxox
oooo

4
oooo
oxox
xxox
oooo


"""