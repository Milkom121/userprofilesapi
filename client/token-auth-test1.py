#IN QUESTO FILE VENOGONO SIMULATE LE AZIONI DI UN CLIENT COME UN BROWSER O UNA APP




#questo snippet fornisce una lista di profili se il token di auntenticazione è corretto
import requests

def client():

    token_h = 'Token 810f5fec97d83fd322259add7010cce8b510ffc8'  #il _h non ho capito a cosa serva ma 'Token ' (compreso lo spazio) sembra sia fondamentale

    headers = {'Authorization': token_h}

    response = requests.get('http://192.168.178.74:8000/api/profiles',
                            headers = headers)

    print('Status code:', response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__':
    client()









# #client per l'ottenimento di un token di autenticazione partendo da username e password
# import requests
#
# def client():
#     credentials = {'username' : 'mario' , 'password' : 'mario'}
#
#     response = requests.post('http://192.168.178.74:8000/api/rest-auth/login/',
#                              data = credentials)
#
#     print('Status code:', response.status_code)
#
#     response_data = response.json()
#     print(response_data)
#
# if __name__ == '__main__':
#     client()
