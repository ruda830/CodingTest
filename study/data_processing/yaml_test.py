import yaml

with open('hogehoge.yml') as file:
    obj = yaml.safe_load(file)
    print(obj['hogehoge_value'])