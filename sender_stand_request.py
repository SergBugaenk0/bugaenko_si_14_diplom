import requests
import configuration
import data

def post_new_client_ORDER(): # создает новый заказ, берет данные из configuration и data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_client_ORDER,  # подставляем полный url
                         json=data.ORDER)


def get_ORDER_on_track(track): # возвращает данные заказа по его треку
    params = {
        't': track
    }
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_on_TRACK, params=params)




