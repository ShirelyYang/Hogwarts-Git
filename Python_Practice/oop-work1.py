# encoding=utf-8
class Cat:
    def __init__(self):
        self.color = "白色"
        self.name = "喵喵"
        self.weight = 5
        self.shape = "胖"
        print(f"小猫的名字叫{self.name}，颜色是{self.color}，体重为{self.weight}kg，体型{self.shape}")
        pass

    def run(self):
        print("小猫跑得非常快")
        pass

    def eat(self, food):
        print(f"小猫爱吃{food}")
        pass

    def hobby(self):
        print("小猫喜欢睡觉~")
        pass

    def disgusting(self):
        print("小猫讨厌游泳")
        pass
    pass


cat = Cat()
cat.run()
cat.eat("小鱼干")
cat.hobby()
cat.hobby()
cat.disgusting()
