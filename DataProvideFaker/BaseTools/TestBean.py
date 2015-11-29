__author__ = 'jacky'
# package: com.example.jacky.testgreendao.modle
#
#  * project     TestGreenDao
#  *
#  * @author hewei
#  * @verstion 15/11/17
#


class TestBean:
    """ generated source for class TestBean """
    FIELD_MSG_TEXT = "msg"
    FIELD_ERR_CODE = "err"
    FIELD_DATA_OBJ_BOOKBEAN = "book_data"
    FIELD_DATA_IMAGE = "img"

    mMsg = "aa"
    mErr = 1
    mData = ""
    mImage=""



if __name__ == '__main__':
    list_tmp = (dir(TestBean))
    print(list_tmp)
