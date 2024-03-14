# Сергей Бугаенко, 14 когорта - финальный проект. Инженер по тестированию плюс.
import sender_stand_request
# Функция для позитивных проверок
def positive_assert():
    # создаем новый заказ и запоминаем его трек номер
    response = sender_stand_request.post_new_client_ORDER()
    track = response.json()['track']
    # при создании заказа проверку на ошибку не делаем т.к. по условию не требуется (в ручную проверил - работает)
    # получаем параметры заказа по его треку
    response = sender_stand_request.get_ORDER_on_track(track)
    order = response.json()['order']
    # принты можно убрать - не принципиально), но с ними наглядней выполнение
    print(response.status_code)
    print(order)
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200
# Тесты:
# Создаем заказ, получаем его номер, получаем информацию о номере, функции используем из sender_stand_request
def test_create_order_and_get_track_test_1():
    positive_assert()

