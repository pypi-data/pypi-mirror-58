# coding: utf-8
from concurrent.futures.thread import ThreadPoolExecutor
from esiter import ESIterator

import logging


class ESMigration(object):
    """ 将一个 Elasticsearch 实例中的数据迁移到另一个 Elasticsearch 实例中 """

    def __init__(
            self,
            from_es,
            from_index,
            to_es,
            to_index,
            search_body=None,
            threads=15,
            from_doc_type=None,
            logger=logging.getLogger(__name__),
    ):
        """
        :param from_es: elasticsearch.Elasticsearch object
        :type from_es: elasticsearch.Elasticsearch
        :type from_index: str
        :param to_es:elasticsearch.Elasticsearch object
        :type to_es:elasticsearch.Elasticsearch
        :type to_index:str
        :type threads: int
        :type from_doc_type: str | None
        :type search_body: dict | None
        :param logger:
        """
        self.from_es = from_es
        self.from_index = from_index
        self.from_doc_type = from_doc_type

        self.to_es = to_es
        self.to_index = to_index

        self.es_iter = ESIterator(from_es, yield_source_doc=False)
        self.search_body = search_body
        self.pool = ThreadPoolExecutor(threads)
        self.logger = logger

    def index(self, doc):
        try:
            resp = self.to_es.index(
                id=doc['_id'],
                body=doc['_source'],
                index=self.to_index,
                doc_type=doc['_type'],
            )
            self.logger.info(resp)
        except Exception:
            self.logger.exception('error when index doc')

    def migrate(self):
        for idx, _, doc in self.es_iter.search(self.search_body, index=self.from_index, doc_type=self.from_doc_type):
            self.pool.submit(self.index, doc)
