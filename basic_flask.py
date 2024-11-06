from flask import Flask
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    logger.info("Homepage requested!")
    return "<h1>Hello! This is a test page.</h1>"

if __name__ == '__main__':
    logger.info("Starting Flask server...")
    print("="*50)
    print("Server starting on: http://localhost:8080")
    print("Press Ctrl+C to quit")
    print("="*50)
    app.run(host='0.0.0.0', port=8080, debug=True) 