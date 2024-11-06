from flask import Flask, render_template, request, jsonify
from .crawler import WebCrawler

def create_app():
    app = Flask(__name__)
    crawler = WebCrawler()
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/crawl', methods=['POST'])
    def crawl():
        url = request.form.get('url')
        if not url:
            return jsonify({"error": "URL is required"})
        
        result = crawler.crawl(url)
        return render_template('result.html', result=result)
    
    return app 