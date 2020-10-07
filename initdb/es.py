from elasticsearch import Elasticsearch
from elasticsearch.helpers import parallel_bulk


_es = None
_INDEX = 'bhus'


def _client():
    global _es

    if _es is None:
        _es = Elasticsearch([{'host': 'elasticsearch'}])

    return _es


def bulk_insert(states):
    c = _client()
    c.indices.delete(index=_INDEX, ignore=[400, 404])
    actions = [_state_to_action(s) for s in states]
    parallel_bulk(c, actions)


def count():
    c = _client()
    c.indices.refresh(_INDEX)
    print(c.cat.count(index=[_INDEX,]))


def _state_to_action(state):
    return {
        '_index': _INDEX,
        '_type': 'document',
        'doc': state
    }
