from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '19247244'
API_KEY = 'KsuVGDNz4zc1DIn1GQT9WgmD'
SECRET_KEY = 'uFjPneEYwtArlP22QX4Qap89QWAZqr0e'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def face_register(image, userId, imageType='BASE64', groupId='user'):
    """ 调用人脸注册 """
    res = client.addUser(image, imageType, groupId, userId)
    print(res)
    # errcode 不为0到时候，说明注册失败
    if res['errcode']:
        return False
    return True


def face_search(image, imageType='BASE64', groupIdList='user'):
    """ 调用人脸搜索 """
    client.search(image, imageType, groupIdList)
