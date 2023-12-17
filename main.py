import requests
from bs4 import BeautifulSoup
import re
import lxml
import json
from lxml.html.clean import Cleaner
from scrapper import link_scrapper, text_scrapper, extract_soup


def main(json_file, depth, min_len, min_text):
    
    # Read the university information from jsonlines files
    uni_list=[]
    with open(json_file, encoding = 'utf8') as f:
        for jsonObj in f:
            uni_dict = json.loads(jsonObj)
            uni_list.append(uni_dict)

    # Parse the university information to the scrapper
    for uni in uni_list:
        URL = uni["網址"]
        university_name= uni['學校名稱']
        university_name_eng = uni['abbrev']
        URL_suffix = f'{university_name_eng}.edu'
        URL_suffix2 = f'{university_name_eng}.org'
        URL_suffix3 = f'{university_name_eng}.net'
        
        # Create empty set to store the links and soups extracted
        link_list = []
        soup_list = []
        extracted_text = []

        for i in range(depth):
            link_list.append(set())
            soup_list.append(set())

        # Start scrapping
        for i in range(depth):
            try:
                
                if i == 0:
                    print(f'start scrapping{university_name}')
                    r = requests.get(URL)
                    soup = BeautifulSoup(r.content,'lxml')

                    link_list[i].update(link_scrapper(soup,URL_suffix, URL_suffix2, URL_suffix3))
                    print(f'link extraction layer: {i} done')
                    new_soup, new_extracted_text = extract_soup(link_list[i], university_name, min_len)
                    soup_list[i].update(new_soup)
                    extracted_text.extend(new_extracted_text)
                    print(f'soup extraction layer: {i} done')

                else:
                    for soup in soup_list[i-1]:

                        link_list[i].update(link_scrapper(soup, URL_suffix, URL_suffix2))

                    # Compare the links in layer i with layer i-1 to remove repeated links
                    for j in range(i):
                        link_list[i] = link_list[i]-link_list[i-j-1]

                    print(f'link extraction layer: {i} done')
                    new_soup, new_extracted_text = extract_soup(link_list[i], university_name, min_len)
                    soup_list[i].update(new_soup)
                    extracted_text.extend(new_extracted_text)
                    print(f'soup extraction layer: {i} done')
            
            # Output error to checkpoint/error.txt file    
            except:
                f = open(f"checkpoint/error.txt",'a',encoding= 'utf8')
                f.write(f'{university_name}\n')
                f.close()
                pass
        # print extracted text to txt file
        # Write all the extracted link to checkpoint/university_name_links.txt
        f = open(f"checkpoint/{university_name}_link.txt",'w',encoding= 'utf8')
        f2 = open(f"output/output_{university_name}.txt",'w',encoding='utf8')
        for line in extracted_text:
            f2.write(line)

        for link_set in link_list:
            for link in link_set:
                f.write(f'{link}\n')
        f.close
        f2.close
        print(f'Create university link done')

                

if __name__ == '__main__':
    main('input/all_uni.jsonl',3,50,20)

