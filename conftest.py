import pytest
from  pythoncode.calculator import  Calculator

@pytest.fixture(scope="class")
def myfixture():
    print("开始计算")
    yield
    print("结束计算")
