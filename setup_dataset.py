
url1 = 'https://data.mendeley.com/public-files/datasets/3dhn4xnjxw/files/7b73f607-2e05-4bf1-9152-adf872a98634/file_downloaded'
url2 = 'https://data.mendeley.com/public-files/datasets/3dhn4xnjxw/files/b46506db-892d-4cbc-ac9d-5787edaf534f/file_downloaded'

import urllib.request
import patoolib
import shutil
import os 
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(
  url1,
   "S13_S21.rar")

urllib.request.urlretrieve(
  url2,
   "S19_S11.rar")

# use if exists
# shutil.rmtree('/content/data')
# shutil.rmtree('/content/test_data')


os.makedirs('data')
patoolib.extract_archive("S13_S21.rar", outdir="data")
patoolib.extract_archive("S19_S11.rar", outdir="data")
 
shutil.rmtree('/content/data/S13_S21/I11')
shutil.rmtree('/content/data/S13_S21/I12')

shutil.rmtree('/content/data/S19_S11/I11')
shutil.rmtree('/content/data/S19_S11/I12')

os.makedirs('test_data')
patoolib.extract_archive("S13_S21.rar", outdir="test_data")
patoolib.extract_archive("S19_S11.rar", outdir="test_data")

shutil.rmtree('/content/test_data/S13_S21/I1')
shutil.rmtree('/content/test_data/S13_S21/I2')
shutil.rmtree('/content/test_data/S13_S21/I3')
shutil.rmtree('/content/test_data/S13_S21/I4')
shutil.rmtree('/content/test_data/S13_S21/I5')
shutil.rmtree('/content/test_data/S13_S21/I6')
shutil.rmtree('/content/test_data/S13_S21/I7')
shutil.rmtree('/content/test_data/S13_S21/I8')
shutil.rmtree('/content/test_data/S13_S21/I9')

shutil.rmtree('/content/test_data/S19_S11/I1')
shutil.rmtree('/content/test_data/S19_S11/I2')
shutil.rmtree('/content/test_data/S19_S11/I3')
shutil.rmtree('/content/test_data/S19_S11/I4')
shutil.rmtree('/content/test_data/S19_S11/I5')
shutil.rmtree('/content/test_data/S19_S11/I6')
shutil.rmtree('/content/test_data/S19_S11/I7')
shutil.rmtree('/content/test_data/S19_S11/I8')
shutil.rmtree('/content/test_data/S19_S11/I9')

