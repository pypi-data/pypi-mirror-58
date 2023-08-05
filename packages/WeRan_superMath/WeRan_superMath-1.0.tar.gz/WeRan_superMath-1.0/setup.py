from distutils.core import setup

setup(
    name='WeRan_superMath',     # 模块对外名称
    version='1.0',   # 版本号
    descirption='这是第一个对外发布模块，仅限用于测试',
    author='WeRan',  # 作者
    author_email='we_ran@163.com',
    py_modules=['WeRan_superMath.demo1','WeRan_superMath.demo2']   #要发布的模块
)