## Flask-DXCaptcha

Flask-DXCaptcha是依赖顶象科技提供的无感验证功能开发的Flask 扩展

### 安装Flask-DXCaptcha

使用**pip**安装

```pip install Flask-DXCaptcha```

### 配置

```the-config.cfg```文件添加配置项

```
DX_APP_ID = 'xxx'
DX_APP_SECRECT = 'xxx'
```

需要从[顶象科技官网](https://www.dingxiang-inc.com/)或者

跟其他扩展使用的方式类型，简单介绍如下

```
from flask_dxcaptcha import DXCaptcha

app = Flask(__name__)
app.config.from_pyfile('the-config.cfg')
dxcaptcha = DXCaptcha(app)
```

或者 

```
from flask import Flask
from flask_dxcaptcha import DXCaptcha
dxcaptcha = DXCaptcha()
...
app = Flask(__name__)
app.config.from_pyfile('the-config.cfg')
dxcaptcha.init_app(app)
```

### 如何使用

```
dxcaptcha.client.setTimeOut(2)

response = dxcaptcha.client.checkToken(v_token)

if response['serverStatus'] == 'SERVER_SUCCESS':
    if response['result'] is False:
        pass
        # token验证失败，业务系统可以直接阻断该次请求或者继续弹验证码
        # 具体的实现逻辑
else:
    pass
    # '提交验证失败，请重新提交'
    # 具体的实现逻辑
```

```v_token```值的获取可以参考官网文档，下面仅是示例

html
```
<div id='c1'></div>
```

javascript
```
<script src="https://cdn.dingxiang-inc.com/ctu-group/captcha-ui/index.js"></script>

<script type='text/javascript'>
var myCaptcha = _dx.Captcha(document.getElementById('c1'), {
  appId: 'appId', // appId
  style: 'popup',
  width: '100%',
  success: function (token) {
    document.getElementById('v_token').value = token;
    myCaptcha.hide();
  }
});
myCaptcha.show();
</script>  
```