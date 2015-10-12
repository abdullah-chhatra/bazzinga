__author__ = 'leena'

from redisQueue import RedisQueue


q = RedisQueue('test')
q.put('hello world')
