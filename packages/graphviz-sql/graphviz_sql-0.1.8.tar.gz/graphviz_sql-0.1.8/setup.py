
#############################################
# File Name: setup.py
# Author: wangxup
# Mail: wang_xup@163.com
# Created Time:  2019-12-01
#############################################

from setuptools import setup, find_packages            


with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name = "graphviz_sql",      #这里是pip项目发布的名称
    version = "0.1.8",  
    keywords = ("None"),
    description = "将tree.export_graphviz构建决策树代码转换为标准sql",
    long_description = long_description,
	long_description_content_type="text/markdown", 
    # license = "MIT Licence",
    url = "https://github.com/WangxuP/graphviz_sql",     
    author = "wangxup",
    author_email = "wang_xup@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    # install_requires = ['random', 'pandas', 'numpy', 'sklearn']
)
