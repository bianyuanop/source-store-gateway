from urllib.parse import quote
from base64 import encode
import json
import util

msg = {
    'version': 'v1',
    'param': 'query',
    'arg': '0'
}

encoded_msg = util.encrypt(json.dumps(msg), util.secret_key)
str_msg = encoded_msg.decode('ascii')
decoded_msg = str_msg.encode('ascii')

assert decoded_msg == encoded_msg

print(str_msg)
print(quote(str_msg))

