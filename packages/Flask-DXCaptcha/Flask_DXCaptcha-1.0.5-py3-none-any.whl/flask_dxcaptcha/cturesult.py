# -*- coding: utf-8 -*-
# @Author: durban.zhang
# @Date:   2019-12-25 16:42:46
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-12-25 17:35:14

from .risklevel import RiskLevel


class CtuResult:

    def __init__(self, riskLevel, riskType):
        self.riskLevel = riskLevel
        self.riskType = riskType

    def hasRisk(self):
        return RiskLevel.REJECT == self.riskLevel or\
            RiskLevel.REVIEW == self.riskLevel

    def getRiskLevel(self):
        return self.riskLevel
