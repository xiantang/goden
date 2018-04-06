import requests
from lxml import etree
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
def get_content():
    for i in range(1,101):

        # content=requests.get('https://www.jinfuzi.com/simu/list_d1_w1_p{}.html'.format(i),headers=headers).text
        print(len(content))

get_content()