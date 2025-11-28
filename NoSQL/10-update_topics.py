#!/usr/bin/env python3
"""fijwdnfvudevmd"""


def update_topics(mongo_collection, name, topics):
    """fowdifvidvvf"""
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics }}
    )
