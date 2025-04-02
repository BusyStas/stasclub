from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/depin')
def depin():
    return render_template('depin.html')

@app.route('/exchanges')
def exchanges():
    return render_template('exchanges.html')

@app.route('/wallets')
def wallets():
    return render_template('wallets.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
