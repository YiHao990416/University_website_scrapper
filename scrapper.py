import requests
from bs4 import BeautifulSoup
import re
import lxml
from lxml.html.clean import Cleaner
from datetime import datetime

# [Cleaner to clean all the javascript function] 
cleaner = Cleaner()
cleaner.javascript = True # This is True because we want to activate the javascript filter
cleaner.style = True  

# [Extract the soup from the university webpage link and print all the text into a output/uni_name.txt file] 

def extract_soup(link_list, university_name, min_len):
    soup_list = set()
    extracted_string = []

    for link in link_list:
        try: 

            # enter the webpage and extract the soup
            r = requests.get(link)
            soup = BeautifulSoup(r.content,'lxml')
            soup_list.add(soup)
            
            # remove the unwanted style and function 
            soup.prettify

            # open a new file as "append" so that text from multiple layer of webpage can write to the same file
            # f = open(f"output/output_{university_name}.txt",'a',encoding='utf8')
            # f.write(f'\n關於{university_name}的資訊: {soup.title.string}\n\n')
            extracted_string.append(f'\n關於{university_name}的資訊: {soup.title.string}\n\n')

            # Add "|" at the beginning and the end of the text so that we can remove unwanted style and function 
            visible_text = soup.getText('|',strip = True)
            cleaner.clean_html(visible_text)

            # Split all the text and store them in to a list so that we can preprocess the extracted text
            html_split = visible_text.split(sep="|")

            # text preprocessing
            for string in html_split:
                if re.search(u'[\u4e00-\u9fff]', string) and ("<" in string) == False and (">" in string) == False and ("{" in string) == False and ("}" in string) == False:
                    string =string.replace(' ',"")
                    # Removal of email address
                    string = re.sub("([\w\.\-\_]+@[\w\.\-\_]+)", "", string)
                    #Removal of phone number
                    string = re.sub(r'\b(?:\+\d{1,2}\s?)?(?:\(\d{1,4}\))?[ -]?\d{1,5}[ -]?\d{1,5}[ -]?\d{1,9}\b', "", string)
                    # only write sentence with length greater than min_len to the .txt file
                    if len(string)>=min_len:
                        # f.write(f'{string}\n')
                        extracted_string.append(f'{string}\n')

            # f.close()
        except:
            pass
    # Return the soup
    return soup_list, extracted_string

# [link scrapper is used to extract all the university webpage link from the extracted soup ]
def link_scrapper(soup, URL_suffix, URL_suffix2):
    website = []

    # Retrieve all the link from the soup
    for link in soup.find_all("a"):
        website.append(str(link.get('href')))
    
    link_list = set()
    current_link =''

    # Process the website to filter unwanted website
    for i in range(len(website)):

        # Join the main link to the sublink
        link=''
        if re.match(r'^((http|https)://)',website[i]): 
            current_link = website[i]
            link = (website[i])
        
        if re.match(r'^/',website[i]):
            link = current_link + website[i] 

        # Make sure only related link is extracted example: link with suffix = ncku.edu, link without the keywords "portal" or "login"
        if re.match(r'^((http|https)://)',link) and re.match(r'^(?:(?!portal).)*$',link) and re.match(r'^(?:(?!login).)*$',link) and ((URL_suffix or URL_suffix2) in link):
            link_list.add(link)

    return link_list


# [text_scrapper is used when we only need to extract text from a single webpage]
def text_scrapper(link_list, university_name, university_name_eng,min_len, min_text):
    # text = set()
    for link in link_list:
        try:
            URL = link
            r = requests.get(URL)

            soup = BeautifulSoup(r.content,'html5lib')
            soup.prettify
            f = open(f"output/output_{university_name}.txt",'a',encoding='utf8')
            f.write(f'\n關於{university_name}的資訊: {soup.title.string}\n\n')
            visible_text = soup.getText('|',strip = True)
            cleaner.clean_html(visible_text)
            html_split = visible_text.split(sep="|")

        
            for string in html_split:
                if re.search(u'[\u4e00-\u9fff]', string) and ("<" in string) == False and (">" in string) == False and ("{" in string) == False and ("}" in string) == False:
                    string = re.sub("([\w\.\-\_]+@[\w\.\-\_]+)", "", string)
                    string = re.sub(r'\b(?:\+\d{1,2}\s?)?(?:\(\d{1,4}\))?[ -]?\d{1,5}[ -]?\d{1,5}[ -]?\d{1,9}\b', "", string)
                    # text.append(string)
                    if len(string)>=min_len:
                        f.write(f'{string}\n')

            f.close()

        except:
            pass
    
    





    
