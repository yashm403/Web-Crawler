from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print("Request received!")
    return "Hello, World!"

if __name__ == '__main__':
    print("Starting test server...")
    app.run(port=9000) 