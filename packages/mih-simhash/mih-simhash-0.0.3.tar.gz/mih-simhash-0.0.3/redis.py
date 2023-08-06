# encoding: utf-8

import os
import aioredis


from configparser import ConfigParser



def xor(k1, k2):

    return format(int(k1, 2) ^ int(k2, 2), 'b').count('1')



def keypair(key, seq, num_drawer):

    length = int(len(key) / num_drawer)
    start  = seq * length
    end    = start + length

    key_head = key[start:end]
    key_tail = key[:start] + key[end:]

    return key_head, key_tail



def keyrecover(key_head, key_tail, seq, num_drawer):

    length = int((len(key_head)+len(key_tail)) / num_drawer)
    start  = seq * length
    end    = start + length

    key1   = key_head if 0 == seq else key_tail[:start]
    key2   = '' if 0 == seq or (num_drawer-1) == seq else key_head
    key3   = key_tail if 0 == seq else\
             key_head if (num_drawer-1) == seq else key_tail[len(key1):]

    key    = key1 + key2 + key3

    return key



async def hit(fingerprint, title, num_drawer, path_config=None):

    cfg = ConfigParser()

    path_config = path_config if path_config is not None else\
                  os.path.join(os.path.dirname(__file__), 'config.cfg')
    cfg.read(path_config)
    
    host = cfg.get('redis', 'host')
    port = cfg.getint('redis', 'port')

    conn = await aioredis.create_connection((host, port))

    redis = aioredis.Redis(conn)

    # check direct
    await redis.select(0)
    event = await redis.lrange(fingerprint, 0, 2)

    if not event:
        found = False
        max_distance = num_drawer - 1

        # check indirect
        for i in range(1, num_drawer+1):
            await redis.select(i)

            # make keypair
            key_head, key_tail = keypair(fingerprint, i-1, num_drawer)

            # candidates
            key_tail_finds = await redis.lrange(key_head, 0, -1)

            if key_tail_finds is None: continue

            # near approximate
            # found
            for key in key_tail_finds:
                if max_distance >= xor(key_tail, key.decode()):
                    found = True
                    fingerprint_near = keyrecover(key_head, key.decode(), i-1, num_drawer)
                    await redis.select(0)
                    eid, ename = await redis.lrange(fingerprint_near, 0, 2)
                    break

            if found: 
                break


        # create
        # not found
        if not found:
            eid   = '{0:0>4x}'.format(int(fingerprint, 2)).encode()
            ename = title.encode()
        
        # update "direct"
        await redis.select(0)
        await redis.rpush(fingerprint, eid, ename)

        # update "indirect"
        for i in range(1, num_drawer+1):
            await redis.select(i)
            key_head, key_tail = keypair(fingerprint, i-1, num_drawer)
            await redis.rpush(key_head, key_tail)

    else:
        
        eid, ename = event



    redis.close()

    return eid.decode(), ename.decode()
