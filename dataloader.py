def load_data(path):
    with open(path, 'r', encoding='utf-8')as f:
        raw = f.readlines()
        article=[]
        for line in raw:
            line=line.replace('\n', '')
            article.append(line)
        article=list(filter(None, article))
    return article