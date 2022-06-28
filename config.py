from datetime import datetime
import socket

user_code = "USER0001202204221813207006642"
app_code = "app00859263495eb4d4d68a4d4f4bfb9511e61"
chaincode = "cc_1d720b6c79f848de8d36d2b08709b116"
nodeApi = "http://52.83.209.158:17502"
mspDir = './BsnTestnetCert(EMR)/fabricMsp'
httpcert = ''
app_public_cert_path = "./BsnTestnetCert(EMR)/gatewayCert/gateway_public_cert_secp256r1.pem"
user_private_cert_path = "./BsnTestnetCert(EMR)/userAppCert/secp256r1/private_key.pem"

user_data = {
        'lxl': '123',
    }

mock_data = [{
    'id': '0002',
    'name': '小红',
    'sex': '男',
    'age': '18',
    'info': '无不良疾病史',
    'caseList': [{
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hospital': '广中医',
        'result': '健康',
    }]
}]

env = 'pro'
if socket.gethostname() == 'LEOXLLI-NB1':
    env = 'dev'
