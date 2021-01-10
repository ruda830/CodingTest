import json
def get_str(arg):
    res =[]
    if isinstance(arg, str):
        res.append(arg)
    elif isinstance(arg, list):
        for item in arg:
            res += get_str(item)
    elif isinstance(arg, dict):
        for value in arg.values():
            res += get_str(value)
    return res


if __name__ == "__main__":
    with open('complexity_str.json', encoding='utf-8') as f:
        arg = json.load(f)
        print(get_str(arg))

        #ここからいらない機能-----------------------------
        #ついでに、文字列の連結
        s = ''.join(get_str(arg))
        print(s)
