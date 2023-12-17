import os
import re
import json


uni_list=[]
uni_name = []
with open('./input/all_uni.jsonl', encoding = 'utf8') as f:
    for jsonObj in f:
        uni_dict = json.loads(jsonObj)
        uni_list.append(uni_dict)

for uni in uni_list:
    uni_name.append(uni['學校名稱'])



for filename in os.listdir("./output"):       
    match =re.search(r"_(.*?)\.", filename)
    print(match.group(1))
    for i,element in enumerate(uni_name):
        if match.group(1) == element:
            uni_name.pop(i)

print(uni_name)

    