import pytest
from pythoncode.calculator import  Calculator

class TestCalc:
     def setup_class(self):
         self.calc = Calculator()
         print("开始计算")
     def  teardown_class(self):
          print("结束计算")
     @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(100,200,300)],ids=["int","minus","bigint"])
     def test_add(self,a,b,expect):

         assert  expect== self.calc.add(a,b)

     @pytest.mark.parametrize("a,b,expect", [(8, 5, 3), (-3, -2, -1), (300, 200, 100),(300, 0, 300)],
                                  ids=["int", "minus", "bigint","sub_zero"])
     def test_sub(self, a, b, expect):

        assert expect == self.calc.sub(a, b)

     @pytest.mark.parametrize("a,b,expect", [(2, 2, 4), (-3, 1, -3), (300, 200, 60000),(4,0,0)],
                              ids=["int", "minus", "bigint","mul_zero"])
     def test_mul(self, a, b, expect):
         assert expect == self.calc.mul(a, b)

     @pytest.mark.parametrize("a,b,expect", [(4, 2, 2), (-3, 1, -3), (60000, 200, 300),(800,1,800)],
                              ids=["int", "minus", "bigint","div_1"])
     def test_div(self, a, b, expect):
         assert expect == self.calc.div(a, b)