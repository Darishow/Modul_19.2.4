import requests
import json

# GET запрос
response_get = requests.get('https://petstore.swagger.io/v2/store/inventory')
print('GET:', response_get.json())

# POST запрос
data_post = {
    'id': 1,
    'petId': 1,
    'quantity': 1,
    'shipDate': '2023-06-09T10:00:00Z',
    'status': 'placed',
    'complete': True
}
headers_post = {'Content-Type': 'application/json'}
response_post = requests.post('https://petstore.swagger.io/v2/store/order', data=json.dumps(data_post), headers=headers_post)
print('POST:', response_post.json())

# DELETE запрос
order_id = 1  # Идентификатор заказа, который вы хотите удалить
response_delete = requests.delete(f'https://petstore.swagger.io/v2/store/order/{order_id}')
print('DELETE:', response_delete.json())

# PUT запрос
data_put = {
    'id': 1,
    'petId': 1,
    'quantity': 2,
    'shipDate': '2023-06-10T10:00:00Z',
    'status': 'approved',
    'complete': True
}
headers_put = {'Content-Type': 'application/json'}
response_put = requests.put('https://petstore.swagger.io/v2/store/order', data=json.dumps(data_put), headers=headers_put)
print('PUT:', response_put.json())



