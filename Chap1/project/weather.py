import sys
dic = {}

with open('weather_info.txt','r', encoding='utf-8') as f:
    for line in f.readlines():
        key, value =line.strip().split(',')
        dic[key] = value

history = []
while True:
    user_input = input("请输入指令或您要查询的城市名：")

    if user_input in dic.keys():
        weather = dic[user_input]
        weather_history = "{}的天气情况是：{}".format(user_input, weather)
        print(weather_history)
        history.append(weather_history)

    elif user_input == "history":
        print("您的查询历史是：")
        for weather_history in history:
            print(weather_history)

    elif user_input == "help":
        print("""
        直接输入城市名称查询对应天气
        输入'help'，查看如何使用
        输入‘history’，查看历史记录
        输入'quit'，退出程序
        """)

    elif user_input == "quit":
        print("退出程序")
        exit(1)

    else:
        print("未找到对象，请输入'help'查看帮助")
