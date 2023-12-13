import requests

def photo(link):
    img_data = requests.get(link).content
    test_value = requests.get(link).status_code
    with open('image_name1.jpg', 'wb') as handler:
        handler.write(img_data)
    return test_value