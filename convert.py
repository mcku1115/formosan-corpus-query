import os
import re
import json

corpus = []

for tf in os.listdir('txt/'):
    with open(os.path.join('txt/', tf), encoding='utf-8') as f:
        data = f.readlines()
    
    text = []
    for line in data:
        text.append(line.rstrip())
    
    atayal_text = [line for line in text if re.match('^a:', line)]
    mandarin_text = [line for line in text if re.match('^m:', line)]  

    for i in range(0, len(atayal_text)):
        atayal_text[i] = re.sub('^a: ', '', atayal_text[i])
        atayal_text[i] = list(atayal_text[i].split(" "))
        for j in range(len(atayal_text[i])):
            atayal_text[i][j] = {'word': atayal_text[i][j]}


    for i in range(0, len(mandarin_text)):
        mandarin_text[i] = re.sub('^m: ', '', mandarin_text[i])
        mandarin_text[i] = list(mandarin_text[i].split(" "))

    corp_dict = {'atayal': atayal_text, 'mandarin': mandarin_text}

    corpus.append(corp_dict)


with open('corpus.jsonl', 'w', encoding='utf-8') as f:
        json.dump(corpus, f, ensure_ascii=False)




        

