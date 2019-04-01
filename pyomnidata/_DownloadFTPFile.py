import os
from . import Globals

def _DownloadFTPFile(addr,fname):
	'''
	Downloads a file from an FTP site, returns the full path of the 
	local version of that file.
	
	Inputs:
		addr: full address of file to be downloaded e.g. 
			ftp://a.b.c/folder/file.txt
		fname: file name e.g. file.txt
		
	Returns:
		full path to downloaded file
	'''
	
	#wget the file
	os.system('wget '+addr+' -O '+Globals.DataPath+'tmp/'+fname)
	

	#return the file name
	return Globals.DataPath+'tmp/'+fname
