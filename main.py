from bs4 import BeautifulSoup
import requests
import lxml # Used in BS4 on line 13

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
}
url = input("Type a Reddit Url (Ex. https://www.reddit.com/r/birds/): ")
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')


for item in soup.select('.Post'):
    try:
        print('----------------------------------------')
        print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text())
        print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
        print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text())
        print(item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href'])	
    except Exception as e:
        #raise e
        print('')
