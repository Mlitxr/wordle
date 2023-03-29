# coding:utf-8
import argparse
from dataloader import *
from fenci import *
import math
from wordcloud import WordCloud
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="词云分析")
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
for id in range(20):
    article_path="./article./{}.txt".format(id+1)
    data.append(load_data(article_path))
#print(len(data))#文章数量

#分词
print("分词")
words=[]
for article in data:
    words_in_article=[]
    print(article)
    for sentence in article:
        #print(sentence)
        words_in_sentence=back_match(sentence)
        for word in words_in_sentence:
            words_in_article.append(word)
        #print(words_in_article)
        #print(words_in_article)
    words.append(words_in_article)
#print(words[0])

#词频统计：TF-IDF
tf_per_article=[]
#TF
for article in words:
    word_tf={}
    for word in article:
        word_tf[word]=0
    for word in article:
        word_tf[word]=word_tf[word]+1/len(article)
    tf_per_article.append(word_tf)

#IDF
#print("计算idf")
word_idf={}
for article in words:
    for word in article:
        word_idf[word]=0
#print("initial")
for key in word_idf:
    for article in words:
        try:
            a = article.index(key)
            word_idf[key] = word_idf[key] + 1
            continue
        except ValueError:
            continue
for key in word_idf:
    word_idf[key]=math.log(len(words)/(word_idf[key]+1))

#print(tf_per_article)
#print("idf")
#print(word_idf)

tf_idf=[]
for article in tf_per_article:
    tf_idf_article={}
    for key in article:
        tf_idf_article[key]=article[key] * word_idf[key]
    tf_idf.append(tf_idf_article)


#输出词云图
for id in article_id:
    word_cloud=WordCloud(font_path=r'./font/simhei.ttf',background_color='white',max_font_size=70)
    word_cloud.fit_words(tf_idf[id-1])
    plt.imshow(word_cloud)
    plt.xticks([])
    plt.yticks([])
    plt.savefig('./pic/article_{}'.format(id), dpi=500)
    #plt.show()

#全部的词频
all_word_tf={}
length_all=0
for i in range(len(words)):
    length_all=length_all+len(words[i])
    for word in words[i]:
        all_word_tf[word]=0
for i in range(len(words)):
    for word in words[i]:
        all_word_tf[word]=all_word_tf[word]+1/length_all
#print("all_tf")
#print(all_word_tf)
all_tf_idf={}
for key in all_word_tf:
    all_tf_idf[key] = all_word_tf[key] * word_idf[key]
#print("all_tf_idf")
#print(all_tf_idf)

word_cloud=WordCloud(font_path=r'./font/simhei.ttf',background_color='white',max_font_size=70)
word_cloud.fit_words(all_tf_idf)
plt.imshow(word_cloud)
plt.xticks([])
plt.yticks([])
plt.savefig('./pic/article_all', dpi=500)
plt.show()