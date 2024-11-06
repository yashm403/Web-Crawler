import requests
import justext
import logging
from urllib.parse import urlparse

class WebCrawler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def crawl(self, url):
        try:
            # Send GET request
            response = requests.get(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            # Extract text using justext
            paragraphs = justext.justext(
                response.content,
                justext.get_stoplist("English")
            )
            
            # Get only the main content
            content = []
            for paragraph in paragraphs:
                if not paragraph.is_boilerplate:
                    content.append(paragraph.text)
            
            return {
                "success": True,
                "content": content,
                "url": url
            }
            
        except Exception as e:
            self.logger.error(f"Error crawling {url}: {str(e)}")
            return {"error": str(e)} 