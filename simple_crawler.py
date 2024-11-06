from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Simple Web Crawler</h1>
    <form action="/test" method="get">
        <button type="submit">Test Crawl</button>
    </form>
    '''

@app.route('/test')
def test_crawl():
    try:
        # Try to crawl a simple website
        url = "http://example.com"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').text
        return f"Successfully crawled {url}<br>Title: {title}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    print("="*50)
    print("Starting crawler on: http://localhost:8080")
    print("Press Ctrl+C to quit")
    print("="*50)
    app.run(host='0.0.0.0', port=8080, debug=True) 