import requests

return longitude and latitude
#使用baidu API
def geocodeB(address):
    base = url = "http://api.map.baidu.com/geocoder?address=" + address + "&output=json&key=f247cdb592eb43ebac6ccd27f796e2d2"
    response = requests.get(base)
    answer = response.json()
    return answer['result']['location']['lng'],answer['result']['location']['lat']
geocodeB("杭州")
