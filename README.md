# Аттестационная работа
_Это - бекэнд часть платформы сети, продающей электронику_
### Установка
> * Скопируйте репозиторий
> * Установите все зависимости
> * Заполните файл .env
> * Примените миграции (_python manage.py migrate_)
> * Загрузите данные для БД (_python manage.py loaddata data.json_)
> * Запустите проект (_python manage.py runserver_)
### Реализованные модели
> * Seller - модель для магазинов
> * Contact - модель контактов магазинов
> * Product - модель товаров, которые продаются магазинами
> * User - пользователь
### ТЗ
* DRF 
  * Запрет на обновление поля credit (задолженность) через API
  * Фильтр магазинов по странам
* /admin
  * url для поставщиков
  * Фильтр по городам
  * admin action - обнуление задолженности перед поставщиком
### URLS
* Seller
  * http://localhost:8000/shop/list/ - список (магазины + контакты)
  * http://localhost:8000/shop/create/ - создание
  * http://localhost:8000/shop/update/<int:pk>/ - обновление
  * http://localhost:8000/shop/retrieve/<int:pk>/ - detail
  * http://localhost:8000/shop/destroy/<int:pk>/ - удаление
* Contact
  * http://localhost:8000/shop/create/contact/ - создание
  * http://localhost:8000/shop/update/contact/<int:pk>/ - обновление
* Product
  * http://localhost:8000/shop/create/product/ - создание
  * http://localhost:8000/shop/update/product/<int:pk>/ - обновление
  * http://localhost:8000/shop/destroy/product/<int:pk>/ - удаление
  * http://localhost:8000/shop/list/product/ - список (магазины + продукты)
* User
  * http://localhost:8000/users/token/ - создание токенов
  * http://localhost:8000/users/refresh/ - обновление токенов