# -*- coding: utf-8 -*-
# @Author: durban.zhang
# @Date:   2019-12-25 17:02:16
# @Last Modified by:   durban
# @Last Modified time: 2019-12-25 18:43:25

from flask import current_app, _app_ctx_stack

from flask_dxcaptcha.captchaclient import CaptchaClient


class DXCaptcha(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('DX_APP_ID', '')
        app.config.setdefault('DX_APP_SECRECT', '')

    def init_captcha_client(self):
        if current_app.config['DX_APP_ID'] == '' or \
                current_app.config['DX_APP_SECRECT'] == '':
            raise Exception('DX_APP_ID and DX_APP_SECRECT can not empty.')

        return CaptchaClient(
            current_app.config['DX_APP_ID'],
            current_app.config['DX_APP_SECRECT'],
        )

    @property
    def client(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'dx_captcha'):
                ctx.dx_captcha = self.init_captcha_client()
            return ctx.dx_captcha
