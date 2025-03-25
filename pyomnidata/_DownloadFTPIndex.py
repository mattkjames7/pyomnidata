import os
from . import Globals

def _DownloadFTPIndex(ftp):
	'''
	This routine downloads the index.html of the omni FTP site:
	ftp://spdf.gsfc.nasa.gov/pub/data/omni/high_res_omni/
	
	Returns:
		Boolean, True if index file exists
	
	'''
	#check that the temporary folder exists
	if not os.path.isdir(f"{Globals.DataPath}/tmp"):
		os.makedirs(f"{Globals.DataPath}/tmp")

	#download using ftplib
	foo=open(f"{Globals.DataPath}/tmp/index.html","w")	
	files = ftp.mlsd(facts=['modify'])
	for file in files:
		line = file[0] + ' ' + file[1].get('modify') + '\n'
		foo.write(line)
	foo.close()
	

	#check that the file exists, return True if so
	return os.path.isfile(f"{Globals.DataPath}/tmp/index.html")
	
