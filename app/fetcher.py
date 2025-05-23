from newspaper import Article

def fetch_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Fel vid hämtning av artikel: {e}")
        return None