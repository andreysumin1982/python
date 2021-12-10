#--
import requests
import csv
from bs4 import BeautifulSoup
#--
pathSaveFile = '/home/asumin/Документы/Программирование_Python/test_files/auto.csv'
#--
#URL = 'https://auto.ru/sankt-peterburg/cars/luaz/all/'
#URL = 'https://auto.ru/sankt-peterburg/cars/great_wall/all/'
#URL = 'https://auto.ru/sankt-peterburg/cars/ssang_yong/all/'
#URL = 'https://auto.ru/sankt-peterburg/cars/haval/all/'
#URL = 'https://auto.ru/sankt-peterburg/cars/mazda/all/'
#URL = 'https://auto.ru/sankt-peterburg/cars/citroen/all/'
#URL = 'https://auto.ru/sankt-peterburg/cars/ferrari/all/'
#URL = 'https://auto.ru/sankt-peterburg/cars/subaru/all/'
#URL = 'https://auto.ru/sankt-peterburg/cars/cadillac/all/'
#URL = 'https://auto.ru/sankt-peterburg/cars/gaz/all/'
#URL = 'https://auto.ru/sankt-peterburg/cars/geely/all/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
            'accept':'*/*'
           }
#--
def get_html(url, params=None):
    r = requests.get(url,  headers=HEADERS, params=params)
    r.encoding = 'utf-8'
    return r
#--
def get_page_count(html): # Ф-ция находит кол-во страниц для парсинга
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='ListingPagination-module__page') # находим общий контент, гда лежат все страницы
    count = []  # список для страниц
    #--
    for item in items: # бежим по тому, что нашел
        count.append((item.find('span', class_='Button__content').find('span', class_='Button__text').get_text()))
    if len(count) != 0 :
        return int(count[-1])
    else:
        return 1
#--
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="ListingItem-module__main")
    arr = []
    for item in items:
        arr.append({'name_auto': item.find('h3', class_='ListingItemTitle-module__container ListingItem-module__title').find('a', class_='Link ListingItemTitle-module__link').get_text('target'),
                    'summary': item.find('div', class_='ListingItemTechSummaryDesktop__cell').get_text(),
                    'price': item.find('div', class_='ListingItemPrice-module__content').get_text('span'),
                    'kmage': item.find('div', class_='ListingItem-module__kmAge').get_text(),
                    'year' : item.find('div', class_='ListingItem-module__year').get_text(),
                    'link': item.find('a', class_='Link ListingItemTitle-module__link').get('href')
                    })
    return arr # Возвращает список {внутри словарь распарсеных контeнтов}
#--
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        page_count = get_page_count(html.text)
        cars = []
        for page in range(1, page_count + 1):
            print(f'Парсинг страницы {page} из {page_count}')
            html = get_html(URL, params={'page':page})
            cars.extend(get_content(html.text))
        return cars
    else:
        return 'Ошибка соединения. Сервер не доступен.'
#--
def save_file(): # Записываем в файл формата .CSV
    with open(pathSaveFile, 'w', newline='') as write_file:
        writer = csv.writer(write_file, delimiter = ';') # Отделяем стобцы (;)
        writer.writerow(['Марка','Характеристики','Цена','Пробег','Год','Ссылка']) # Шапка
        count = 0
        for pars in parser():
            writer.writerow([pars["name_auto"], pars["summary"],
                            pars['price'], pars["kmage"],
                            pars["year"], pars["link"]])
            count +=1
        print(f'OK. Получено машин: {count}.')
#--
save_file() # Вызываем ф-цию
#--