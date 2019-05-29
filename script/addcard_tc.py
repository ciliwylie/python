from p2p_WY.po.addcard import MoneyManage
from p2p_WY.libs.tools import verifyClass
import unittest

class test_addcard(verifyClass):
    def setUp(self):
        self.add=MoneyManage()

    def test_addcard(self):
        result = self.add.add_Bankcard()
        self.verifyKey(result,'info','保存成功')

if __name__ == '__main__':
    unittest.main()

