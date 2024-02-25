## Установка
### Шаблон описания файла .env
 - USER=<логин paloalto>
 - PASSWORD=<пароль paloalto>
 - DB_USER=<логин clickhouse>
 - DB_PASSWORD=<логин clickhouse>
 - TOKEN=<токен бота Телеграм>
### Инструкции для развертывания и запуска приложения
для Linux-систем все команды необходимо выполнять от имени администратора1
- Склонировать репозиторий
```bash
git clone git@github.com:PaulSssar/Paloalto.git
```
- Выполнить вход на удаленный сервер
- Установить docker на сервер:
```bash
apt install docker.io 
```
- Установить docker-compose на сервер:
```bash
apt install docker-compose
```

- Скопировать файл docker-compose.yml:
```bash
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
```
- Создать .env файл по предлагаемому выше шаблону.

- собрать и запустить контейнеры на сервере:
```bash
docker-compose up -d --build
```

## API сайта:
- http://192.168.100.7:8000/categories/ - Получение количества сайтов по категориям
- http://192.168.100.7:8000/search/?domain=<domain> - Поиск по домену и получение всей информации по результату поиска
## Автор
Павел Сарыгин 

