import yaml
def test_yaml():
    with open('../tmp.yaml','r',encoding='utf-8') as f:
        data=yaml.load(f)
    print('yaml data:', data)