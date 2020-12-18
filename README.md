# where_to_go

развернутый сайт тут - https://abstractdata.ru/


### Как установить (рекомендуется) на ОС LINUX с помощью Docker и docker-compose

Установка будет развернута из контейнеров с доступом через "обратный прокси" [Nginx](https://nginx.org/ru/) 
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
В этой же папке создаем .env файл. Ваш .env должен содержать строки с константами:

;;;;;;;;

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

Программа требует установленной базы данных PostgreSQL 13.1 c именем _database1_.
В PGADMIN создайте и запустите скрипт c переменными из .env файла -
```
CREATE USER <POSTGRES_USER>;
ALTER USER <POSTGRES_USER> WITH ENCRYPTED PASSWORD '<POSTGRES_PASSWORD>';
GRANT ALL PRIVILEGES ON DATABASE <POSTGRES_DB> TO <POSTGRES_USER>;
ALTER ROLE <POSTGRES_USER> SUPERUSER;
```

### Использование

Переходим в каталог с программой
Команда -

```
python main.py runserver
```
