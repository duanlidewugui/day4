from random import random, Random
#
#
#进入商城，随机挑选商品进行半价，或者有购买该商品后可以进行全场满减
#
#2021/6/9/11/10
class GameShop:
    # 商品的名称和优惠状态，cost是原价，变为dis表示正在打折

    # 初始化列表
    def __init__(self, games):

        self.games = games

    # 单独商品折扣半价
    def discount(self, dis):
        self.dis = dis
        self.games[dis][2] = self.games[dis][2] / 2
        self.games[dis][3] = "dis"
    #将商品的状态变为满减
    def max_minus(self,dis):
        self.games[dis][3] = "可满减"

    # 获得整个列表
    def getGames(self):
        print("\t\t\t\t商城\t\t\t\t\t")
        print("商品序号\t","名称", "\t\t\t价格", "\t\t\t状态")
        for i,name, price, state,amout in self.games:
            print(i,"\t\t",name,"\t\t",price,"\t\t\t",state)
#依次分别是商品序号，商品名称，商品价格，商品折扣状态，商品已被添加到购物车次数
games = [
    [1,"gta5  ", 180, "cost",0],
    [2,"巫师3  ", 90, "cost",0],
    [3,"上古卷轴5", 50, "cost",0],
    [4,"传送门2  ", 30, "cost",0],
    [5,"往日不在", 298, "cost",0],
    [6,"战地风云5", 228, "cost",0],
    [7,"NBA 2K21", 199, "cost",0],
    [8,"极品飞车22", 200, "cost",0],
    [9,"双人成行", 198, "cost",0],
    [10,"无主之地3", 198, "cost",0]
]
#money就是全场的余额
print("请输入您的余额")
money = int(input())
#max_max
max_max = 0
max1 = 0
long_money = money

steam = GameShop(games)
loan = int(random() * 20)
shop_cat=[

]
max = 0
if loan <10:
    print("恭喜您获得了",steam.games[loan][1],"商品半价的优惠")
    steam.discount(loan)
    max = loan
else:
    print("恭喜您获得了购买",steam.games[loan-10][1], "商品即可全场满600减300的优惠")
    steam.max_minus(loan-10)
    max = loan



while True:
    p = long_money-money
    if max>10 and steam.games[max-10][4] != 0:
        if max1 == 0 and p >= 600 :
            money = money + 300
            max1 += 1



    steam.getGames()
    print("请输入")
    print("您目前的余额为",money)
    print("将商品添加至购物车--1\t查看购物车--2\t\t结算--3\t\t离开商场--4")
    key = int(input())
    while key == 1:
        print("请输入您想购买的商品的商品序号")
        id = int(input())
        if id>10 or id<=0:
            print("没有该商品，返回主页面")
            break
        elif money < games[id-1][2]:
            print("余额已不足，请充值，将返回主页面")
            break
        else:
            print("添加购物车成功，将返回主界面")
            if steam.games[id-1][4] == 0:
                steam.games[id - 1][4] += 1
                money = money - steam.games[id-1][2]
                shop_cat.append(
                    [steam.games[id - 1][0], steam.games[id - 1][1],
                     steam.games[id - 1][2], steam.games[id - 1][3],
                     steam.games[id - 1][4]])
                break
            else:
                i = 0
                while steam.games[id-1][0] != shop_cat[i][0]:
                    i += 1
                shop_cat[i][4] += 1
                shop_cat[i][2] = shop_cat[i][2]+steam.games[id - 1][2]
                money = money - steam.games[id - 1][2]
                break


    while key == 2 :
        if len(shop_cat) == 0:
            print("购物车为空，将返回主页面")
            break
        print("\t\t\t\t购物车\t\t\t\t\t")
        print("名称", "\t\t\t价格", "\t\t\t状态","\t\t\t购买数量")
        for i, name, price, state, amout in shop_cat:
            print( name, "\t\t\t", price, "\t\t\t", state,"\t\t\t",amout)
        if max < 10:
            i = 0
            m = 0
            while i < len(shop_cat):
                m = m + shop_cat[i][2]
                i += 1
            max_max = steam.games[max][2]*steam.games[max][4]
            print("目前总金额为",m,"已优惠",max_max)
            max_max = 0

        else:
            i = 0
            m = 0
            while i < len(shop_cat):
                m = m + shop_cat[i][2]
                i += 1

            if steam.games[max-10][4] == 0:
                print("目前总金额为",m)
                print("你还需要购买满减商品才能享受满减")

                break
            elif m < 600:
                print("目前总金额为",m)
                print("您还需要购买",600-m,"元才能享受满减")
                break
            else:
                print("目前总金额为",m-300,"已优惠300元")

                break

        print("输入随意数字退出购物车界面")
        input()
        break

    if key == 3:
        print("您购买了")
        print("名称", "\t\t\t价格", "\t\t\t购买数量")
        for i, name, price, state, amout in shop_cat:
            print(name,"\t\t\t",price,"\t\t\t",amout)

        i = 0
        m = 0
        while i < len(shop_cat):
            m = m + shop_cat[i][2]
            i += 1

        if max < 10:
            max_max = steam.games[max][2] * steam.games[max][4]
        else:
            if max1 == 1 :
                max_max = 300
                m = m -300

        if max_max > 0:
            print("您优惠了",max_max,"元")

        print("您消费了",m,"元")
        m = int(m/10)
        print("您获得了",m,"积分")
        print("您还剩下",money,"元")
        break

    if key == 4:
        print("您放弃了购物，一分钱也没买，默默离开了此地")
        break


























