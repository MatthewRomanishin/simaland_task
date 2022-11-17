# Клонируем репозиторий
- `git clone https://github.com/MatthewRomanishin/simaland_task.git`  
- `pip install -r requirements.txt`  
# Создаем DB

- `sudo docker volume create simaland_test`  
- `sudo docker run -e POSTGRES_PASSWORD=admin -e POSTGRES_USER=admin -p 5432:5432 --name simaland_test --mount source=simaland_test,target=/var/lib/postgresql  -d postgres:11`    
- `sudo docker exec -it simaland_test psql -U admin`  
- `CREATE DATABASE users_db;`  
- `\q`  

# RUN
`python app.py`  

Примеры запросов лежат в `requests_examples.py`. Оттуда же можно их потестировать.
