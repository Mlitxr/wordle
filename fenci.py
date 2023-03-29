# coding:utf-8

#需要删除的符号字符串
punctuation = '？！的，。、；：“”‘’【】{}、|/*-+~@#￥%……&*（）——-=~`·《》<>;:"?!1234567890.,ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#字典读取
datas = []
with open("dict.txt","r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        datas.append(line)
dict=[]
i=0
for data in datas:
    words = data.split(" ")
    dict.append(words[0])

def remove(txt):#去除标点符号
    punctuation_str = punctuation
    #print(punctuation_str)
    for i in punctuation_str:
        txt = txt.replace(i, '')
    return txt


def  back_match(text): #分词
    word_list = []
    m = max(len(word) for word in dict)
    #print("m:{}".format(m))
    txt = remove(text)
    pi = len(txt) -1
    count = 0
    while pi >=0 :
        n = len(txt[0:pi+1])
        if n < m:
            m=n
        for index in range(m-1,-1,-1):
            count=count+1
            #print(txt[pi - index:pi + 1])
            #print(count)
            if (txt[pi-index:pi+1] in dict):
                word_list.append(txt[pi-index:pi+1])
                pi = pi - index-1
                count=0
                break
            if count>14:
                #print('>15')
                pi = pi - index - 1
                count=0
                continue

    #print('/'.join(word_list[::-1]))
    return word_list[::-1]

if __name__ == '__main__':
    text = "中国高度重视科技创新，积极融入全球创新网络，严格保护知识产权，走出了一条有中国特色的知识产权发展道路。从2012年到2021年，全社会研发投入从1.03万亿元增长到2.79万亿元，强度从1.91%增长到2.44%。中国全社会研究与试验发展人员全时当量超过500万人年，连续多年居世界第一位。全国知识产权保护社会满意度从63.69分提升到80.61分，创历史新高。"
    #text = "总台CGTN记者：近日，布基纳法索发生今年以来第二次政变，政变军人已免除过渡总统，解散政府和过渡议会，并计划召开全国有生力量大会，推举新的过渡总统。请问中方有何评论？"
    #text = "哈萨克斯坦24KZ记者：我的问题涉及习近平主席对哈萨克斯坦的访问。请问这次访问主要内容以及对两国关系及其未来发展的意义是什么？"
    words = back_match(text)
    print(words)