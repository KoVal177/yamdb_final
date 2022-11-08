# Разворачивание проекта ["Yamdb"](https://github.com/KoVal177/api_yamdb/) на Docker и отдельном сервере.

### Состояние
![event parameter](https://github.com/github/docs/actions/workflows/main.yml/badge.svg?event=push)

### Функционал
При добавлении изменений в репозиторий выполняются следующие действия:   
1. Производится тестирование и проверка синтаксиса;
2. Компилируется новый образ проекта и выкладывается на [Docker Hub](https://hub.docker.com/);
3. На удаленном сервере в [Yandex Cloud](https://cloud.yandex.ru/) разворачивается проект с учетом внесенных изменений;
4. Загружается статика, производятся миграции и добавление в базу тестовых данных.
5. Администратору через telegram отправляется уведомление, если все действия были произведены успешно.
  
Работающий сервер находится по адресу [vkyatube.sytes.net/](http://vkyatube.sytes.net/)  
Результат выполнения запроса "Выдать названия всех произведений" - [vkyatube.sytes.net/api/v1/titles/](http://vkyatube.sytes.net/api/v1/titles/)
