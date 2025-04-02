from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/depin')
def depin():
    return render_template('depin.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
