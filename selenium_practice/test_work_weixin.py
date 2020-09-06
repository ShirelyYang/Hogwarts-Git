import shelve

from selenium import webdriver


class TestWorkWX:
    def test_work_weixin(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        db = shelve.open("../test_project/cookie_db/weixin_cookie")
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def test_cookie(self):
        db = shelve.open("../test_project/cookie_db/weixin_cookie")
        cookies = db['cookie']
        db.close()
        print(cookies)
        cookies2 = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850770889759'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid',
                                            'path': '/', 'secure': False, 'value': '1688850770889759'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                'secure': False, 'value': '1970325048156169'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False,
                                                                'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
                                                                'value': 'a2234'}, {'domain': 'work.weixin.qq.com',
                                                                                    'expiry': 1599391401,
                                                                                    'httpOnly': True,
                                                                                    'name': 'ww_rtkey', 'path': '/',
                                                                                    'secure': False,
                                                                                    'value': '8sivtiv'}, {
                'domain': '.qq.com', 'expiry': 1599446276, 'httpOnly': False, 'name': '_gid', 'path': '/',
                'secure': False, 'value': 'GA1.2.1493185445.1599359867'}, {'domain': '.work.weixin.qq.com',
                                                                           'httpOnly': True, 'name': 'wwrtx.refid',
                                                                           'path': '/', 'secure': False,
                                                                           'value': '17162754232265843'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
                'value': 'uo-QflXh9v6QZB4C_gZdFSu9P85OlsscYxPsOMcAiRC-eaM1f0DshWT2otUhUPXl'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
                'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/',
                                'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1599359927,
                                                                      'httpOnly': False, 'name': '_gat', 'path': '/',
                                                                      'secure': False, 'value': '1'}, {
                'domain': '.qq.com', 'expiry': 1662431876, 'httpOnly': False, 'name': '_ga', 'path': '/',
                'secure': False, 'value': 'GA1.2.462047580.1599359867'}, {'domain': '.work.weixin.qq.com',
                                                                          'expiry': 1630895865, 'httpOnly': False,
                                                                          'name': 'wwrtx.c_gdpr', 'path': '/',
                                                                          'secure': False, 'value': '0'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                'value': 'nRLDkaBfySUShu31hhhsDH2wslDa1Br-A-I3TQ5l2V0fAh70R1CEOAPw0G26gVLMosHsRu_toTA0Unk9UsBnPOrHE04KwAkPlurkMv6xX3nvd4TRE26-E-fgsKuudet9kRveLqmau6XrdRsP2ckchyBMEfIjmES3YDA8bzzduYULqlJc4BtJOrmsrM-GUbPAblIVsA4CBsknpFInCx8QV5byE3f6PiPDcLcEZ1CBjWk2cO9lsS_GHa8CS3aqiOLYJGH7kqdmPuW34E0YN3Oqjw'}, {
                'domain': '.work.weixin.qq.com', 'expiry': 1601951876, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
                'path': '/', 'secure': False, 'value': 'zh-cn'}]

