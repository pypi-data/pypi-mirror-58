#!/usr/bin/env python3
#
# This Class implements a method to enable item-level expiration for redis.
# The standard mechanism involves using a redis sorted set, that allow for
# scores to be attached to items.  By setting the score value to a Unix
# Timestamp in the future, we can use ZSET functions to obtain items to be
# removed i.e that have expired.
#
# This means another process must take care of recurrent maintenance.
#
# The class might implement key-ization of added items for additional
# data storage needs, but today is easier to separate the functionality.
#
# Author: Arturo 'Buanzo' Busleiman <buanzo@buanzo.com.ar>
#
# References:
# * https://stackoverflow.com/questions/17060672/ttl-for-a-set-member
# * https://quickleft.com/blog/how-to-create-and-expire-list-items-in-redis/

import datetime
import redis


class DeadSet():
    def __init__(self, keyname=None, default_expire=None, rdb=None):
        if type(default_expire) is datetime.timedelta:
            self.default_expire = default_expire
        else:
            raise ValueError
        if rdb is None:
            self.redis = redis.StrictRedis(host="localhost", port=6379, db=0,
                                           decode_responses=True)
        else:
            if not str(type(rdb)).startswith("<class 'redis.client."):
                raise TypeError
            else:
                self.redis = rdb
        self.keyname = keyname

    def expire_date_as_score(self):
        future = datetime.datetime.utcnow() + self.default_expire
        return(future.timestamp())

    def add_expiring_item(self, itemId=None):
        if itemId is None:
            return(None)
        rdb = self.redis
        ret = rdb.zadd(self.keyname,
                       self.expire_date_as_score(),
                       itemId)
        return(ret)

    # This needs to be called for expiration to happen
    def expire_items(self):
        timestamp = datetime.datetime.utcnow().timestamp()
        ret = self.redis.zremrangebyscore(self.keyname,
                                          0,
                                          timestamp)
        return(ret)

    def zscan(self):
        return(self.redis.zscan(self.keyname))


if __name__ == '__main__':
    from time import sleep
    from pprint import pprint
    import random
    q5m = DeadSet(keyname="DS_FIVE",
                  default_expire=datetime.timedelta(minutes=5))
    # this item _MAY_ stop existing in 5m:
    q5m.add_expiring_item(itemId=str(random.random()))
    print("UPDATES WILL BE PRINTED EVERY 60 SECONDS")
    while True:
        ret = q5m.expire_items()
        zs = q5m.zscan()
        print("Number of items deleted: {}".format(ret))
        pprint(zs)
        if ret > 0:
            break
        sleep(60)
