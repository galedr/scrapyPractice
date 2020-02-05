from flask import Flask

app = Flask(__name__)


@app.route('/', method='GET')
def index():
    return "<p style='color: red;'>Hello World!</p>"


@app.route('tmpFeature', method='POST')
def tmpFeature():
    # todo 試爬取計算連續三股票投報率(現金股利/除息前購買價)大於5%的股票
    return
