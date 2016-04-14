import leancloud


def register_leancloud(app):
    leancloud.init(app_id='',
                   app_key='',
                   master_key='')
    return app
