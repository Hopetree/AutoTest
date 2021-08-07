"""
项目全局配置，配置针对的是项目，而不是测试
"""
import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 日志文件配置
LOG_CONFIG = {
    'console_output_level': 'INFO',
    'file_output_level': 'INFO',
    'log_path': os.path.join(BASE_DIR, 'log'),
    'log_file_name': 'autotest.log',
    'backup_count': 7,
}

if __name__ == '__main__':
    print(BASE_DIR)
