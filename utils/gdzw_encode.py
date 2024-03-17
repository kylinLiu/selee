import execjs


def doEncrypt(plaintext, publicKey):
    with open(r'njs/sm22.js') as f:
        docjs = execjs.compile(f.read())
        params = [plaintext, publicKey]
        result = docjs.call('get_str', *params)
        return result
