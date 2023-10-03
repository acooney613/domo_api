import logging
from pydomo import Domo

API_HOST = "api.domo.com"

class domo_connector:
    def __init__(self):
        domo = self.init_domo_client(CLIENT_ID, CLIENT_SECRET)

    def init_domo_client(self, client_id, client_secret, **kwargs):
        handler = logging.Streamhandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name) - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logging.getLogger().addHandler(handler)

        return Domo(client_id, client_secret, logger_name = 'foo', log_level = logging.INFO, api_host = API_HOST, **kwargs)
        