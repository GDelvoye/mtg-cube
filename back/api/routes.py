from api_pool.mongo.filter import filter_pool


def filter_route(payload):
    return filter_pool(payload)
