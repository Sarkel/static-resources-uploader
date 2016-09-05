import shutil
import os


dirr = 'tmp/'
fileName = 'DA_Resources'
path = 'source'
correctName = fileName + '.resource'
antDir = 'retrieveUnpackaged/staticresources/'
for file in os.listdir(dirr):
    os.remove(dirr + file)

shutil.make_archive(dirr + fileName, 'zip', path)
os.rename(dirr + fileName + '.zip', dirr + correctName)
if os.path.exists(antDir + correctName):
    os.remove(antDir + correctName)
os.rename(dirr + correctName, antDir + correctName)

for file in os.listdir(dirr):
    os.remove(dirr + file)

os.system('ant deployUnpackaged')
