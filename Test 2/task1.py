import random

import pandas as pd
import pymorphy3
morph = pymorphy3.MorphAnalyzer()

df = pd.read_csv(r'C:\Users\janep\Desktop\codes\57Sch\2024\i-love-crispy-laptops\Test2\word_forms.zip', compression='zip', sep='\t', encoding = 'ISO-8859-1')


def get_info(word: str) -> pymorphy3.tagset:
    return morph.parse(word)[0].tag


def sim_finder(word: str) -> str:
    sims = df[df['pos']== get_info(word)]['1gram'].values
    return sims[random.randrange(0, len(sims), 1)]


def sen_maker(sentence: str) -> list:
    sen_parsed = sentence.split(' ')
    sen_return = []
    for word in sen_parsed:
        sen_return.append(sim_finder(word))
    return sen_return


df['pos'] = df['1gram'].apply(lambda x: get_info(str(x))) # В датасете почему то были float...
sentence = input("Введите")
print(sentence)
print(*sen_maker(sentence))
