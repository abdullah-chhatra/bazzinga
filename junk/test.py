from RedisConnection import app

import redis
import os
import pickle
import unittest
import json

class CloudTestCase(unittest.TestCase):

  def setUp(self):
    msg = pickle.dumps({"sender" : "helllooooo", "receiver" : ["namu" ,"timpi" ,"sayali" ,"teju " ,"leena"], "name" : "friends"})
    app.redis.set('test1', msg)

  def tearDown(self):
    #app.redis.flushdb()
    pass

  def test_clouds(self):
    tester = app.test_client(self)

    response = tester.get('/test.json', content_type='application/json')

if __name__ == '__main__':
  unittest.main()
