# -*- coding:utf-8 -*-
import random
import time
from DataProvideFaker.BaseTools.Config import DBHelperUtils

__author__ = 'jacky'

["user_name", "user_image", "common_img", "city_name", "city_code", 'price']

from faker import Factory

class FakerMapping:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(FakerMapping, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self, county = 'zh_CN'):

        self.fake = Factory.create(county)
        self.img = DBHelperUtils().get_imgs()
        self.img_size = len(self.img)

        self.data_format = {
            "用户名":"USER_NAME",
            "照片":"IMAGE",
            "邮箱":"EMAIL",
            "城市":"CITY",
            "字符串":"TEXT",
            "时间戳":"TIME",
            "错误代码":"ERR_CODE",
            "单词":"WORD",
            "ID":"ID",
            "对象":"OBJ"

        }

        self.erro_code_list = [
            0,
            60501,
            605002,
            605003,
            401003,
        ]


    def get_ramdon_img(self):
        index = random.randint(0, self.img_size)
        return self.img[index]

    def __get_cls_name(self, low_case_string):

        key_word_list = low_case_string.split("_")

        if len(key_word_list) > 0:

            return key_word_list[len(key_word_list) - 1]

        else:
            return None




    def __get_cate_obj(self, low_case_string):

        _cls_name = self.__get_cls_name(low_case_string)

        print _cls_name

        if _cls_name is None:
            return None


        _packet_name = _cls_name
        _module_home = __import__(_packet_name,globals(),locals(),[_cls_name])

        obj =  getattr(_module_home,_cls_name)

        return obj()


    def get_data(self, surfix ='FILED'):
        if surfix is None:
            return None

        usurfix = surfix.upper()

        if usurfix.count(self.data_format["用户名"]) >0 :
            return self.fake.name()

        if usurfix.count(self.data_format['邮箱'])>0:
            return self.fake.word() + self.fake.email()

        if usurfix.count(self.data_format['照片'])>0:
            return self.get_ramdon_img()

        if usurfix.count(self.data_format['城市']) > 0:
            return self.fake.city_name()

        if usurfix.count(self.data_format['字符串']) > 0:
            return self.fake.text(max_nb_chars=200)

        if usurfix.count(self.data_format['时间戳']) > 0:
            return int(time.time()) - random.randint(0, 200)

        if usurfix.count(self.data_format['错误代码']) > 0:
            return self.erro_code_list[0]

        if usurfix.count(self.data_format['单词']) > 0:
            return self.fake.text(max_nb_chars=5)

        if usurfix.count(self.data_format['ID']) > 0:
            return random.randint(1, 2000)

        if usurfix.count(self.data_format['对象']) > 0:

            return self.__get_cate_obj(usurfix.lower())





if __name__ == '__main__':

    mapping = FakerMapping()

    print mapping.get_data('USER_NAME')
    print mapping.get_data('EMAIL')
    print mapping.get_data('IMAGE')
    print mapping.get_data('TEXT')
    print mapping.get_data('TIME')
    print mapping.get_data('ERR_CODE')

    print mapping.get_data('FIELD_DATA_OBJ_BOOKBEAN')



