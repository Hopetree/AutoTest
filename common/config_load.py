import os

from common.data_load import YamlLoad
from settings import BASE_DIR


class ConfigYaml(YamlLoad):
    def __init__(self, env):
        # 从环境变量中读取环境信息
        self.env = env
        self.config_path = os.path.join(BASE_DIR, 'config')
        self.config = self.get_config()

    def get_config(self):
        # global.yaml + env.yaml
        base_filename = os.path.join(self.config_path, 'global.yaml')
        base_config = self.load_data(base_filename)
        filename = os.path.join(self.config_path, f'{self.env}.yaml')
        env_config = self.load_data(filename)
        for each in env_config:
            base_config[each] = env_config[each]
        return base_config


if __name__ == '__main__':
    conf = ConfigYaml('dev').get_config()
    print(conf)
