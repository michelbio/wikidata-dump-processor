import logging
import argparse

from pymongo import MongoClient


logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='MongoDB host')
    parser.add_argument('port', help='MongoDB port')
    parser.add_argument('db_name', help='Database name')
    parser.add_argument('collection_name', help='Collection name')
    args = parser.parse_args()

    host = args.host
    port = int(args.port)
    db_name = args.db_name
    collection_name = args.collection_name

    logger.info(f'db name: {db_name}')
    logger.info(f'collection name: {collection_name}')
    logger.info('indexing...')
    client = MongoClient(host=host, port=port)
    collection = client[db_name][collection_name]

    # { id: 1 }
    logger.info('index key: { id: 1 }')
    collection.create_index('id', unique=True)

    # { aliases.en.value: 1 }
    logger.info('index key: { aliases.en.value: 1 }')
    key = [('aliases.en.value', 1)]
    pfe = {'aliases.en.value': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { sitelinks.enwiki.title: 1 }
    logger.info('index key: { sitelinks.enwiki.title : 1 }')
    key = [('sitelinks.enwiki.title', 1)]
    pfe = {'sitelinks.enwiki.title': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { sitelinks.enwiki.title: 1, id: 1 }
    logger.info('index key: { sitelinks.enwiki.title: 1, id: 1 }')
    key = [('sitelinks.enwiki.title', 1), ('id', 1)]
    pfe = {'sitelinks.enwiki.title': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { claims.P646 }
    logger.info('index key: { claims.P646 }')
    key = [('claims.P646', 1)]
    pfe = {'claims.P646': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { claims.P646.mainsnak.datavalue.value: 1 }
    logger.info('index key: { claims.P646.mainsnak.datavalue.value: 1 }')
    key = [('claims.P646.mainsnak.datavalue.value', 1)]
    pfe = {'claims.P646.mainsnak.datavalue.value': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { labels }
    logger.info('index key: { labels }')
    key = [('labels', 1)]
    pfe = {'labels': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { labels.en.value: 1, id: 1 }
    logger.info('index key: { labels.en.value: 1, id: 1 }')
    key = [('labels.en.value', 1), ('id', 1)]
    pfe = {'labels.en.value': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { claims.P279 }
    logger.info('index key: { claims.P279 }')
    key = [('claims.P279', 1)]
    pfe = {'claims.P279': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { claims.P279.mainsnak.datavalue.value.id: 1 }
    logger.info('index key: { claims.P279.mainsnak.datavalue.value.id: 1 }')
    key = [('claims.P279.mainsnak.datavalue.value.id', 1)]
    pfe = {'claims.P279.mainsnak.datavalue.value.id': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { claims.P31 }
    logger.info('index key: { claims.P31 }')
    key = [('claims.P31', 1)]
    pfe = {'claims.P31': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { claims.P31.mainsnak.datavalue.value.id: 1 }
    logger.info('index key: { claims.P31.mainsnak.datavalue.value.id: 1 }')
    key = [('claims.P31.mainsnak.datavalue.value.id', 1)]
    pfe = {'claims.P31.mainsnak.datavalue.value.id': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { claims.P30 }
    logger.info('index key: { claims.P30 }')
    key = [('claims.P30', 1)]
    pfe = {'claims.P30': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { claims.P30.mainsnak.datavalue.value.id: 1 }
    logger.info('index key: { claims.P30.mainsnak.datavalue.value.id: 1 }')
    key = [('claims.P30.mainsnak.datavalue.value.id', 1)]
    pfe = {'claims.P30.mainsnak.datavalue.value.id': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { claims.P625 }
    logger.info('index key: { claims.P625 }')
    key = [('claims.P625', 1)]
    pfe = {'claims.P625': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { claims.P625.mainsnak.datavalue.value.latitude: 1 }
    logger.info(
        'index key: { claims.P625.mainsnak.datavalue.value.latitude: 1 }')
    key = [('claims.P625.mainsnak.datavalue.value.latitude', 1)]
    pfe = {'claims.P625.mainsnak.datavalue.value.latitude': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Official Name
    # { claims.P1448: 1 }
    logger.info(
        'index key: { claims.P1448: 1 }')
    key = [('claims.P1448', 1)]
    pfe = {'claims.P1448': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Official Name
    # { claims.P1448.mainsnak.datavalue.value.text: 1 }
    logger.info(
        'index key: { claims.P1448.mainsnak.datavalue.value.text: 1 }')
    key = [('claims.P1448.mainsnak.datavalue.value.text', 1)]
    pfe = {'claims.P1448.mainsnak.datavalue.value.text': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Population
    logger.info(
        'index key: { claims.P1082: 1 }')
    key = [('claims.P1082', 1)]
    pfe = {'claims.P1082': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Population value
    logger.info(
        'index key: { claims.P1082.mainsnak.datavalue.value.amount: 1 }')
    key = [('claims.P1082.mainsnak.datavalue.value.amount', 1)]
    pfe = {'claims.P1082.mainsnak.datavalue.value.amount': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Timezone
    logger.info(
        'index key: { claims.P421: 1 }')
    key = [('claims.P421', 1)]
    pfe = {'claims.P421': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Timezone value
    logger.info(
        'index key: { claims.P421.mainsnak.datavalue.value.id: 1 }')
    key = [('claims.P421.mainsnak.datavalue.value.id', 1)]
    pfe = {'claims.P421.mainsnak.datavalue.value.id': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Area (square km)
    logger.info(
        'index key: { claims.P2046: 1 }')
    key = [('claims.P2046', 1)]
    pfe = {'claims.P2046': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Area (square km) value
    logger.info(
        'index key: { claims.P2046.mainsnak.datavalue.value.amount: 1 }')
    key = [('claims.P2046.mainsnak.datavalue.value.amount', 1)]
    pfe = {'claims.P2046.mainsnak.datavalue.value.amount': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Flag image
    logger.info(
        'index key: { claims.P41: 1 }')
    key = [('claims.P41', 1)]
    pfe = {'claims.P41': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Flag image value
    logger.info(
        'index key: { claims.P41.mainsnak.datavalue.value: 1 }')
    key = [('claims.P41.mainsnak.datavalue.value', 1)]
    pfe = {'claims.P41.mainsnak.datavalue.value': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Coat of arms
    logger.info(
        'index key: { claims.P94: 1 }')
    key = [('claims.P94', 1)]
    pfe = {'claims.P94': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Coat of arms value
    logger.info(
        'index key: { claims.P94.mainsnak.datavalue.value: 1 }')
    key = [('claims.P94.mainsnak.datavalue.value', 1)]
    pfe = {'claims.P94.mainsnak.datavalue.value': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Inception date
    logger.info(
        'index key: { claims.P571: 1 }')
    key = [('claims.P571', 1)]
    pfe = {'claims.P571': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # Inception data value
    logger.info(
        'index key: { claims.P571.mainsnak.datavalue.value.time: 1 }')
    key = [('claims.P571.mainsnak.datavalue.value.time', 1)]
    pfe = {'claims.P571.mainsnak.datavalue.value.time': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)

    # { properties: 1 }
    logger.info('index key: { properties: 1 }')
    key = [('properties', 1)]
    pfe = {'properties': {'$exists': True}}
    collection.create_index(key, partialFilterExpression=pfe)
