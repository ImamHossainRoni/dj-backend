## Dj-Backend:
It's simple REST API backend for Product catalog image scrapping and image resizing etc. :)

## How to run (1)
1. After activating virtualenv then run

 ```pip install -r requirements.txt```

2. If requirements are fully satisfied then run

```python manage.py makemigrations```

3. and then run 

```python manage.py migrate```

4. If migrate done then run 

```python manage.py runserver```



## How to scrap image  (2)
 To scrap image just run a custom management command:

``python manage.py scrape``

## How to access API urls (3)
 To retrieve specific image info then-

```http://127.0.0.1:8000/api/v1/catalog/images/retrieve/{ID}/```

To get all scrapped images info from original source url name then-

```http://127.0.0.1:8000/api/v1/catalog/images/retrieve-by-source-url/{SOURCE_URL_NAME}/```

To get special sized of images then pass optional query params to url named `size`. like-

```http://127.0.0.1:8000/api/v1/catalog/images/retrieve/755b31ce-643b-427a-9f5b-0870a5fe9f43/?size=small```

and,

```http://127.0.0.1:8000/api/v1/catalog/images/retrieve-by-source-url/applegadgetsbd.com/?size=small```

*** If anything goes under your find, please feel free to knock me: imamhossainroni95@gmail.com


# Thank you!