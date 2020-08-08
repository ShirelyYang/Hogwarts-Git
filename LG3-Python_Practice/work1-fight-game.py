# encoding=utf-8
import random
"""
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

def fight():
    # 血量
    my_hp = 1000
    your_hp = 1000
    # 攻击力
    my_power = 200
    your_power = 190
    # 加血
    blood = 100
    while True:
        # 随机整数，左右都是闭区间
        i = random.randint(1, 4)
        if i == 1:
            my_hp -= your_power
            pass
        elif i == 2:
            your_hp -= my_power
            pass
        elif i == 3:
            my_hp += blood
            pass
        else:
            your_hp += blood
        if my_hp <= 0 or your_hp <= 0:
            break
    if my_hp > your_hp:
        print("我赢了！")
        pass
    else:
        print("你赢了！")
        pass


fight()
