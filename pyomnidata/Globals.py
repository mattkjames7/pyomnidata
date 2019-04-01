import os

#try and find the OMNIDATA_PATH variable - this is where data will be stored
ModulePath = os.path.dirname(__file__)+'/'
try:
	DataPath = os.getenv('OMNIDATA_PATH')+'/'
except:
	print('Please set OMNIDATA_PATH environment variable')
	DataPath = ''
