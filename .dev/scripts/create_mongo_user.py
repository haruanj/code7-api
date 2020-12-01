import os
import pymongo


def create_mongo_user():
    """ Create user on MongoDB """
    mongo_url = "mongodb://mongo:mongo@code7-mongo/admin"
    database = "code7"
    username = "code7"
    password = "code7"

    client = pymongo.MongoClient(mongo_url)
    mongo_db = pymongo.database.Database(client, database)

    mongo_db.add_user(
        username,
        password=password,
        **{"roles": [{"role": "readWrite", "db": database}, {"role": "dbAdmin", "db": database}]}
    )


if __name__ == "__main__":
    create_mongo_user()
