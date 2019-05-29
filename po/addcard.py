from p2p_WY.libs.base_work import LoingBaseclass
class MoneyManage(LoingBaseclass):
    def add_Bankcard(self):
        self.loginAPI()
        url = '/member.php?ctl=uc_money&act=savebank'
        add_data = dict(
            real_name='你大爷',
            bank_id='1',
            otherbank='',
            region_lv1='1',
            region_lv2='2',
            region_lv3='52',
            region_lv4='501',
            bankzone='%E5%B7%A5%E5%95%86%E9%93%B6%E8%A1%8C%E9%95%BF%E5%AE%89%E7%81%B5%E5%A2%83%E6%94%AF%E8%A1%8C',
            bankcard='20222222222222222222',
            reBankcard='202222222222222222222'
        )
        method='post'
        result = self.requestData(method=method,url=url,body=add_data,cookies=self.cookies)
        return result

if __name__ == '__main__':
    run = MoneyManage()
    run.add_Bankcard()