from distutils.core import setup

setup(
    name='abc123',   #对外我们模块的名字
    version='1.0' ,  #版本号
    description='这是第一个对外发布的模块', #描述
    author='Galen',  #作者
    author_email='676216474@qq.com',
    py_modules=['abc123.demo1','abc123.demo2']       #要发布的模块
)