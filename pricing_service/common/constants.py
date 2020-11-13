import re


URL = "https://www.johnlewis.com/samsung-galaxy-tab-a-2019-10-1-inch-tablet-android-32gb-2gb-ram-wi-fi/black/p4127095"
TAG_NAME = "p"
QUERY = {"class": "price price--large"}
PRICE_PATTERN = re.compile(r"([0-9],?[0-9]*\.[0-9][0-9])")
