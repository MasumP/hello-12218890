from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello 12218890!"  # Replace with your student number

if __name__ == '__main__':
    app.run()
