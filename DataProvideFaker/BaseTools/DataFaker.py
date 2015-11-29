import json
import time
from DataProvideFaker.BaseTools.FakerMapping import FakerMapping
from DataProvideFaker.BaseTools.TestBean import TestBean

__author__ = 'jacky'

from faker import Factory


class DataFaker:
    def __init__(self):
        self.fake_mapping = FakerMapping()

    def get_attri(self, obj):
        list = (dir(obj))
        return list

    def get_dict(self, obj):
        attri_list = self.get_attri(obj)
        class_dic = {}
        for item in attri_list:
            if item.startswith("FIELD_"):
                if item.count("OBJ") > 0:
                    tmp_obj = self.fake_mapping.get_data(item)
                    class_dic.update({getattr(obj, item): self.get_dict(tmp_obj)})

                else:
                    class_dic.update({getattr(obj, item): self.fake_mapping.get_data(item)})

        return class_dic


if __name__ == '__main__':
    # data_faker = DataFaker()
    #print data_faker.get_dict(TestBean())
    print int(time.time())
    print time.strftime("%Y-%m-%d %H:%M:%S")
    timeArray = time.strptime(time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))

    print timeStamp










