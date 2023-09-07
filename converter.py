from flask import Flask, render_template, request, send_from_directory
from txt_to_csv import convert_txt_to_csv 
import pandas as pd

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('app.html')

@app.route('/convert', methods=['POST'])
def route_convert():
    data = request.get_json()
    text = data['text']
    csv = convert_txt_to_csv(text)
    return send_from_directory('temp', 'temp.csv')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port='8080')