# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from weather_fetch import fetchWeather

app = Flask(__name__)
history = []

@app.route('/', methods=['GET', 'POST'])
def Index():
    return render_template('home.html')

@app.route('/location', methods=['GET', 'POST'])
def weather_web():
    while True:
        if request.args.get('btn') == 'help':
            return render_template('help.html')
        elif request.args.get('btn') == 'history':
            return render_template('history.html', history=history)
        elif request.args.get('btn') == 'search':
            location = request.args.get('city')
            try:
                weather_history = fetchWeather(location)
                history.append(weather_history)
                return render_template('result.html',
                    weather_history=weather_history)
            except KeyError:
                return render_template('error.html')

if __name__ == "__main__":
    app.run(debug = True)
