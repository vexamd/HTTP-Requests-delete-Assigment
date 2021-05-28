import requests
r = requests.delete("http://127.0.0.1:8080/", params={'name': 'john'})
print("Request method: DELETE, \
    Response status_code: {}, Response data: {}".format(r.status_code, r.text))
r = requests.get("http://127.0.0.1:8080/", params={"name":'john'})
print("Request method: GET, \
    Response status_code: {}, Response data: {}".format(r.status_code, r.text))