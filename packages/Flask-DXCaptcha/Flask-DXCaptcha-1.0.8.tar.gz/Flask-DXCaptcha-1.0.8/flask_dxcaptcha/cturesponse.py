# -*- coding: utf-8 -*-
# @Author: durban.zhang
# @Date:   2019-12-25 16:42:46
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-12-25 17:02:57


class CtuResponse:

    def __init__(self, uuid, status, result):
        self.uuid = uuid
        self.status = status
        self.result = result
