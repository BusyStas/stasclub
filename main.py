from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analogy')
def analogy():
    return render_template('analogy.html')

@app.route('/depin')
def depin():
    return render_template('depin.html')

@app.route('/exchanges')
def exchanges():
    return render_template('exchanges.html')

@app.route('/wallets')
def wallets():
    return render_template('wallets.html')

@app.route('/fidelity')
def fidelity():
    return render_template('fidelity.html')

@app.route('/presale')
def presale():
    return render_template('presale.html')

@app.route('/hard_wallets')
def hard_wallets():
    return render_template('hard_wallets.html')

@app.route('/mining')
def mining():
    return render_template('mining.html')

@app.route('/gold')
def gold():
    return render_template('gold.html')

@app.route('/tokens')
def tokens():
    return render_template('tokens.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
