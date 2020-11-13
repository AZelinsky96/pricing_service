import re

from bs4 import BeautifulSoup
from pricing_service.common.constants import PRICE_PATTERN


CONTENT_PARSERS = {
    "html": "html.parser"
}


class SoupParser:

    def __init__(self, content: str, parser_type: str) -> None:
        self.content = content
        self.parser_type = CONTENT_PARSERS.get(parser_type)
        self.parser = BeautifulSoup(self.content, self.parser_type) if self.parser_type is not None else None
    

class PriceParser(SoupParser):

    def get_price(self, tag: str, query: str) -> str:
        element = self.parser.find(tag, query) if self.parser is not None else None
        return self.format_price(element.text) if element is not None else None
    
    def format_price(self, price: str) -> float:
        return float(PRICE_PATTERN.search(price.strip()).group(1).replace(",", ""))
        