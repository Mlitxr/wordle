# coding:utf-8
import argparse
from dataloader import *
from fenci import *

parser = argparse.ArgumentParser(description="词云分析")
parser.add_argument('-analyse_mode', type=str, default='all', help="默认输出一张词云图，每篇文章输出一张词云图请输入partly")
parser.add_argument('-article_id', type=str, default='1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20',
                    help="需要分析的文章编号，请用半角逗号分割")
args = parser.parse_args()

article_id=[]
txt=args.article_id.split(',')
for id in txt:
    article_id.append(eval(id))
#print(article_id[1])

#读取文章
print("读取文章")
data=[]
for id in article_id:
    article_path="./article./{}.txt".format(id)
    data.append(load_data(article_path))
#print(len(data))#文章数量

#分词
print("分词")
words=[]
for article in data:
    words_in_article=[]
    #print(article)
    for sentence in article:
        #print(sentence)
        words_in_sentence=back_match(sentence)
        for word in words_in_sentence:
            words_in_article.append(word)
        #print(words_in_article)
        #print(words_in_article)
    words.append(words_in_article)
print(words[0])

#词频统计：TF-IDF
#IDF
word_idf={}
for article in words:
    word_idf={}
    for word in article:
        word_idf[word]=0
for key in word_idf:
    for article in words:
        try:
            a = article.index(key)
            word_idf[key] = word_idf[key] + 1
            continue
        except ValueError:
            continue
print(word_idf)


#输出词云图