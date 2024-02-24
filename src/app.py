import config
from app_initializer import initialize_data

connexion_app = config.connex_app
connexion_app.add_api("swagger.yml", strict_validation=True)

if __name__ == '__main__':
    initialize_data()
    connexion_app.run()


