*Feedback test*

Установка:

1. Зависиомсти
    ```bash
        pip install -r requirements.txt
  
    ```
    
2. Настройки

    * Создаем файл конфигурации
    ```bash
        cd fogstream && cp example.settings.py settings.py
    ```
    * Указываем парамметры бд и почтового сервера
    
3. Миграции
    ```bash
        pytonh3 manage.py migrate
    ```
    
4. Создаем суперпользователя
    ```bash
        pytonh3 manage.py createsuperuser
    ```
5. Собираем фронтентд
    ```bash
       cd ./fogstreamtest/static && npm i && npm run build
    ```
