import shelve


class PutCookie:
    def put_cookie(self):
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
          'value': '1716275423840412'},
         {'domain': 'work.weixin.qq.com', 'expiry': 1599328776, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
          'secure': False, 'value': '4scnvb7'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
          'value': 'direct'},
         {'domain': '.work.weixin.qq.com', 'expiry': 1630833240, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/',
          'secure': False, 'value': '0'},
         {'domain': '.work.weixin.qq.com', 'expiry': 1601889241, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
          'path': '/', 'secure': False, 'value': 'zh-cn'}]

        db = shelve.open("../cookie_db/weixin_cookie")
        db['cookie'] = cookies
        db.close()


PutCookie().put_cookie()