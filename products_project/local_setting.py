# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!787ani5ve)uwrvm+awca7ey72jl!!6&-_4kq)ry2f1o2-sf27'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}