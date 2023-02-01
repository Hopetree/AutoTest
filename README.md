# AutoTest 自动化测试

项目结构说明

```shell
├── README.md                               项目说明文件
├── api                                     API测试目录
│   ├── case                                API测试用例目录
│   └── module                              API测试接口封装类
├── app                                     移动端测试目录 
│   ├── case                                移动端测试用例目录
│   └── module                              移动端测试封装类
├── common                                  公共工具类存放目录
│   ├── config_load.py                      读取环境变量的工具
│   ├── data_load.py                        读取测试数据的工具
│   ├── logger.py                           日志工具
│   └── utils.py                            其他工具
├── config                                  环境变量文件目录
│   ├── global.yaml                         全局环境变量
│   ├── dev.yaml                            dev环境变量                     
│   └── sit.yaml                            sit环境变量
├── conftest.py                             pytest全局加载配置
├── data                                    测试数据存放目录
│   ├── demo.yaml                           自定义用例测试数据
│   └── user.yaml                           自定义用例测试数据
├── demo                                    测试用例demo目录，主要展示pytest结合allure的用法
│   ├── case                                演示用例
│   └── module                              演示封装类
├── log                                     日志存放目录
├── pytest.ini                              pytest配置
├── report                                  allure报告
│   └── environment.properties              allure环境变量文件
├── run.py                                  项目启动文件
├── settings.py                             项目配置
└── web                                     web自动化测试目录
    ├── case                                web自动化测试用例
    └── module                              web自动化测试页面定义类
```

log目录和report目录会自动生成，不需要提交到代码仓库

config目录存放不同环境的环境变量文件，global.yaml是全局环境变量，其他文件按需自定义，类似于postman的环境变量，项目执行时需要指定读取的环境变量文件

data目录存放测试数据，用例里面可以指定要读取的数据文件，格式按需设置

