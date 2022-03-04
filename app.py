from flask import Flask, render_template, request, url_for
import pandas as pd
from datetime import datetime
from PIL import Image
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    years = request.form.get('years')
    months = request.form.get('months')
    days = request.form.get('days')

    df = pd.read_csv(f'data/{years}.csv')
    days = int(days)
    months = int(months)
    meisu = df.iloc[days - 1, months]
    meisu = meisu.replace('-', '')

    current = datetime.now()
    current_year = current.year
    current_year = int(current_year)

    years = int(years)
    if (years % 2) == 0:
        even_odd = '金'
    else:
        even_odd = '銀'
    age = current_year - years
    global yourType

    # 壮年期（命数　3を採用）
    if age >= 60:
        if meisu[0:2] < '11':
            print(f'あなたは{even_odd}の羅針盤です。')
            yourType = f'{even_odd}の羅針盤{meisu[0:2]}'

        elif meisu[0:2] < '21':
            print(f'あなたは{even_odd}のインディアン型です。')
            yourType = f'{even_odd}のインディアン{meisu[0:2]}'

        elif meisu[0:2] < '31':
            print(f'あなたは{even_odd}の鳳凰型です。')
            yourType = f'{even_odd}の鳳凰{meisu[0:2]}'

        elif meisu[0:2] < '41':
            print(f'あなたは{even_odd}の時計型です。')
            yourType = f'{even_odd}の時計{meisu[0:2]}'

        elif meisu[0:2] < '51':
            print(f'あなたは{even_odd}のカメレオン型です。')
            yourType = f'{even_odd}のカメレオン{meisu[0:2]}'

        elif meisu[0:2] < '61':
            print(f'あなたは{even_odd}のイルカ型です。')
            yourType = f'{even_odd}のイルカ{meisu[0:2]}'
        else:
            print('その他')

    # 青年期（命数　２を採用）
    elif age >= 30:
        if meisu[2:4] < '11':
            print(f'あなたは{even_odd}の羅針盤です。')
            yourType = f'{even_odd}の羅針盤{meisu[2:4]}'

        elif meisu[2:4] < '21':
            print(f'あなたは{even_odd}のインディアン型です。')
            yourType = f'{even_odd}のインディアン{meisu[2:4]}'

        elif meisu[2:4] < '31':
            print(f'あなたは{even_odd}の鳳凰型です。')
            yourType = f'{even_odd}の鳳凰{meisu[2:4]}'

        elif meisu[2:4] < '41':
            print(f'あなたは{even_odd}の時計型です。')
            yourType = f'{even_odd}の時計{meisu[2:4]}'

        elif meisu[2:4] < '51':
            print(f'あなたは{even_odd}のカメレオン型です。')
            yourType = f'{even_odd}のカメレオン{meisu[2:4]}'

        elif meisu[2:4] < '61':
            print(f'あなたは{even_odd}のイルカ型です。')
            yourType = f'{even_odd}のイルカ{meisu[2:4]}'
        else:
            print('その他')

     # 幼年期（命数　1を採用）
    elif age >= 0:
        if meisu[4:6] < '11':
            print(f'あなたは{even_odd}の羅針盤です。')
            yourType = f'{even_odd}の羅針盤{meisu[4:6]}'

        elif meisu[4:6] < '21':
            print(f'あなたは{even_odd}のインディアン型です。')
            yourType = f'{even_odd}のインディアン{meisu[4:6]}'

        elif meisu[4:6] < '31':
            print(f'あなたは{even_odd}の鳳凰型です。')
            yourType = f'{even_odd}の鳳凰{meisu[4:6]}'

        elif meisu[4:6] < '41':
            print(f'あなたは{even_odd}の時計型です。')
            yourType = f'{even_odd}の時計{meisu[4:6]}'

        elif meisu[4:6] < '51':
            print(f'あなたは{even_odd}のカメレオン型です。')
            yourType = f'{even_odd}のカメレオン{meisu[4:6]}'

        elif meisu[4:6] < '61':
            print(f'あなたは{even_odd}のイルカ型です。')
            yourType = f'{even_odd}のイルカ{meisu[4:6]}'
        else:
            print('その他')
    else:
        pass

    #20022年の運勢
    if yourType[0:-2] == '金の羅針盤':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    elif yourType[0:-2] == '銀の羅針盤':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    elif yourType[0:-2] == '金のインディアン':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    elif yourType[0:-2] == '銀のインディアン':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    elif yourType[0:-2] == '金の鳳凰':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    elif yourType[0:-2] == '銀の鳳凰':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    elif yourType[0:-2] == '金の時計':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    elif yourType[0:-2] == '銀の時計':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    elif yourType[0:-2] == '金のカメレオン':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    elif yourType[0:-2] == '銀のカメレオン':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    elif yourType[0:-2] == '金のイルカ':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    elif yourType[0:-2] == '銀のイルカ':
        img_path = f'static/img/{yourType[0:-2]}.png'
        with open(f'2022/{yourType[0:-2]}.txt', 'r', encoding='utf-8') as f:
            unsei2022 = f.read()
    else:
        pass

    return render_template('result.html',
                           age=age,
                           yourType=yourType[0:-2],
                           picture = img_path,
                           unsei2022 = unsei2022)

if __name__ == '__main__':
    app.run(debug=True)