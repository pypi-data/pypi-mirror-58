#文件的发送
from distutils.core import setup

setup( name='DuMath',# 对 外 我 们 模 块 的 名 字
version='1.0',# 版 本 号 description='这是第一个对外发布的模块，测试哦',
# 描 述
author='dushangjaing',# 作 者
author_email='3075374663@qq.com',
py_modules=['DuMath.demo1','DuMath.demo2']
# 要 发 布 的 模 块
)