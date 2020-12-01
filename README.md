# code7-api

To run it, install docker and docker-compose and run:
```
docker-compose up
```
to run tests:
```
docker exec -it code7 sh

python manage.py test
```

#### 1. To create an author, make a post request with the body:

```
{
"name": "Author Name"
}
```

to http://localhost:8000/api/v1/authors/

#### 2. To create news, make a post request with the body:
```
{
"title": "News Title",
"description": "News Description",
"author": "author_id (can be found in http://localhost:8000/api/v1/authors/)",
}
```
to http://localhost:8000/api/v1/news/


#### 3. To search news, make a guet request with the body:

to http://localhost:8000/api/v1/news/


#### 4. To search for the content add the get parameter q with the desired text:

http://localhost:8000/api/v1/news/?q=title+or+description+or+author+name


#### 5. To update news, make a put request with the body:
```
{
"title": "News Title",
"description": "News Description",
"author": "author_id (can be found in http://localhost:8000/api/v1/authors/)",
}
```
to http://localhost:8000/api/v1/news/<news_id>/

 
#### 6. To delete news, make a delete request to to http://localhost:8000/api/v1/news/<news_id>/
