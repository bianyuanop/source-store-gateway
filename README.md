## see `test.py` 

generate sigature first then quote it to be able to use directly in browser address

for example

transfer this json

{
    "version": "v1",
    "param": "query",
    "arg": "1",
}

use `util.encrypt` TO 

E9z/9KBfSl%2BxGVeKap39qLSUjRu4LnXwqxGh1P0Bh4T1NJX90cg/O6ybEiN875fw0HGX6nSxk4u8CvTbiybpkg%3D%3D

then use urllib.parse.quote TO SAFE ONE

pOwi66f4R%2B/PfOqBVXh6ifHxGOq5WQ/vhn9APVpDsyP9%2BdKjXHhw41aRfaBnyFRX4jZekp23gXBIYIKf4shI2Q%3D%3D

then direct to `/gateway?sig=pOwi66f4R%2B/PfOqBVXh6ifHxGOq5WQ/vhn9APVpDsyP9%2BdKjXHhw41aRfaBnyFRX4jZekp23gXBIYIKf4shI2Q%3D%3D`

then you can be redirect