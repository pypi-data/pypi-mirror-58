import setuptools

# 读取README.md文件的内容
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # 以下为必填参数
    name="xadmin-captcha", # 包名称
    version="1.0.1",# 版本号
    description="captcha for django xadmin",# 简单描述
    packages=setuptools.find_packages(),  # 需要打包的包列表,setuptools.find_packages()可以自动获取所有的包以及子包1
    # 以下为可选参数
    author="chenniantao",# 作者
    author_email="76876201@qq.com",# 作者邮箱
    long_description=long_description,# 详细描述
    long_description_content_type="text/markdown",# 详细描述的文本类型
    url="https://github.com/kauzhu",# 主页
    python_requires='>=3.6',# python版本限制
    license='MIT',#协议
    install_requires=['django-simple-captcha']
)