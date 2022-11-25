import json
import time
import requests
import logging
import QuotePic
from mastodon import Mastodon

# Set up Mastodon
mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://botsin.space'
)

# For adding logs in application
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

# Get Quote
logger.info("getting quote")
def get_quote():
    url = "https://api.quotable.io/random"

    try:
        response = requests.get(url)
    except:
        logger.info("Error while calling API...")
    res = json.loads(response.text)
    print(res)
    return res['content'] + " - " + res['author']


logger.info("making image")
toot = get_quote()
QuotePic.get_wallpaper(toot)
logger.info("sleeping")
time.sleep(3)
media = mastodon.media_post("created_image.png")
logger.info("tooting quote")

mastodon.status_post("Random Quote of the day!", media_ids=media)
