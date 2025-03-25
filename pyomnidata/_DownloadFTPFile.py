from . import Globals
from ftplib import FTP_TLS
progress = 0
import numpy as np

def _GetCallback(f,ftp,fname):
	'''
	callback function for downloading the file
	
	Inputs
	======
	f : file
		instance of an open file (binary)
	ftp : FTP()
		ftp instance
	fname : str
		Name of the file on the server
	
	'''
	#get the size of the file
	ftp.sendcmd("TYPE i")
	size = ftp.size(fname)
	
	#set progress to 0
	global progress
	progress = 0
	
	def callback(chunk):
		f.write(chunk)
		global progress
		progress += len(chunk)
		
		ndone = np.int32(50*progress/size)
		sdone = '\r[' + '='*ndone + '-'*(50-ndone) + ']'
		print(sdone,end='')
		
	return callback
	
def _DownloadFTPFile(fname):
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

	#login to the FTP server
	ftp = FTP_TLS(Globals.ftpbase)
	ftp.login()  
	ftp.cwd(Globals.ftpdir)
	
	#open the output file
	f = open(f"{Globals.DataPath}/tmp/{fname}","wb")	

	#get the callback function
	global progress
	progress = 0
	cb = _GetCallback(f,ftp,fname)	
	
	#download binary file using ftplib
	print('Downloading: {:s}'.format(fname))
	ftp.retrbinary('RETR '+fname, cb)
	print()
	
	#close the file
	f.close()
	
	#close FTP connection
	ftp.close()	

	#return the file name
	return f"{Globals.DataPath}/tmp/{fname}"
