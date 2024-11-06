from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Web Crawler</title>
            <style>
                body { font-family: Arial; margin: 40px; }
                .form-group { margin: 20px 0; }
                input[type=url] { width: 300px; padding: 5px; }
                button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
            </style>
        </head>
        <body>
            <h1>Web Crawler</h1>
            <form action='/crawl' method='get'>
                <div class='form-group'>
                    <label>Enter URL to crawl:</label><br>
                    <input type='url' name='url' required placeholder='https://example.com'>
                </div>
                <button type='submit'>Crawl Website</button>
            </form>
        </body>
    </html>
    '''

@app.route('/crawl')
def crawl():
    url = request.args.get('url')
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text content
        texts = soup.stripped_strings
        content = '\\n'.join(texts)
        
        return f'''
        <html>
            <head>
                <title>Crawler Results</title>
                <style>
                    body {{ font-family: Arial; margin: 40px; }}
                    .result {{ background: #f5f5f5; padding: 20px; margin: 20px 0; }}
                    .back {{ padding: 10px 20px; background: #007bff; color: white; text-decoration: none; }}
                </style>
            </head>
            <body>
                <h1>Crawling Results</h1>
                <h2>URL: {url}</h2>
                <div class='result'>
                    <pre>{content}</pre>
                </div>
                <a href='/' class='back'>Back to Home</a>
            </body>
        </html>
        '''
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    print('Web Crawler starting at http://localhost:8080')
    app.run(port=8080, debug=True)
