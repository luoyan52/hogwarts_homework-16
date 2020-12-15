import pytest
from pythoncode.calculator import  Calculator
import yaml
def get_datas(algo):
    with open('./data.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        datas = datas[algo]["datas"]
        ids = datas[algo]["myid"]
        return [datas, ids]

class TestCalc:

     @pytest.mark.parametrize("a,b,expect",
                              get_datas("add")[0],
                              ids=get_datas("add")[1])
     def test_add(self,a,b,expect):

         assert  expect== self.calc.add(a,b)

     @pytest.mark.parametrize("a,b,expect",
                              get_datas("sub")[0],
                              ids=get_datas("sub")[1])
     def test_sub(self, a, b, expect):

        assert expect == self.calc.sub(a, b)

     @pytest.mark.parametrize("a,b,expect",
                              get_datas("mul")[0],
                              ids=get_datas("mul")[1])
     def test_mul(self, a, b, expect):
         assert expect == self.calc.mul(a, b)

     @pytest.mark.parametrize("a,b,expect",
                              get_datas("div")[0],
                              ids=get_datas("div")[1])
     def test_div(self, a, b, expect):
         assert expect == self.calc.div(a, b)