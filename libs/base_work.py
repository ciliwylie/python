from p2p_WY.libs.tools import RequestHttp
class LoingBaseclass(RequestHttp):
    cookies={'PHPSESSID':''}
    def loginAPI(self,email='nidaye002',
        user_pwd='SlROanJvYWxyUEtrd3dlbkVIVGt2T2paTk9OeEhLaXZtRktNQlBld0FOYVRqZU9YUnQlMjV1NjVCOSUyNXU3RUY0c2YxMjM0NTYlMjV1OEY2RiUyNXU0RUY2',
        ajax='1'):
        api_url = '/index.php?ctl=user&act=dologin'
        login_data=dict(
            email=email,
            user_pwd=user_pwd,
            ajax=ajax
        )
        result = self.requestData(method='post', url=api_url, body=login_data)
        pid=result.cookies['PHPSESSID']
        self.cookies['PHPSESSID']=pid
        return result


if __name__ == '__main__':
    run = LoingBaseclass()
    print(run.loginAPI().json())
