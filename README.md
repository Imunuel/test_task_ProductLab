# Для запуска проекта:
необходимо создать postgreSQL базу данных:
* 'NAME': "test_task",
* 'USER': 'test_task_user',
* 'PASSWORD': 'dbpass',

Далее в самом приложении выполнить команды:
```commandline
pip install -r requirements.tst
```
```commandline
python manage.py migrate
```
```commandline
python manage.py runserver
```
Для приложения подтянут __swagger__

Для корректной работы API необходима ссылка товара на ozon, 
так как работа с wildberries не была корректной

### Прохоренко Роман Владимирович