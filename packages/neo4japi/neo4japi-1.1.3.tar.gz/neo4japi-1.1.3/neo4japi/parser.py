# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 17:11
# @Author  : floatsliang
# @File    : parser.py
import json
import random
import string
from typing import List, Tuple, Dict


def _serialize(val):
    if isinstance(val, Dict):
        val = json.dumps(val)
    else:
        pass
    return val


def _generate_unique_id():
    # 有一千万分之一的概率相同
    return ''.join(random.choices(string.digits, k=8))


def parse_labels(labels: List[str], div=':') -> str:
    parsed_labels = []
    for label in labels:
        parsed_labels.append(label)
    return ':' + div.join(parsed_labels) if parsed_labels else ''


def parse_fields(fields: List[str]) -> str:
    for idx, field in enumerate(fields):
        if '__' in field:
            fields[idx] = field.replace('__', '.', 1)
        else:
            pass
    return ', '.join(fields)


def parse_order_by(order_by: List[List or Tuple]) -> str:
    order_bys = []
    for field, order in order_by:
        if '__' in field:
            field = field.replace('__', '.', 1)
        elif '.' in field:
            pass
        else:
            raise Exception(u'ERROR: expected order by property format: '
                            u'[node].[property] or [node]__[property], got {}'.format(field))
        order_bys.append(u'{} {}'.format(field, order))
    if order_bys:
        return 'ORDER BY {}'.format(','.join(order_bys))
    else:
        return ''


def parse_terms(terms: Dict) -> Dict:
    filters = []
    params = {}
    for field, term in terms.items():
        if '__' in field:
            field = field.replace('__', '.', 1)
        elif '.' in field:
            pass
        else:
            raise Exception(u'ERROR: expected where filter property format: '
                            u'[node].[property] or [node]__[property], got {}'.format(field))
        _field = field.replace('.', '_')
        if isinstance(term, (list, tuple)):
            op = term[1].strip()
            if len(term) == 3:
                relation = u' {} '.format(term[2].strip()).upper()
            else:
                relation = ' AND '
            values = term[0]
            if op.lower() == 'in':
                if isinstance(values, (list, tuple)):
                    _uid = u'{}{}'.format(_field, _generate_unique_id())
                    values = [_serialize(val) for val in values if val is not None]
                    if values:
                        filters.append(u'{} IN ${}'.format(field, _uid))
                        params[_uid] = values
            elif op.lower() == 'join':
                if isinstance(values, (list, tuple)):
                    values = [val.replace('__', '.', 1) for val in values if val is not None]
                    if values:
                        filters.append(u'({})'.format(
                            relation.join([u'{} = {}'.format(field, _serialize(val)) for val in values])))
                else:
                    if values is not None:
                        filters.append(u'{} = {}'.format(field, _serialize(values.replace('__', '.', 1))))
            else:
                if isinstance(values, (list, tuple)):
                    values = [_serialize(val) for val in values if val is not None]
                    if values:
                        sub_q = []
                        for val in values:
                            _uid = u'{}{}'.format(_field, _generate_unique_id())
                            sub_q.append(u'{} {} ${}'.format(field, op, _uid))
                            params[_uid] = val
                        filters.append(u'({})'.format(relation.join(sub_q)))
                else:
                    if values is not None:
                        _uid = u'{}{}'.format(_field, _generate_unique_id())
                        filters.append(u'{} {} ${}'.format(field, op, _uid))
                        params[_uid] = _serialize(values)
        else:
            if term is not None:
                _uid = u'{}{}'.format(_field, _generate_unique_id())
                filters.append(u'{} = ${}'.format(field, _uid))
                params[_uid] = _serialize(term)
    filters = ' AND '.join(filters)
    return {"filters": filters, "params": params}


def parse_properties(properties: Dict, eq=':') -> Dict:
    property_list = []
    params = {}
    for key, val in properties.items():
        _key = key.replace('.', '_')
        _uid = u'{}{}'.format(_key, _generate_unique_id())
        if val is not None:
            if '__' in key:
                key = key.replace('__', '.', 1)
            elif '.' not in key and eq != ':':
                raise Exception('ERROR: expected property name format: '
                                '[node].[property] or [node]__[property], got {}'.format(key))
            property_list.append(u'{} {} ${}'.format(key, eq, _uid))
            params[_uid] = _serialize(val)
    properties = ', '.join(property_list)
    return {'properties': properties, 'params': params}
