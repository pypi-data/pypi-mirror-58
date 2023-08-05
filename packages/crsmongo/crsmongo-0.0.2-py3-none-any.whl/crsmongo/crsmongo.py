# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
import pymongo

class MonogoTools(object):
    def __init__(self,ip='',db_name='',port='27017'):
        conn_str = f'mongodb://{ip}:{port}/'
        self.client = pymongo.MongoClient(conn_str, unicode_decode_error_handler='ignore')
        self.db = self.client[db_name]

    def get_from_collection(self,collection_name,condition={}):
        return self.db[collection_name].find(condition)

    def get_collection_count(self,collection_name,condition={}):
        return self.db[collection_name].find(condition).count()

    def get_one_from_collection(self,collection_name,condition={}):
        return self.db[collection_name].find_one(condition)

    def insert_into_collection(self,collection_name,data={}):
        inserted_id = self.db[collection_name].insert_one(data).inserted_id
        return inserted_id

    def list_all_collections(self):
        return self.db.list_collection_names()
