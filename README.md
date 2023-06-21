# crime-zone
A social crime sharing site including three types of user such as general user,law enforcement user and admin.General user can share any crime ,give star for specific crime post,comment  for specific crime post ,reply for specific comment.User will make it issue by giving star,comment and reply.Law enforcement user can  take any action if the issue if formed and he can suspend user and that suspended user get an email notification.

>Requirements

Django==2.1.2
django-appconf==1.0.2
django-crequest==2018.5.11
djangorestframework==3.9.0
Pillow==5.3.0
pytz==2018.6
six==1.11.0


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
