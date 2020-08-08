# encoding=utf-8
class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power
        pass

    def see_people(self, name):
        """

        :param name: 传入人名
        :return:
        """
        if name == "无崖子":
            print("师弟！！！！")
            pass
        elif name == "李秋水":
            print("呸，贱人")
            pass
        elif name == "丁春秋":
            print("叛徒！我杀了你")
            pass
        pass

    def fight_zms(self, enemy_hp, enemy_power):
        self.power *= 10
        self.hp /= 2
        while True:
            self.hp -= enemy_power
            enemy_hp -= self.power
            if self.hp <= 0:
                print("敌人获胜")
                break
            elif enemy_hp <= 0:
                print("天山童姥获胜")
                break
            pass
        pass
    pass

