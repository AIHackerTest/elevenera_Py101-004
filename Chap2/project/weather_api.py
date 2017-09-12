import requests
import sys
import json

def fetchWeather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key': 'x4jusskdpoppmnrc',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=15)
    return result.text


if __name__ == '__main__':
    history = []
    print("欢迎主人，请输入您想要查询的城市名，天气数据来源于心知天气")

    while True:
        location = input("请输入指令或您要查询的城市名：")

        if location == "history":
            print("您的查询历史是：")
            for weather_history in history:
                print(weather_history)

        elif location == "help":
            print("""
            直接输入城市名称查询对应天气
            输入'help'，查看如何使用
            输入‘history’，查看历史记录
            输入'quit'，退出程序
            """)

        elif location == "quit":
            print("退出程序")
            exit(1)

        else:
            result = fetchWeather(location)
            weather_json = json.loads(result)

            if 'status' in weather_json:
                print(weather_json['status'])
                print("数据请求失败，请输入'help'查看帮助")

            else:
                weather = weather_json['results'][0]['now']['text']
                temperature = weather_json['results'][0]['now']['temperature']
                last_update = weather_json['results'][0]['last_update']

                weather_history = "{0}的天气{1},温度为{2}摄氏度".format(location, weather, temperature)
                print(weather_history)
                print("更新时间：%s" % last_update)
                history.append(weather_history)
