from app import get_price

def test_get_price():
    dis_price = get_price('DIS').json
    print(dis_price)

    assert dis_price['price'] > 0
    assert dis_price['name'] == 'The Walt Disney Company'
    assert dis_price['exchange'] == 'NYSE'
    assert dis_price['currency'] == 'USD'
    assert get_price('KSLAFSADF').status_code == 404
    
    print(get_price('KSLAFSADF').status_code)

#test_get_price()
