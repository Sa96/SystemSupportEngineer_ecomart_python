import config

app = config.app
app.testing = True
connexion_app = config.connex_app
connexion_app.add_api('swagger.yml', strict_validation=True)