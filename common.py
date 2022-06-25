def return_msg(code='200', msg='success', data=None):
    if data:
        return {
            'code': code,
            'msg': msg,
            'data': data
        }
    else:
        return {
            'code': code,
            'msg': msg,
        }
