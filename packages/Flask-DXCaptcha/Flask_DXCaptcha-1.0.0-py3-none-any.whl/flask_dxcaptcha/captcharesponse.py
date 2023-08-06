# -*- coding: utf-8 -*-
# @Author: durban.zhang
# @Date:   2019-12-25 16:42:46
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-12-25 17:04:07


class CaptchaResponse:
    result = False
    serverStatus = ""

    def __init__(self, result, serverStatus):
        self.result = result
        self.serverStatus = serverStatus

    def setResult(self, result):
        self.result = result

    def setServerStatus(self, serverStatus):
        self.serverStatus = serverStatus
