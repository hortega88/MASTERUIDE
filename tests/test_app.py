from app import get_price


def test_get_price():
    dis_price = get_price('DIS').json
    print(dis_price)

    assert dis_price['Precio'] > 0
    assert dis_price['Nombre'] == 'The Walt Disney Company'
    assert dis_price['Intercambio'] == 'NYSE'
    assert dis_price['Moneda'] == 'USD'

    assert get_price('KSLAFSADF').status_code == 404


test_get_price()
