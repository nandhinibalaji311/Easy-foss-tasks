from __future__ import absolute_import, print_function
import tweepy

auth = tweepy.OAuthHandler("V0SOwc8C3dGHWzeDHznfXIAg0","zyEQ0xB9YQDinoxyTklTA3q5eRYzvU2sSvoc3yDSlulkGNQDRF")
auth.set_access_token("V0SOwc8C3dGHWzeDHznfXIAg0", "zyEQ0xB9YQDinoxyTklTA3q5eRYzvU2sSvoc3yDSlulkGNQDRF")

api = tweepy.API(auth)

api.update_status(status ="Hello Everyone !")


