DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_hstore_usage',                      # Or path to database file if using sqlite3.
        'USER': 'zambe',                      # Not used with sqlite3.
        'PASSWORD': '1q2w3e',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = 'q7oirft+1u02cp&amp;9wbchjpuu&amp;ysjuagh(=i*f4j2g6gz)9$q#*'
