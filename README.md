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
```

## Автор
Павел Сарыгин 

