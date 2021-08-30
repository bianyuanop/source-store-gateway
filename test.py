from urllib.parse import quote
import json
import util

msg = {
    'version': 'v1',
    'param': 'query',
    'arg': '0'
}

encoded_msg = util.encrypt(json.dumps(msg), "alongsecrectmightbesafe")
str_msg = encoded_msg.decode('ascii')
decoded_msg = str_msg.encode('ascii')

assert decoded_msg == encoded_msg

print(str_msg)
print(quote(str_msg))


decode_sig = util.decrypt(encoded_msg, "alongsecrectmightbesafe")
decode_str = decode_sig.decode('utf-8')
decode_json = json.loads(decode_str)
print(decode_json)

assert decode_json == msg
