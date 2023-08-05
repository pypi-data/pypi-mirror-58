# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 17:04
# @Author  : floatsliang
# @File    : api.py
from neo4j import GraphDatabase, basic_auth, Transaction, types
from logging import getLogger
from typing import List, Dict, Union
from functools import wraps

from .cql import Node, Relation, Match, Merge, Create

DEFAULT_CONF = {
    "uri": "bolt://127.0.0.1:7687",
    "username": "neo4j",
    "password": "neo4j"
}

__all__ = ['Neo4jApi', 'Node', 'Relation']


def result_wrapper(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        r = func(*args, **kwargs)
        r_list = list(r)
        for idx, rec in enumerate(r_list):
            rec_dict = dict(rec)
            for k, v in rec_dict.items():
                if isinstance(v, types.graph.Node):
                    rec_dict[k] = dict(v)
            r_list[idx] = rec_dict
        return r_list

    return wrapped


class Neo4jApi(object):
    logger = getLogger("Neo4jApi")

    def __init__(self, config=None):
        if not config:
            config = DEFAULT_CONF
        config = config.copy()
        username = config.pop('username')
        password = config.pop('password')
        config['auth'] = basic_auth(username, password)
        self.driver = GraphDatabase.driver(**config)
        self._cli = self.driver.session()
        self._cql_stack = None

    def __enter__(self):
        self._cli.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cli.__exit__(exc_type, exc_val, exc_tb)

    def start_transaction(self):
        return self._cli.begin_transaction()

    def index(self, table=None, on=None, drop=False, t=None):
        if drop:
            op = 'DROP'
        else:
            op = 'CREATE'
        _cql = u'{op} INDEX ON :{table} ({on})'.format(op=op, table=table, on=on)
        if self._cql_stack:
            self.execute(t)
        self._cql_stack = _cql
        self.execute(t)

    def unique(self, table=None, on=None, drop=False, t=None):
        if drop:
            op = 'DROP'
        else:
            op = 'CREATE'
        _cql = u'{op} CONSTRAINT ON (label:{table}) ASSERT label.{on} IS UNIQUE'.format(op=op, table=table, on=on)
        if self._cql_stack:
            self.execute(t)
        self._cql_stack = _cql
        self.execute(t)

    def exists(self, table=None, on=None, drop=False, t=None):
        if drop:
            op = 'DROP'
        else:
            op = 'CREATE'
        _cql = u'{op} CONSTRAINT ON (label:{table}) ASSERT exists(label.{on})'.format(op=op, table=table, on=on)
        if self._cql_stack:
            self.execute(t)
        self._cql_stack = _cql
        self.execute(t)

    def select(self, fields: Union[List, str] = None, tables: Union[List, str] = None, distinct: bool = False,
               order_by: List = None, limit: int = None, offset: int = None, t: Transaction = None,
               result_name: str = 'nodes', **terms):
        """
        select node with condition
        :param result_name:
        :param distinct:
        :param fields:
        :param tables:
        :param order_by:
        :param limit:
        :param offset:
        :param t:
        :param terms:
        :return:
        """
        if not tables:
            raise Exception(u'ERROR: select node must have Labels/RelType')
        if not fields:
            fields = result_name
        else:
            if not isinstance(fields, (list, tuple)):
                fields = [fields]
            for idx, field in enumerate(fields):
                fields[idx] = u'{}.{}'.format(result_name, field)
        new_terms = {}
        for k, v in terms.items():
            new_terms[u'{}.{}'.format(result_name, k)] = v
        _cql = Match(Node(result_name, labels=tables)).Where(**new_terms).Return(fields=fields, distinct=distinct,
                                                                                 order_by=order_by, limit=limit,
                                                                                 skip=offset)
        self._cql_stack = self._cql_stack + _cql if self._cql_stack else _cql
        return self.execute(t)

    def get_one(self, fields=None, tables=None, order_by=None, offset=None, t=None, compile=False, result_name='result',
                **terms):
        return self.select(fields=fields, tables=tables, order_by=order_by, limit=1, offset=offset, t=t,
                           compile=compile, result_name=result_name, **terms)

    def save(self, tables: str = None, t: Transaction = None, compile: bool = False, **properties):
        """
        insert one node into neo4j (even already exists)
        :param compile:
        :param tables:
        :param t:
        :param properties:
        :return:
        """
        if not tables:
            raise Exception(u'ERROR: save node must have Labels/RelType')
        if properties:
            return self.insert([Node(labels=tables, **properties)], t=t, compile=compile)

    def insert(self, nodes: Union[List[Node], Node], t: Transaction = None, compile: bool = False):
        """
        insert many node into neo4j
        :param compile:
        :param nodes:
        :param t:
        :return:
        """
        if not nodes:
            return self
        if not isinstance(nodes, (list, tuple)):
            nodes = [nodes]
        _cql = Create(*nodes)
        self._cql_stack = self._cql_stack + _cql if self._cql_stack else _cql
        if compile:
            return self
        else:
            return self.execute(t)

    def select_by_nodes(self, nodes: Union[List[Node], Node], t: Transaction = None, compile: bool = False,
                        results='nodes', limit=None, **terms):
        if not nodes:
            raise Exception(u'ERROR: select node must have Labels/RelType')
        if not isinstance(nodes, (list, tuple)):
            nodes = [nodes]
        _cql = Match(*nodes)
        if terms:
            _cql.Where(**terms)
        self._cql_stack = self._cql_stack + _cql if self._cql_stack else _cql
        if compile:
            if limit:
                _cql.With(limit=limit)
            return self
        else:
            self._cql_stack = self._cql_stack.Return(fields=results, limit=limit)
            return self.execute(t)

    def select_or_insert(self, node: Node, t: Transaction = None, compile: bool = False, results=None):
        """
        insert or update node
        :param results:
        :param node:
        :param compile:
        :param t:
        :return:
        """
        if not node:
            raise Exception(u'ERROR: select or insert node must have Labels/RelType')
        _cql = Merge(node)
        self._cql_stack = self._cql_stack + _cql if self._cql_stack else _cql
        if compile:
            return self
        else:
            if results:
                self._cql_stack = self._cql_stack.Return(fields=results)
            return self.execute(t)

    def update(self, t: Transaction = None, compile: bool = False, results: str = None, **new_properties):
        _cql = self._cql_stack
        if not _cql:
            raise Exception(u'ERROR: update node/relationship must have Labels/RelType')
        if not new_properties:
            self.logger.warning('update node/relationship without giving values')
            return self
        _cql.Set(**new_properties)
        if compile:
            return self
        else:
            if results:
                self._cql_stack = self._cql_stack.Return(fields=results)
            return self.execute(t)

    def delete(self, detach=False, fields: Union[List, str] = None, t=None, compile=False,
               results: str = None):
        _cql = self._cql_stack
        if not _cql:
            raise Exception(u'ERROR: delete node must have Labels/RelType')
        if not isinstance(fields, (list, tuple)):
            fields = [fields]
        self._cql_stack = _cql.Delete(detach=detach, fields=fields)
        if compile:
            return self
        else:
            if results:
                self._cql_stack = self._cql_stack.Return(fields=results)
            return self.execute(t)

    def related(self, origin: Node, relation: Relation, target: Node, unique=True, t=None, compile=False,
                results=None):
        if not relation or not origin or not target:
            raise Exception(u'ERROR: create relationship must have relation and origin/target node')
        if unique:
            _cql = Merge(origin.relationship_to(relation, target))
        else:
            _cql = Create(origin.relationship_to(relation, target))
        self._cql_stack = self._cql_stack + _cql if self._cql_stack else _cql
        if compile:
            return self
        else:
            if results:
                self._cql_stack = self._cql_stack.Return(fields=results)
            return self.execute(t)

    def has_relation(self, origin: Node, relation: Relation, target: Node, direction=True, t=None,
                     results='relation'):
        if not relation or not origin or not target:
            raise Exception(u'ERROR: search relationship must have relation type')
        if direction:
            _cql = Match(origin.relationship_to(relation, target))
        else:
            _cql = Match(origin.relationship(relation, target))
        self._cql_stack = _cql.Return(fields=results)
        return self.execute(t)

    def traverse(self):
        pass

    def look_around(self, origin_table, origin_properties, relation: Union[List, str] = None, relation_properties=None,
                    depth: int = 5, target_table=None, target_properties=None, results='target', t=None):
        if not origin_table or not origin_properties:
            raise Exception(u'ERROR: origin node must be accurately located when looking around it')
        if depth:
            depth = (1, depth)
        else:
            depth = (1, 5)
        _cql = Match(Node('origin', labels=origin_table, **origin_properties).relationship(
            Relation(labels=relation, depth=depth, **relation_properties),
            Node(results, labels=target_table, **target_properties)))
        self._cql_stack = _cql.Return(fields=results)
        return self.execute(t)

    def family(self):
        pass

    def results(self, fields: List[str], distinct: bool = False, order_by: List = None, skip: int = None,
                limit: int = None, compile=False, t=None):
        _cql = self._cql_stack
        if not _cql:
            raise Exception(u'ERROR: Return results statement cannot be used as root statement')
        self._cql_stack = _cql.Return(fields=fields, distinct=distinct, order_by=order_by, skip=skip, limit=limit)
        if compile:
            return self
        else:
            return self.execute(t)

    def count(self, field: str, distinct: bool = True, compile=False, t=None):
        _cql = self._cql_stack
        if not _cql:
            raise Exception(u'ERROR: Count results statement cannot be used as root statement')
        self._cql_stack = _cql.Return(fields=field, distinct=distinct, count=True)
        if compile:
            return self
        else:
            return self.execute(t)

    @result_wrapper
    def execute(self, t=None):
        _conn = t if t else self._cli
        _cql = self._cql_stack.cql
        self._cql_stack = None
        return _conn.run(_cql['cql'], _cql['params'])

    @property
    def query(self):
        return self._cql_stack.cql
