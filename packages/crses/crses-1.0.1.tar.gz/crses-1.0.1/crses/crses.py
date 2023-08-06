# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
import elasticsearch
import crsts

class EsTools(object):
    def __init__(self,host='localhost',port=9200):
        self.es = elasticsearch.Elasticsearch([{"host":host,"port":port}])

    def insert_record(self,index,body,doc_type="_doc",id=None):
        try:
            return self.es.index(index=index, doc_type=doc_type, id=id, body=body)
        except:
            return None

    def delete_record(self, index, id, doc_type="_doc"):
        try:
            return self.es.delete(index=index, id=id, doc_type=doc_type)
        except:
            return None

    def delete_index(self, index):
        try:
            return self.es.indices.delete(index=index)
        except:
            return None

    def delete_all_record(self, index):
        try:
            return self.es.delete_by_query(index=index, body={'query': {'match_all': {}}})
        except:
            return None

    def query_by_id(self, index, id, doc_type="_doc"):
        try:
            return self.es.get(index=index, doc_type=doc_type, id=id)
        except:
            return None

    def query_table(self, index=None, query=None):
        '''
        Query example:
            {'query': {'match_all': {}}}  # 查找所有文档
            {'query': {'match': {'sex': 'famale'}}}  # 删除性别为女性的所有文档
            {'query': {'range': {'age': {'lt': 11}}}}  # 删除年龄小于11的所有文档
            {'query': {'term': {'name': 'jack'}}}  # 查找名字叫做jack的所有文档
        '''
        try:
            result = self.es.search(index=index, body=query)
            return result['hits']['hits']
        except:
            return None

    def update_record(self, index, id, doc_type="_doc", body=None):
        try:
            return self.es.update(index=index, id=id, doc_type=doc_type, body={"doc": body})
        except:
            return None