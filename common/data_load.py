import os

import yaml

from settings import BASE_DIR


class YamlLoad:
    @staticmethod
    def load_data(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = yaml.safe_load(f)
        return content


class DataTool:
    @staticmethod
    def list_to_parametrize(list_: list):
        """
        将字典组成的列表转化成@pytest.mark.parametrize格式的keys,values格式
        :param list_:
        :return: 元祖，第一个是key组成的字符串，第二个是列表组成的列表
        ('username, password, code', [['user01', 'pass01', 1], ['user02', 'pass02', 1]])
        """
        keys = list_[0].keys()
        values = []
        for item in list_:
            value = [item[k] for k in keys]
            values.append(value)
        return ', '.join(keys), values

    @staticmethod
    def get_data_by_key(dic: dict, key):
        return dic.get(key)


class YamlData(YamlLoad, DataTool):
    def __init__(self, filepath, base_dir=BASE_DIR):
        # 默认从项目根目录开始读取文件
        self.filepath = os.path.join(base_dir, filepath)

    @property
    def data(self):
        """
        读取yaml文件的内容并返回
        :return:
        """
        return self.load_data(self.filepath)

    @property
    def parametrize_data(self):
        return self.list_to_parametrize(self.data)

    def data_by_key(self, key):
        return self.get_data_by_key(self.data, key)


if __name__ == '__main__':
    yd = YamlData('data/user.yaml')
    print(yd.parametrize_data)
    yd = YamlData('data/demo.yaml')
    print(yd.data_by_key('name'))
