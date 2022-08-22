# ShortenerExample
url shortener rest service

🌍 *[English](README.md)



## How to run the application

1. Clone the application with `https://github.com/GamzeUnal/ShortenerExample.git`

2. Download the postman configuration file (optional).
3. To build from source you need Python (3.7).
4. There are number of dependencies which need to be imported before running the application. Please get the dependenices through the following commands -

    ```shell
        pip install django
        pip install djangorestframework
        pip install django-cors-headers
    ```
5. To run the application, please use the following command -

    ```shell
        python manage.py migrate
        python manage.py migrate --run-syncdb
        python manage.py runserver
    ```
> Note: By default the port number its being run on is **8000**.

## Endpoints Description

### Get Shortener By Id

```JSON
    URL - *http://localhost:8000/api/shortener/Id*
    Method - GET
```

### Create Shortener

```JSON
    URL - *http://localhost:8000/api/shortener/*
    Method - POST
    Body - (content-type = application/json)
    {	"original_url" : "https://www.google.com.tr/"
	}
```


### Redirect Original Url

```JSON
    URL - *http://localhost:8000/<str:url>*
    Method - GET
```

