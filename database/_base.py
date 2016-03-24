import leancloud


def register_leancloud(app):
    leancloud.init(app_id='Xmh3GP4wHdgz4jPVpaW6jQYM-gzGzoHsz',
                   app_key='xBmSvfdpXxBkgDhjJuqqBIWW',
                   master_key='j8VdYDUkWaKGTirQQrKsFeUC')
    return app
