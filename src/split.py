import PyPDF2, re


def find(input, string):
    pdf = input
    for page in range(0, pdf.getNumPages()):
        content = ""
        content += pdf.getPage(page).extractText().lower()
        if re.search(string, content) is not None:
            return page

def split(input, output, first, last):
    pdf = input
    pdf_writer = PyPDF2.PdfFileWriter()
    for page in range(first, last):
        pdf_writer.addPage(pdf.getPage(page))
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

infile = '../data/raw/boletim-atualizado.pdf'
pdf = PyPDF2.PdfFileReader(infile)
print(pdf.documentInfo)

#string = 'boletim coronavírus - óbitos'
string = 'óbitos'
outfile = '../data/interim/boletim-atualizado-internacoes.pdf'
first = 0
last = find(pdf, string)
split(pdf, outfile, first, last)

#string = 'boletim coronavírus - pcr'
string = 'pcrpositivo'
outfile = '../data/interim/boletim-atualizado-obitos.pdf'
first = last
last = find(pdf, string)
split(pdf, outfile, first, last)

#string = 'boletim coronavírus - testes rápidos'
string = 'rápidosatualizado'
outfile = '../data/interim/boletim-atualizado-pcr.pdf'
first = last
last = find(pdf, string)
split(pdf, outfile, first, last)

outfile = '../data/interim/boletim-atualizado-testes-rapidos.pdf'
first = last
last = pdf.getNumPages()
split(pdf, outfile, first, last)
