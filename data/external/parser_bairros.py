import re

infile = 'lista_de_bairros_prefeitura.txt'
outfile = 'lista_de_bairros_prefeitura_revisar.txt'

with open(infile, 'r',  newline='') as f:
    lines = f.readlines()

wordlist_raw = []
wordlist = []

for line in lines:
    wordlist_raw.append(re.split('[-–]{1}', line))

for i in wordlist_raw:
    for j in i:
        wordlist.extend(j.split('\n'))

wordlist.sort()

with open(outfile, 'w', newline='') as f:
    for i in wordlist:
        f.write(i+'\n')
