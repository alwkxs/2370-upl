# создать венв
# активировать его
# добавить python
# скачать библиотеки requests bs4
# pip install requests bs4

import json
from site_parser.category import CategoryParser
from site_parser.detail import ArticleParser


def main():
    final_data = {}

    category_parser = CategoryParser()
    article_parser = ArticleParser()

    categories = category_parser.get_categories()
    for category in categories:
        category_name = category.get('title')
        category_url = category.get('href')

        category_articles = category_parser.get_category_articles(category_url)
        articles_data = article_parser.get_articles_data(category_articles)
        final_data[category_name] = articles_data

    with open('upl.json', mode='w', encoding='utf-8') as file:
        json.dump(final_data, file, ensure_ascii=False, indent=4)


main()