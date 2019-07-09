from mastodon import Mastodon

mastodon = Mastodon(
    access_token='',
    api_base_url='https://mastodon.social'
)
def tooth(message):
    mastodon.toot(message)

tooth("Hello World")

