# Пульт охраны банка 

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код верстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников нашего банка.

## Как установить

Python 3 уже должен быть установлен

1. Клонируйте репозиторий с github - для этого выполните в консоли:  
git clone https://github.com/oZerro/django-orm2.git

2. Создайте виртуальное окружение.  
Для создания виртуального окружения:

- Перейдите в директорию своего проекта.  
```
cd django-orm2
```

- Выполните:
```
python -m venv venv
```

3. Активируйте виртуальное окружение.  
Для активации виртуального окружения выполните:

- Для Windows:  
```
venv\Scripts\activate.bat
```

- Для Linux и MacOS:  
```
source venv/bin/activate
```

4. Установите зависимости:  
```
pip install -r requirements.txt
```

5. Создайте файл **.env** в вашей деректории проекта.

- Для Windows:  
```
type nul > .env
```

- Для Linux и MacOS:  
```
touch файл.txt
```

6. Откройте файл **.env** в любом текстовом редакторе и добавьте ваши переменные окружения - сохраните.
Содержание будет такое:
```
DB_HOST='ваш DB_HOST'
DB_PORT='ваш DB_PORT'
DB_NAME='ваш DB_NAME'
DB_USER='ваш DB_USER'
DB_PASSWORD='ваш DB_PASSWORD'
SECRET_KEY='ваш SECRET_KEY'

DEBUG=False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

## Как запустить

Для запуска - из дериктории проекта выполните команду в консоли:
```
python manage.py runserver
```