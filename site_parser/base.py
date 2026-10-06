import settings

import requests
import bs4


class BaseParser:
    def get_soup(self, url: str = settings.SITE_URL) -> bs4.BeautifulSoup:
        """отправка запроса на ссылку, получение html контента"""
        response = requests.get(url)
        response.raise_for_status()
        return bs4.BeautifulSoup(response.text, 'html.parser')

# Single Responsibility Principe