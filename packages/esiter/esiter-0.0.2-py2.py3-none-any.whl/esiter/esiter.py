# coding: utf-8


class ESIterator(object):
    """
    基于 ES Scroll API 的迭代器

    https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-scroll.html#search-request-scroll
    """

    def __init__(self, es, yield_source_doc=False):
        """
        :param es: elasticsearch.Elasticsearch object
        :param yield_source_doc: yield hit['_source'] or not
        """
        self._es = es
        self._yield_source_doc = yield_source_doc

    def process_hit(self, hit):
        if self._yield_source_doc:
            return hit['_source']
        else:
            return hit

    def search(self, body, index, doc_type, es_scroll='1m', es_size=100, params=None):
        """
        :param body:
        :param index:
        :param doc_type:
        :param es_scroll:
        :param es_size:
        :param params:
        :return: (idx, total, doc)
        """
        params = params or {}
        assert 'size' not in params
        params['size'] = es_size
        if 'sort' not in params:
            # scroll requests have optimizations that make them faster when the sort order is _doc
            params['sort'] = '_doc'
        resp = self._es.search(
            index=index,
            doc_type=doc_type,
            body=body,
            scroll=es_scroll,
            params=params
        )
        yielded_idx = 0
        for hit in resp['hits']['hits']:
            yield yielded_idx, resp['hits']['total'], self.process_hit(hit)
            yielded_idx += 1

        while True:
            resp = self._es.scroll(scroll_id=resp['_scroll_id'], scroll=es_scroll)
            if not resp['hits']['hits']:  # 全部遍历完了
                break
            for hit in resp['hits']['hits']:
                yield yielded_idx, resp['hits']['total'], self.process_hit(hit)
                yielded_idx += 1
