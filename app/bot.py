import os
import time
import re
from mastodon import Mastodon, StreamListener
from summarizer import summarize
from newspaper import Article

mastodon = Mastodon(
    access_token=os.getenv("MASTODON_ACCESS_TOKEN"),
    api_base_url=os.getenv("MASTODON_API_BASE_URL")
)

URL_REGEX = re.compile(r'https?://\S+')

def extract_url(content):
    match = URL_REGEX.search(content)
    return match.group(0) if match else None

def fetch_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Fel vid hämtning av artikel: {e}")
        return None

class SummarizerBot(StreamListener):
    def on_update(self, status):
        if status['account']['acct'] == mastodon.account_verify_credentials()['acct']:
            return

        url = extract_url(status['content'])
        if not url:
            print("Ingen URL hittades i toot.")
            return

        print(f"Bearbetar toot med länk: {url}")

        article_text = fetch_article_text(url)
        if not article_text:
            print("Kunde inte hämta artikeltext.")
            return

        summary = summarize(article_text)
        reply_text = f"\ud83d\udccc Sammanfattning:\n{summary}"

        try:
            mastodon.status_post(
                status=reply_text,
                in_reply_to_id=status['id'],
                visibility=status['visibility']
            )
            print("Svar postat.")
        except Exception as e:
            print(f"Fel vid postning av svar: {e}")

if __name__ == "__main__":
    print("Startar bot...")
    while True:
        try:
            mastodon.stream_user(SummarizerBot())
        except Exception as e:
            print(f"Fel i streamen: {e}")
            time.sleep(10)
