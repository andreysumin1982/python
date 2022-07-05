import random
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from datetime import datetime
# ---------------------------------------- #

# Определяем класс и его атрибуты
class testClass:
    def __init__(self,id, title, content, dateTime = None):
        self.id = id
        self.title = title
        self.content = content
        self.dateTime = dateTime or datetime.today().strftime("%d %b. %Y %H:%M")

# Определяем класс для сериализации (атрибуты должны соответствовать как в testClass)
class testSerializer(serializers.Serializer):
    # Задаем тип атрибутов
    id = serializers.CharField()
    title = serializers.CharField()
    content = serializers.CharField()
    dateTime = serializers.DateTimeField()

# Ф-ция для преобразования объектов класса testClass в JSON
def encodeTest():
    # Экземпляр класса testClass
    modeltest = testClass(id=f"{random.randrange(10)}", title='test_title', content=f"{[j*100 for j in range(100)]}")
    # Передаем наш экземпляр в класс сериализации
    modeltest_sr = testSerializer(modeltest)
    # Преобразуем полученный объект в JSON
    json = JSONRenderer().render(modeltest_sr.data)
    return json
#------------------------------------------------------------#

# Еще один тестовый класс
class testclass2:
    def __init__(self, id, data, time=None):
        self.id = id
        self.data = data
        self.time = time or datetime.today().strftime("%H:%M")
#
class testSerializer2(serializers.Serializer):
    id = serializers.CharField()
    time = serializers.DateTimeField()
    data = serializers.CharField()
#
def encodeTest2(id, data):
    modeldata = testclass2(id, data)
    modeltest_sr = testSerializer2(modeldata)
    json = JSONRenderer().render(modeltest_sr.data)
    return json
#
