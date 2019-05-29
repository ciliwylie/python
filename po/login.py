from p2p_WY.libs.tools import RequestHttp
import requests

def Login_API():
    run=RequestHttp()
    api_url = '/index.php?ctl=user&act=dologin'
    login_data = dict(
        email='nidaye002',
        user_pwd='SlROanJvYWxyUEtrd3dlbkVIVGt2T2paTk9OeEhLaXZtRktNQlBld0FOYVRqZU9YUnQlMjV1NjVCOSUyNXU3RUY0c2YxMjM0NTYlMjV1OEY2RiUyNXU0RUY2',
        ajax='1',
    )
    result = run.requestData(method='post',url=api_url,body=login_data)
    print(result.json())
    return result






