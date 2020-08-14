import csv, re
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import difflib

def name_checker(wrong_names,correct_names):
    filter = ['I', 'II', 'III']
    names_array = []
    ratio_array = []
    for wrong_name in wrong_names:
        #wrong_name_term = [x for x in wrong_name.split(' ') if x.upper() not in filter][-1]
        #possible_names = process.extract(wrong_name_term,correct_names,scorer=fuzz.partial_ratio)
        possible_names = process.extract(wrong_name,correct_names,scorer=fuzz.token_set_ratio)
        possible_names_refined = process.extract(wrong_name,[x[0] for x in possible_names[:3]],scorer=fuzz.partial_ratio)
        correct_name = process.extractOne(wrong_name,[x[0] for x in possible_names_refined[:2]],scorer=fuzz.ratio)
        print(wrong_name)
        print(possible_names[:3])
        print(possible_names_refined[:2])
        print(correct_name)
        names_array.append(correct_name[0])
        ratio_array.append(correct_name[1])
    return names_array,ratio_array

# read files:
workfile = '../data/interim/boletim-atualizado-pcr.csv'
wordlistfile = '../data/external/lista_de_bairros_prefeitura_curada.txt'

df = pd.read_csv(workfile)

wordlist = []

with open(wordlistfile, newline='') as f:
    lines = f.readlines()

for i in lines:
        wordlist.append(i.strip('\n'))


#match_entry = df.Bairro.tolist()
match_entry = sorted(set(df.Bairro.tolist()))
match_options = wordlist

name_match,ratio_match = name_checker(match_entry,match_options)

df_out = pd.DataFrame()
df_out['old_name'] = pd.Series(match_entry)
df_out['correct_name_auto'] = pd.Series(name_match)
df_out['correct_ratio'] = pd.Series(ratio_match)

df_out.to_csv(r'../data/processed/names_test.csv', index=False)
