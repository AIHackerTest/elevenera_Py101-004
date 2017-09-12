# -*- coding: utf-8 -*-

import requests
import json

def fetchWeather(location):
    result = requests.get(
        'https://api.seniverse.com/v3/weather/now.json',
        params={
            'key': 'x4jusskdpoppmnrc',
            'location': location,
            'language': 'zh-Hans',
            'unit': 'c'
        },
        timeout=15)

    weather_json = json.loads(result.text)

    weather = weather_json['results'][0]['now']['text']
    temperature = weather_json['results'][0]['now']['temperature']
    last_update = weather_json['results'][0]['last_update']

    weather_history = "{0}的天气{1},温度为{2}摄氏度,更新时间为{3}".format(
        location, weather, temperature, last_update)
    return weather_history

if __name__ == "__main__":
    fetchWeather(location)
