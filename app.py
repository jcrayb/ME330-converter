from flask import Flask, render_template, request, send_from_directory, abort

from txt_to_csv_lab4 import convert_txt_to_csv_4
from txt_to_csv_lab1 import convert_txt_to_csv_1

import requests
from urllib.parse import urlparse
import io
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/healthcheck')
def healthcheck():
    return {'status':'healthy'}

@app.route('/convert', defaults={'type':''})
@app.route('/convert/<type_>', methods=['POST'])
def route_convert(type_):
    if not type_:
        return abort(400)
    data = request.get_json()
    lab = request.args['lab']
    print(lab)
    if type_ == 'url':
        csv_string = ''
        urls = data['urls']
        for url in urls:
            site = urlparse(url).hostname
            if site != 'mtil.illinois.edu':
                return abort(400)
            request_obj = requests.get(url)
            encoding = request_obj.apparent_encoding
            text = str(request_obj.content, encoding="utf-8").replace(str('\r'), str('\n'))
            #print(text)
            if lab=='lab1':
                csv = convert_txt_to_csv_1(text)

            if lab=='lab4':
                csv = convert_txt_to_csv_4(text)

            if csv_string:
                csv = csv.replace(csv.split('\n')[0], '')
            csv_string += csv
    elif type_ == 'text':
        text = data['text']
        csv_string = convert_txt_to_csv(text)
    else:
        return abort(400)
    df = pd.read_csv(io.StringIO(csv_string))
    if 'Unnamed: 0' in df.columns:
        df = df.drop('Unnamed: 0', axis=1)
    df.to_csv('temp/temp.csv')
    return send_from_directory('temp', 'temp.csv')


if __name__ == '__main__':
    if not os.path.exists('./static/config'):
        os.mkdir('./static/config')
    app.run(debug=True, host="0.0.0.0", port='8080')