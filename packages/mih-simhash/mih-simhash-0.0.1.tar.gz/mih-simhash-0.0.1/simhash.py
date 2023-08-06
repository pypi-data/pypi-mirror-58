# encoding: utf-8

import hashlib
import asyncio
import jieba.analyse

from redis import hit


class SimHash(object):


    def __init__(self, num_drawer=4, num_words=100):

        self.num_drawer = num_drawer
        self.num_words  = num_words
        self.num_bits   = 256



    def preprocess_keywords(self, doc):

        pos = ('n' , 's' , 't'  , 'nr' , 'ns' ,
               'nt', 'nw', 'nz' , 'v'  , 'vd' ,
               'vn', 'a' , 'ad' , 'an' , 'd'  ,
                'm', 'q' , 'PER', 'LOC', 'ORG', 'TIME')

        kww = jieba.analyse.extract_tags(doc, topK=self.num_words, withWeight=True, allowPOS=pos)

        keywords, weights = zip(*kww)

        return keywords, weights


    
    def preprocess_hash(self, keywords):

        hashkeywords = [format(int(hashlib.sha256(kw.encode()).hexdigest(),16),'b')\
                        .zfill(self.num_bits)
                        for kw in keywords]

        return hashkeywords



    def preprocess_fingerprint(self, hashkeywords, weights):

        length_words = len(hashkeywords)

        fingerprint = ''.join([str(int(sum([int(hashkeywords[j][i])*weights[j]
                      for j in range(length_words)])>0))
                      for i in range(self.num_bits)])

        return fingerprint



    def preprocess(self, title, content):

        doc               = title + content
        keywords, weights = self.preprocess_keywords(doc)
        hashkeywords      = self.preprocess_hash(keywords)
        fingerprint       = self.preprocess_fingerprint(hashkeywords, weights)

        return fingerprint



    def fit_predict(self, title, content):

        fingerprint = self.preprocess(title, content)
        eid, ename  = asyncio.get_event_loop()\
                      .run_until_complete(hit(fingerprint, title, self.num_drawer))

        return eid, ename
