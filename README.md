#Создаем DB

- `sudo docker volume create simaland_test`  
- `sudo docker run -e POSTGRES_PASSWORD=forum_password -e POSTGRES_USER=forum_user -p 5432:5432 --name postgres --mount source=postgres-data,target=/var/lib/postgresql  -d postgres:11`  
- `sudo docker exec -it simaland_test psql -U admin`  
- `CREATE DATABASE users_db;`  
- `\q`  

#RUN
`python app.py`  

Примеры запросов лежат в `requests_examples.py`. Оттуда же можно их потестировать.
