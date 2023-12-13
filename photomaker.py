import requests
def photo(link):
    img_data = requests.get(link).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)
    print(img_data)

photo("https://d7-invdn-com.investing.com/company_logo/eb173ed14992dd403ddb9d3ea9bbf477.jpg")