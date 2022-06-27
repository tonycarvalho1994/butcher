from decouple import config


class AppSettings:
    APP_NAME = 'Butcher API'
    APP_DESCRIPTION = 'API responsible for providing data stored in the MOSAIQ \
    system, of the radiotherapy treatment of Oncoradium Aracaju patients.'
    APP_CONTACT = {
        'name': 'TI Oncoradium',
        'email': 'ti@oncoradium.com.br',
    }
    APP_HOST = 'localhost'
    APP_PORT = 8000

    # Database Settings
    DB_HOST = config('DB_HOST', '0.0.0.0')
    DB_PORT = config('DB_PORT', 5432)
    DB_NAME = config('DB_NAME', 'my_database')
    DB_USER = config('DB_USER', 'db_user')
    DB_PASS = config('DB_PASS', 'db_pass')
