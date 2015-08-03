import urllib
import sys
import pdb
import os

start_page = 146
end_page = 380

# Raag Dabari
# url_prefix = "http://www.new.dli.ernet.in/data/upload/0043/064/PTIFF/"
# Deewan-e-ghalib (Hindi)
# url_prefix = "http://www.new1.dli.ernet.in/data6/upload/0141/719/PTIFF/"
# Deewan-e-ghalib (English)
url_prefix = "http://www.new.dli.ernet.in/data/upload/0042/567/PTIFF/"

path_to_save = "/home/chaturvedi/Downloads/deewan-e-ghalib-english/"
os.chdir(path_to_save)

for x in range(start_page,end_page):
  complete_url =  url_prefix + str(x).zfill(8) + ".tif"
  print("Downloading # " + str(x))
  file_name = str(x).zfill(4)
  urllib.urlretrieve(complete_url, path_to_save + file_name + ".tif")
  # Coverting page-by-page, can't convert in one go
  os.system('convert ' + file_name + '.tif ' + file_name + '.pdf')


os.system('pdftk *.pdf cat output combined.pdf')
