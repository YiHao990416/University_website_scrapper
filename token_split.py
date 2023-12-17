import argparse
import pandas as pd
import jieba
import os

def avg_tokens(data):
    schools_df = pd.read_json(data, lines=True, encoding = 'utf-8')
    
    total_tokens = 0
    total_length = len(schools_df)

    for i, article in schools_df.iterrows():
        
        article_title = article['title']
        
        article_content = article['text']
        contents = article_title + article_content
        # contents =  article_content
        # Use jieba to tokenize the text
        tokens = jieba.cut(contents)
        # Convert the tokens to a list for further processing
        token_list = list(tokens)
        # print(token_list)
        # print(len(token_list))
        total_tokens += len(token_list)
    print(f'avg token length of the data {args.data} is {total_tokens/total_length}')
    print(f'all tokens num of the data in {args.data} is {total_tokens}')

def avg_tokens_folder(data_path):
    filenames = [f for f in os.listdir(data_path)]
    # print(filenames)
    
    total_tokens = 0
    total_length = 0

    for file in filenames:
        print(f'starting reading {file}')
        read_path = os.path.join(data_path, file)
        schools_df = pd.read_json(read_path, lines=True)
        total_length += len(schools_df)
        for i, article in schools_df.iterrows():
            article_title = article['title']
            article_content = article['text']
            contents = article_title + article_content
            # Use jieba to tokenize the text
            tokens = jieba.cut(contents)
            # Convert the tokens to a list for further processing
            token_list = list(tokens)
            # print(token_list)
            # print(len(token_list))
            total_tokens += len(token_list)
    print(f'avg token length of the data in {data_path} is {total_tokens/total_length}')
    print(f'avg token length of one school in {data_path} is {total_tokens/len(filenames)}')
    print(f'all tokens num of the data in {data_path} is {total_tokens}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data', type=str, default='./data/wiki_all_data.jsonl')
    parser.add_argument('-f', '--folder', type=str, default='./data/official')
    args = parser.parse_args()

    avg_tokens(args.data)
    # avg_tokens_folder(args.folder)