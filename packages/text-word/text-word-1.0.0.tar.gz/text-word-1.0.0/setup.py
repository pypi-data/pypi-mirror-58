import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="text-word",  # Replace with your own username
    version="1.0.0",  # 版本信息
    packages=setuptools.find_packages(),  # 程序包列表[项目中的py文件]
    install_requires=["jieba", "matplotlib"],  # 依赖包
    py_modules=["text"],  # 忽略的py文件
    python_requires=">=3",  # python版本
    url="https://github.com/Gemini128663/word_frequency_statistics.py",  #
    author="chang_an",  # 作者
    author_email="1286631591@qq.com",  # 作者邮箱
    description="中文文本词频统计",  # 描述
)
