### Neo4jApi

A simple Neo4j api driver.

#### Usage

* select node/relation from neo4j:
```python
with Neo4jApi() as dbi:
    res = (dbi.select_by_nodes(
        Node('ds', labels='DATASET', datasource_id=1)
        .relationship(Relation('rel'), Node('sj', labels='SUB_DATAJOB')),
        ds__id=1, ds__name=(['kafka', 'elastisearch'], 'IN')))
```

* start a transaction:
```python
with Neo4jApi() as dbi:
    with dbi.start_transaction() as _t:
        dbi.insert(Node(labels='DATASOURCE', **data_source), t=_t)
```