import requests

list = []
with open('paths.txt', "r", encoding='utf-8') as file:
    for line in file:
       list.append(line.strip())

def subdom(url,listOfSubs):
    for sub in listOfSubs:
        response = requests.get(f"{url}/{sub}")
        with open('log.txt','a') as file:
            file.writelines(f"{response.status_code}, {sub}\n")
            print(response.status_code, sub)
    print("Tarkistus suoritettu!")


url = 'https://www.vuokraussastamala.fi'

subdom(url,list)
