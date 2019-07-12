import unittest
from unittest.mock import patch

import fakeredis

from CachedFunc.CacheRepos import MemRepo, RedisRepo


# Here we use MemRepo as the basic test case and cache repo.
class TestMemRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = MemRepo()

    def test_saveAndGet(self):
        l = [1, 2, 3]
        self.repo['key1'] = l
        self.assertEqual(self.repo['key1'], [1, 2, 3])
        self.assertFalse(self.repo['key1'] is l)
        ll = self.repo['key1']
        self.assertFalse(self.repo['key1'] is ll)

    def test_in(self):
        self.assertFalse('key2' in self.repo)
        self.repo['key2'] = 3
        self.assertTrue('key2' in self.repo)


class TestRedisRepo(TestMemRepo):
    def setUp(self) -> None:
        redis_patcher = patch('redis.Redis', fakeredis.FakeStrictRedis)
        self.redis = redis_patcher.start()
        self.addCleanup(redis_patcher.stop)
        self.repo = RedisRepo()

