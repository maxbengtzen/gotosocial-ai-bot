import os
from mastodon import Mastodon

def get_mastodon_client():
    return Mastodon(
        access_token=os.getenv("MASTODON_ACCESS_TOKEN"),
        api_base_url=os.getenv("MASTODON_API_BASE_URL")
    )