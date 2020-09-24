import camelot
import csv, os

basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(basepath)

#Lista de Óbitos:
infile = 'data/interim/boletim-atualizado-obitos.pdf'
outfile = 'data/interim/boletim-atualizado-obitos.csv'

tables = camelot.read_pdf(infile, flavor='stream', pages='all')
output = []

print(infile,':')

for table in tables:
    print(table, table.parsing_report)
    output.extend(table.data)

output = output[2:]

with open(outfile, 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for row in output:
        wr.writerow(row)

#Lista de Casos por PCR:

infile = 'data/interim/boletim-atualizado-pcr.pdf'
outfile = 'data/interim/boletim-atualizado-pcr.csv'
tables = camelot.read_pdf(infile, flavor='stream', pages='all')
output = []

print(infile,':')

for table in tables:
    print(table, table.parsing_report)
    output.extend(table.data)

output = output[2:]

with open(outfile, 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for row in output:
        wr.writerow(row)

#Lista de Casos por Testes Rápidos:

infile = 'data/interim/boletim-atualizado-testes-rapidos.pdf'
outfile = 'data/interim/boletim-atualizado-testes-rapidos.csv'
tables = camelot.read_pdf(infile, flavor='stream', pages='all')
output = []

print(infile,':')

for table in tables:
    print(table, table.parsing_report)
    output.extend(table.data)

output = output[2:]

with open(outfile, 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for row in output:
        wr.writerow(row)

#Lista de Internações:

infile = 'data/interim/boletim-atualizado-internacoes.pdf'
outfile = 'data/interim/boletim-atualizado-internacoes.csv'
tables = camelot.read_pdf(infile, flavor='stream', pages='all')
output = []

print(infile,':')

for table in tables:
    print(table, table.parsing_report)
    output.extend(table.data)

output = output[2:]

with open(outfile, 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for row in output:
        wr.writerow(row)
