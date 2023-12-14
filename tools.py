import json
import jsonlines
import re
import os

def txt_to_array(document,university_name):
    text = []
    extracted_text=[]
    f = open(document,'r',encoding='utf8')
    index = 0

    for line in enumerate(f):

        if line[1] != '\n':
            text.append(line[1])

    for line in text:
        if f"關於{university_name}的資訊:" in line:
            extracted_text.append([line])
            index += 1
        # elif line !="\n" and line !="":
        else:
            extracted_text[index-1].append(line)

    print(extracted_text)
    with jsonlines.open(f"output_json/output_{university_name}.jsonl",'w') as w:
        for line in extracted_text:
            # if "".join(line[1:]) !="" or re.search('[a-zA-Z]', "".join(line[1:])) == False:
            if "".join(line[1:]) !="":
                w.write({"title":line[0].replace('\n',''),"text":(''.join(line[1:])).replace('\n','')})

    return extracted_text


for filename in os.listdir("./output"):       
    match =re.search(r"_(.*?)\.", filename)
    print(match)
    txt_to_array(f'output/{filename}',match.group(1))