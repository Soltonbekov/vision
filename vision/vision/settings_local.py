DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vision_db',
        'USER': 'root',
        'PASSWORD': '123',
    }
}