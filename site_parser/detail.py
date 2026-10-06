import settings
from .base import BaseParser
import bs4

class ArticleParser(BaseParser):
    def get_articles_data(self, category_articles: bs4.ResultSet[bs4.Tag]):
        result = []
        for i in category_articles:
            title = i.find('h2').get_text()
            href = i.find('h2').find('a').get('href')

            detail_data = self.get_article_detail(href)

            img = i.find('img').get('data-src')

            description = i.find('div', class_='sh-text').next.get_text(strip=True)
            side_date = i.find('div', class_='side-date').find_all('span')
            date = side_date[0].get_text()
            if len(side_date) == 2:
                comments = side_date[-1].get_text()
            else:
                comments = '0'
            result.append({
                'title': title,
                'href': href,
                'img': img,
                'description': description,
                'date': date,
                'comments': comments,
                **detail_data
            })
        return result

    def get_article_detail(self, article_url: str):
        soup = self.get_soup(article_url)

        description = soup.find('div', {'itemprop': 'articleBody'}).get_text()
        author_name = soup.find('h2', class_='author-name').get_text()
        author_bio = soup.find('div', class_='author-bio').get_text()

        return {
            'full_description': description,
            'author_name': author_name,
            'author_bio': author_bio
        }
