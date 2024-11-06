from flask import Flask
import logging

# Set up logging to see what's happening
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    logger.info("Request received!")
    return "Hello, World!"

if __name__ == '__main__':
    logger.info("Starting server...")
    try:
        # Try different host bindings
        app.run(debug=True, port=9000)
        # If above doesn't work, try these alternatives:
        # app.run(host='127.0.0.1', port=9000, debug=True)
        # app.run(host='0.0.0.0', port=9000, debug=True)
    except Exception as e:
        logger.error(f"Error: {e}") 