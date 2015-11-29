import pymongo
import redis

__author__ = 'jacky'

# MongoDB
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_VOD_DB = "tmp_test"
THIRD_VOD_INFO_COLLECTION = "third_vod_info"


class DBHelperUtils():

    def __init__(self):
        connection = pymongo.MongoClient(
            MONGODB_SERVER,
            MONGODB_PORT
        )

        db = connection[MONGODB_VOD_DB]
        self.collection = db[THIRD_VOD_INFO_COLLECTION]

    def save(self, Item):
        self.collection.insert(Item)

    def get_imgs(self):

        ulr_list = []

        for item in self.collection.find():
            ulr_list.append( item['url'])
        return  ulr_list
if __name__ == '__main__':

    print DBHelperUtils().get_imgs()
