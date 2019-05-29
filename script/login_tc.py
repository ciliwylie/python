from p2p_WY.po.login import Login_API
from p2p_WY.libs.tools import verifyClass

class test_login(verifyClass):
    def test_login(self):
        result = Login_API()
        self.verifyKey(result,'info','成功登录')

if __name__ == '__main__':
    print(test_login())