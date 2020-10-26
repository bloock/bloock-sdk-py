
def resolve():
    global checker
    checker = True

def reject(e):
    global checker
    checker = False

def mocked_apiservice_write(data):
    if data[0].getMessage() == '012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8':
        return ['012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8']
    elif data[0].getMessage() == '112c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8':
        return []
    else:
        raise BaseException("Any api exception")

def mocked_setinterval_init(b, writer):
    return