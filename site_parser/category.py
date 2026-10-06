from .base import BaseParser
import bs4
import settings


class CategoryParser(BaseParser):
    def get_categories(self) -> list[dict[str, str]]:
        soup = self.get_soup()

        # {'class': 'nav_row'}
        nav_row = soup.find('div', class_='nav_row').find('ul')

        items = nav_row.find_all('li')[:-3]
        result = []
        for item in items:
            title = item.get_text(strip=True)
            href = item.find('a').get('href')
            result.append({
                'title': title,
                'href': f'{settings.SITE_URL}{href}'
            })
        return result

    def get_category_articles(self, category_url: str) -> bs4.ResultSet[bs4.Tag]:
        soup = self.get_soup(category_url)
        wrapper = soup.find('div', id='content-block')
        return wrapper.find_all('div', class_='sh-news')




