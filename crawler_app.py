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
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container mt-5">
                <h1>Web Crawler</h1>
                <form action="/crawl" method="post">
                    <div class="mb-3">
                        <label for="url" class="form-label">Enter URL to crawl:</label>
                        <input type="url" class="form-control" id="url" name="url" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Crawl</button>
                </form>
            </div>
        </body>
    </html>
    '''

@app.route('/crawl', methods=['POST'])
def crawl():
    url = request.form.get('url')
    try:
        # Send GET request to the URL
        response = requests.get(url)
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text content
        text_content = soup.get_text()
        
        # Return results
        return f'''
        <html>
            <head>
                <title>Crawler Results</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            </head>
            <body>
                <div class="container mt-5">
                    <h1>Crawling Results</h1>
                    <h2>URL: {url}</h2>
                    <div class="mt-4 p-3 bg-light">
                        <pre>{text_content}</pre>
                    </div>
                    <a href="/" class="btn btn-primary mt-3">Back</a>
                </div>
            </body>
        </html>
        '''
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    print("Starting Web Crawler on http://localhost:8080")
    app.run(host='0.0.0.0', port=8080, debug=True) 