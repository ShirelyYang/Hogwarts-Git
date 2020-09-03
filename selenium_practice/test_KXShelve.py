import shelve


class TestShelve:
    def test_shelve(self):
        cookies = [
            {'domain': '.kangxin.com', 'expiry': 1914460422, 'httpOnly': False, 'name': 'b8475611d1985bb7_gr_last_sent_cs1',
             'path': '/', 'secure': False, 'value': '1013'}, {'domain': '.kangxin.com', 'expiry': 1914460422,
                                                              'httpOnly': False, 'name': 'grwng_uid', 'path': '/',
                                                              'secure': False,
                                                              'value': '0ecd2367-afd4-4774-be3f-a30885448593'}, {
                'domain': '.kangxin.com', 'expiry': 1599102222, 'httpOnly': False,
                'name': 'b8475611d1985bb7_gr_last_sent_sid_with_cs1', 'path': '/', 'secure': False,
                'value': '9c96da64-2049-4d55-b545-6d049be97370'}, {'domain': '.service.kangxin.com', 'httpOnly': False,
                                                                   'name': 'Hm_lpvt_80591015967b34bca119790d5ea1ae4a',
                                                                   'path': '/', 'secure': False, 'value': '1599100422'}, {
                'domain': '.kangxin.com', 'expiry': 1599102222, 'httpOnly': False, 'name': 'b8475611d1985bb7_gr_session_id',
                'path': '/', 'secure': False, 'value': '9c96da64-2049-4d55-b545-6d049be97370'}, {'domain': '.kangxin.com',
                                                                                                 'expiry': 1599102222,
                                                                                                 'httpOnly': False,
                                                                                                 'name': 'b8475611d1985bb7_gr_session_id_9c96da64-2049-4d55-b545-6d049be97370',
                                                                                                 'path': '/',
                                                                                                 'secure': False,
                                                                                                 'value': 'true'}, {
                'domain': '.kangxin.com', 'expiry': 1914460422, 'httpOnly': False, 'name': 'b8475611d1985bb7_gr_cs1',
                'path': '/', 'secure': False, 'value': '1013'}, {'domain': '.service.kangxin.com', 'expiry': 1630636422,
                                                                 'httpOnly': False,
                                                                 'name': 'Hm_lvt_80591015967b34bca119790d5ea1ae4a',
                                                                 'path': '/', 'secure': False,
                                                                 'value': '1599100400,1599100422'}, {
                'domain': '.kangxin.com', 'expiry': 1914460422, 'httpOnly': False, 'name': 'gr_user_id', 'path': '/',
                'secure': False, 'value': 'c8917b73-5c9a-4ab4-b849-ae219dce529f'}]
        db = shelve.open("mydb/KXCN_Normal_cookies")
        db['cookie'] = cookies
        db.close()
