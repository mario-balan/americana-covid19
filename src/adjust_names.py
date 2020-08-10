import csv, re
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import difflib

def name_checker(wrong_names,correct_names):
    names_array = []
    ratio_array = []
    for wrong_name in wrong_names:
            x=process.extractOne(wrong_name,correct_names,scorer=fuzz.ratio)
            names_array.append(x[0].upper())
            ratio_array.append(x[1])
    return names_array,ratio_array

def diff_checker(wrong_names,correct_names):
    names_array = []
    for wrong_name in wrong_names:
        match = difflib.get_close_matches(wrong_name,correct_names)
        if match:
            names_array.append(match)
        else:
            names_array.append('')

    return names_array

# read files:
workfile = '../data/interim/boletim-atualizado-pcr.csv'
wordlistfile = '../data/external/lista_de_bairros.txt'
wordlistfilealternate = '../data/external/lista_de_bairros_prefeitura_curada.txt'

df = pd.read_csv(workfile)

with open(wordlistfilealternate, newline='') as f:
    lines = f.readlines()

wordlist_alternate = []

for i in lines:
        wordlist_alternate.append(i.strip('\n'))

with open(wordlistfile, newline='') as f:
    lines = f.readlines()

wordlist_raw = []
wordlist = []


for line in lines:
    wordlist_raw.append(line.strip())

for i in wordlist_raw:
    nome = re.search('^[^\(]+', i)
    tipo = re.search('(?<=\()(.*?)(?=\s*\))', i)
    if nome and tipo:
        wordlist.append(tipo.group().strip()+' '+nome.group().strip())
    else:
        wordlist.append(nome.group().strip())

match_entry = df.Bairro.tolist()
#match_options = wordlist
match_options = wordlist_alternate

name_match,ratio_match = name_checker(match_entry,match_options)
#name_match = diff_checker(match_entry,match_options)

df_out = pd.DataFrame()
df_out['old_name'] = pd.Series(match_entry)
df_out['correct_name_auto'] = pd.Series(name_match)
df_out['correct_ratio'] = pd.Series(ratio_match)

df_out.to_csv(r'../teste.csv', index=False)
