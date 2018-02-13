# Examples of REST requests using requests
import requests
restEndpoint="https://simplebackend.apps.de1.bosch-iot-cloud.com/sensorMeasurement"
headers={'Accept':'application/json'}

print("----GET----")
# GET
responseGet=requests.get(url=restEndpoint,headers=headers)
print(responseGet.status_code)
print(responseGet.text)
# To get the response in a json:
# json=responseGet.json()
# To access the property temperature of the second object:
# json[1]['temperature']
# To get the headers of the response: 
# responseGet.headers


print("----POST----")
# POST 
newMeasurement={"dateTime": "13.02.2018 13:28","humidity": 70,"sensorId": 1,"temperature": 43}
responsePost=requests.post(url=restEndpoint,headers=headers,json=newMeasurement)
print(responsePost.status_code)
print(responsePost.text)

print("----PUT-----")
# PUT 
# PUT returns 201 for success 
editedMeasurement={"dateTime": "13.02.2018 13:31","measurementId":3, "humidity": 100,"sensorId": 1,"temperature": 100}
responsePUT=requests.put(url=restEndpoint,headers=headers,json=editedMeasurement)
print(responsePUT.status_code)
print(responsePUT.text)

print("----DELETE-----")
# DELETE 
restEndpoint="https://simplebackend.apps.de1.bosch-iot-cloud.com/sensorMeasurement"
measurementIdDelete='3'
responseDELETE=requests.delete(url=restEndpoint+"/"+measurementIdDelete,headers=headers)
print(responseDELETE.status_code)
print(responseDELETE.text)

print("----GET-----")
# GET 
restEndpoint="https://simplebackend.apps.de1.bosch-iot-cloud.com/sensorMeasurement"
measurementIdGet='3'
responseGET=requests.get(url=restEndpoint+"/"+measurementIdGet,headers=headers)
print(responseGET.status_code)
print(responseGET.text)

