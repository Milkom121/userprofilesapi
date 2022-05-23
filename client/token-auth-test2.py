#IN QUESTO FILE VENOGONO SIMULATE LE AZIONI DI UN CLIENT COME UN BROWSER O UNA APP




#questo snippet fornisce una lista di profili se il token di auntenticazione è corretto
import requests

def client():

    token_h = 'Token 3123be8f2313b21a0c4da51d99fd254a9ddd8b42'  #il _h non ho capito a cosa serva ma 'Token ' (compreso lo spazio) sembra sia fondamentale

    # data ={
    #     'username': 'testrest',
    #     'email': 'test@rest.com',
    #     'password1': 'cambiami12',
    #     'password2': 'cambiami12'
    # }
    #
    # response = requests.post('http://192.168.178.74:8000/api/rest-auth/registration/',
    #                          data = data)

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
