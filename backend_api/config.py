class SystemConfig:

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'testuser',
        'password': 'hoge',
        'host': '127.0.0.1:3306',
        'db_name': 'world'
    })

    SECOND_SAMPLE_DATABASE = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'testuser',
        'password': 'hoge',
        'host': '127.0.0.1:3306',
        'db_name': 'sakila'
    })
    SQLALCHEMY_BINDS = {"second_sample_db": SECOND_SAMPLE_DATABASE}


Config = SystemConfig
