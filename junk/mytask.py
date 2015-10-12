__author__ = 'leena'

from example import add

res = add.delay(2, 2)
print(res.get())
