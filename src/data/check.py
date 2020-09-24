import requests, os
import time, pytz
from datetime import datetime
from dateutil.parser import parse

basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(basepath)

url = 'http://www.americana.sp.gov.br/coronavirus/boletim-atualizado.pdf'
file = 'data/raw/boletim-atualizado.pdf'
r = requests.head(url)
url_time = parse(r.headers['last-modified'])

pattern = '%Y-%m-%d %H:%M:%S'
url_epoch_time = int(time.mktime(time.strptime(url_time.strftime(pattern), pattern)))

file_time_naive = datetime.fromtimestamp(os.path.getmtime(file))
tz_sp = pytz.timezone('America/Sao_Paulo')
file_time = tz_sp.localize(file_time_naive)

if url_time > file_time:
    file_name, file_extension = os.path.splitext(file)
    os.rename(file, file_name + '_' + str(file_time.date()) + file_extension)
    open(file, 'wb').write(requests.get(url).content)
    os.utime(file, (url_epoch_time, url_epoch_time))
    print('Arquivo "%s" atualizado!' % file)
else:
    print('Não há uma versão mais recente de "%s"!' % file)
