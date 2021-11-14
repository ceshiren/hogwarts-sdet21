"""
__author__ = 'hogwarts_xixi'
"""

# 一个功能点封装成一个fixture
import pytest


@pytest.fixture(scope="session", autouse=True)
def open_browser():
    print("打开浏览器")
    pass


@pytest.fixture()
def connect_db():
    print("连接数据库")
    pass


# hook 函数，预加载
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
