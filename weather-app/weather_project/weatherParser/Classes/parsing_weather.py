import requests
from datetime import datetime
#---------------------------
class parsing:
    def __init__(self):
        pass
    def getData(self):
        # Key
        apiKey = '0a5f324681efd3b00cf37496755d39ca'
        URL = f'https://api.openweathermap.org/data/2.5/weather?id=498817&units=metric&appid={apiKey}&lang=ru'
        # id-города
        citys = {'Санкт-Петербург': 498817,
                 'Москва': 524894,
                 'Металлострой': 527361,
                 'Кировск': 548391,
                 'Лондон': 3489741,
                 }
        # --
        response = requests.get(URL)  # передаем параметры в http-запрос
        outputResponse = {'status': response.status_code, 'headers': response.headers, 'output': response.json()}
        # --
        iconImage = f'http://openweathermap.org/img/wn/{outputResponse["output"]["weather"][0]["icon"]}@2x.png'
        # dateNow = datetime.strftime("%d %B %H.%M")
        context = {
            'date': 'Сегодня ' + datetime.today().strftime("%d %b. %Y %H:%M"),
            'name': outputResponse['output']['name'],  # город
            'icon': iconImage,  # иконка
            'description': outputResponse['output']['weather'][0]['description'].capitalize(),
            # состояние погоды (снег, дождь...)
            'temp': f'{outputResponse["output"]["main"]["temp"]} \u2103',  # температура
            'feels_like': f'{outputResponse["output"]["main"]["feels_like"]} \u2103',  # ощущение как
            'wind': outputResponse['output']['wind']['speed'],  # ветер
            'humidity': outputResponse['output']['main']['humidity'],  # влажность
        }
        return context  # Вызвращает словарь
        # return JsonResponse(context) # Вызвращает json

    # ---