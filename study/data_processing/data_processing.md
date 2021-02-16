pythonで　yaml<=>JSON
https://pyteyon.hatenablog.com/entry/2020/05/15/084557


JSON
listでも、dictでも。かっこでくくられ、,で区切られたデータ構造

YAML
インテンドで区切られたデータ構造。基本dictで扱い、-を使うとlistに直せる


list
[]

dict(辞書)
{}
{key:value}


探索には
isinstance関数つかう(＊complexity_str.pyをみて)