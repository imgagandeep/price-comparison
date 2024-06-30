# price-comparison

Price Comparison is web based API which is built in Django Rest Framework. To compare a price with different retailer sell a same produt with different prices.

```
Result of get API endpoint is "/api/products/":
{
    "success": true,
    "message": "Products are retrieved successfully.",
    "data": {
        "Product A": [
            {
                "retailer": "store3",
                "price": 20.0
            },
            {
                "retailer": "store2",
                "price": 15.0
            },
            {
                "retailer": "store1",
                "price": 10.0
            }
        ],
        "Product B": [
            {
                "retailer": "store2",
                "price": 15.0
            },
            {
                "retailer": "store3",
                "price": 10.0
            }
        ]
    }
}
```

<h3>🛠️ Project Setup:</h3>

-   Install Python from here -> https://www.python.org/

### Clone the repository

```
git clone https://github.com/imgagandeep/price-comparison
```

### Install virualenv

```
    ├── pip install virtualenv
```

### Create virtualenv

```
    ├── virtualenv <your-env>
```

### Activate virtualenv (Windows)

```
    ├── path\<your-env>\Scripts\activate
```

### Activate virtualenv (MAC)

```
    ├── source path\<your-env>\bin\activate
```

### Activate virtualenv (Linux)

```
    ├── path\<your-env>\bin\activate
```

### After activate virtualenv Install Libraries

```
    ├── pip install -r requirements.txt
```

### Configure secret_key, debug, logging_level and allowed_host in .env file

```
    ├── SECRET_KEY = "<SECRET_KEY>"
    ├── DEBUG = TRUE
    ├── LOGGING_LEVEL = "INFO"
    ├── ALLOWED_HOST = *
```

# Database Choice

I used a PostgreSQl database which is robust, scalable and reliable. I would be avoid the unexpected errors while using a same project in Production. That's why I used same database configuration in development mode.

### Configure database in .env file

```
    ├── ENGINE = "django.db.backends.postgresql"
    ├── DB_HOST = "localhost"
    ├── DB_PORT = "PORT"
    ├── DB_NAME = "DATABASE-NAME"
    ├── DB_USER = "DATABASE-USER-NAME"
    ├── DB_PASSWORD = "DATABASE-USER-PASSWORD"
```

### Run Migrations

```
    ├── python manage.py makemigrations
    ├── python manage.py migrate
```

### Run server

```
    ├── python manage.py runserver
```
