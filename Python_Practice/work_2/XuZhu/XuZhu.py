# encoding=utf-8
from TongLao import TongLao


class XuZhu(TongLao.TongLao):
    def __init__(self):
        super().__init__(1000, 200)

    def read(self):
        print("罪过罪过")
        pass
    pass


tonglao = TongLao.TongLao(2000, 300)
tonglao.see_people("无崖子")
tonglao.fight_zms(1800, 200)
xuzhu = XuZhu()
xuzhu.read()
