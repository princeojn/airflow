import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = '09a76ecbc73ce28cea17a41dab639264'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'qJxrs8cIfjDRkEfFbLwzI8xbJJRZ-RESp_7cZqkQgZPmdB6zO03XTifkC00KKcleAAABjurIIyqUJG13ldIf8A'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)