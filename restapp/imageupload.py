import os
import requests

url = "http://localhost:8000/api/post/"

payload = {'prod_name': 'Tanjiro',
'prod_price': '9999',
'description': 'Fire Haki Blade User ',
'soldat': '1'}


folder_dir = "D:\\restapilearn\\learnrestv2\\restapp\\image_da"
for images in os.listdir(folder_dir):
    if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
        files=[
            ('prod_image',(images,open('D://restapilearn//learnrestv2//restapp//image_da//'+images,'rb'),'image/jpeg'))
            ]
        headers = {'Authorization': 'Bearer 985079682cc31250a1bf3fc1b20e95a9379aae6e'}
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        payload = None

print(response.text)



# import requests

# url = "http://localhost:8000/api/post/"

# payload = {'prod_name': 'rd5tuudr6u',
# 'prod_price': '10',
# 'description': '',
# 'soldat': ''}
# files=[
#   ('prod_image',('nezukodraw.jpg',open('D://restapilearn//learnrestv2//restapp//image_da//nezukodraw.jpg','rb'),'image/jpeg'))
# ]
# headers = {
#   'Authorization': 'Bearer 985079682cc31250a1bf3fc1b20e95a9379aae6e'
# }

# response = requests.request("POST", url, headers=headers, data=payload, files=files)

# print(response.text)







