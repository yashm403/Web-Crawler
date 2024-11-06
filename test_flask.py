from flask import Flask
print('Starting program...')
try:
    app = Flask(__name__)
    print('Flask app created!')
    
    @app.route('/')
    def hello():
        return 'Hello World!'
    
    if __name__ == '__main__':
        print('Starting Flask server...')
        app.run(port=8080)
except Exception as e:
    print(f'An error occurred: {e}')
input('Press Enter to exit...')
