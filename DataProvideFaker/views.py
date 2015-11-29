import json
from django.http import HttpResponse
from DataProvideFaker.BaseTools.DataFaker import DataFaker
from DataProvideFaker.BaseTools.TestBean import TestBean

__author__ = 'jacky'

import faker


def index(req):
    response_data = dict()
    response_data = DataFaker().get_dict(TestBean())
    return HttpResponse(json.dumps(response_data), content_type="application/json")


if __name__ == '__main__':
    print DataFaker().get_dict(TestBean())
