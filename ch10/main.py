import requests
from bs4 import BeautifulSoup
import glob
import re

def main():
    log_files = glob.glob('*.log')

    for log in log_files:
        with open(log) as f:
            for line in f:
                result = re.findall("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)
                print(result)



def main_download_logs():
    url ="https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = [link for link in soup.find_all('a') if link['href'][0] != '?']

    for link in links:
        # https://logs.eolem.com/apache_logs_01.log
        file = f"{url}{link['href']}"
        response = requests.get(file)
        
        local_file = link['href']
        with open(local_file,'w') as f:
            print(response.text,file=f)


if __name__ == "__main__":
    main()