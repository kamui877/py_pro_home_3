import bs4
import requests


keywords = ['phyton', 'разработчик', 'бекенд']
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://habr.com'
res = requests.get(f'{url}/ru/all/', headers=headers).text
page_soup = bs4.BeautifulSoup(res, 'html.parser')
containers = page_soup.find_all('article')
parser = int(input("Введите команду(1-из превью, 2-из текста статьи): "))
help_list = []
for container in containers:
    title = container.find('h2').find('span').text
    link = f'{url + container.find("h2").find("a")["href"]}'
    data = container.find('time')['title']
    if parser == 1:
        preview = container.find(class_="tm-article-body tm-article-snippet__lead").find_all('p')
        for keyword in keywords:
            for val in preview:
                if keyword in val.text:
                    help_list.append(f'{title}\n{link}\n{data}\n')
    elif parser == 2:
        resp = requests.get(link, headers=headers).text
        page_soup_1 = bs4.BeautifulSoup(resp, 'html.parser')
        article_body = page_soup_1.find(id="post-content-body").find_all('p')
        for keyword in keywords:
            for val in article_body:
                if keyword in val.text:
                    help_list.append(f'{title}\n{link}\n{data}')
for val in list(set(help_list)):
    print(f'\n{val}')
