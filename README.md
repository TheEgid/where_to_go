# where_to_go  
  
**Развернутый пример работы тут - https://abstractdata.ru/**  
  
Проект предназначен для отображения на html-карте интересных мест Москвы.  
  
### Как установить (рекомендуется) на ОС LINUX с помощью Docker и docker-compose  
  
Установка будет развернута из контейнеров с доступом через "обратный прокси" [Nginx](https://nginx.org/ru/).  
Скачиваем файлы. Переходим в папку с файлами. Docker и docker-compose должны быть уже установлены. Выполняем комманду:  
```  
make build  
```  
  
режим "демона" -  
```  
make run  
```  
  
### Как установить без Docker на ОС WINDOWS 10  
  
Скачиваем файлы. Переходим в папку с файлами. Python 3.9 должен быть уже установлен.  
[Отсюда](https://yadi.sk/d/Dbk6LGZhOQFGfg) скачиваем и распаковываем в папку содержимое архива.  
  
  
В этой же папке создаем .env файл. Ваш .env должен содержать строки с константами:  
  
```  
SECRET_KEY  
POSTGRES_USER  
POSTGRES_PASSWORD  
SUPERUSER_LOGIN  
SUPERUSER_PASSWORD  
```  
  
Для корректной установки GDAL (Geospatial Data Abstraction Library  
 — библиотека абстракции гео-пространственных данных) запустить  
   
```  
pip install https://download.lfd.uci.edu/pythonlibs/z4tqcw5k/numpy-1.19.4+vanilla-cp39-cp39-win_amd64.whl  
  
pip install https://download.lfd.uci.edu/pythonlibs/z4tqcw5k/GDAL-3.1.4-cp39-cp39-win_amd64.whl  
```   
Затем используйте pip для установки зависимостей:  
  
```  
pip install -r requirements.txt  
```  
  
Программа требует установленной базы данных Postgis c именем _database1_.  
В PGADMIN создайте и запустите скрипт c переменными из .env файла -  
  
```sql  
CREATE USER <POSTGRES_USER>;  
  
ALTER USER <POSTGRES_USER> WITH ENCRYPTED PASSWORD '<POSTGRES_PASSWORD>';  
  
GRANT ALL PRIVILEGES ON DATABASE database1 TO <POSTGRES_USER>;  
  
ALTER ROLE <POSTGRES_USER> SUPERUSER;  
```   
### Использование  
  
Переходим в каталог с программой. 

Команда миграций  
```  
python manage.py migrate
```  
  
Команда создания суперпользователя  
```  
python manage.py init_admin  
```  
  
Команда запуска сервера -  
```  
python manage.py runserver  
```  
  
Команда заливки объектов (пример) -  
```  
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9A%D1%80%D0%B5%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%BE%20%C2%AB%D0%9B%D1%8E%D0%BC%D1%8C%D0%B5%D1%80-%D0%A5%D0%BE%D0%BB%D0%BB%C2%BB.json  
```  
## Цели проекта  
  
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
