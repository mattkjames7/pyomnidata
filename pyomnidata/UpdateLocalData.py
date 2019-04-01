import os
import numpy as np
from . import Globals
from ._ReadDataIndex import _ReadDataIndex
from ._DownloadFTPIndex import _DownloadFTPIndex
from ._ParseFTP import _ParseFTP
from ._CompareUpdates import _CompareUpdates
from ._DownloadFTPFile import _DownloadFTPFile
from ._ConvertFTPFile import _ConvertFTPFile
from ._DeleteFTPFile import _DeleteFTPFile

def UpdateLocalData(Force=False):
	'''
	This will download and convert any OMNI data which is missing from 
	the local archive.
	
	'''
	
	#let's download and read the FTP index
	status = _DownloadFTPIndex()
	if not status:
		print('Download failed; check for write permission to data folder')
		return
	FileNames,Addresses,UpdateDates,Res = _ParseFTP()
	n = np.size(FileNames)
	
	#check current data index
	idx = _ReadDataIndex()
	
	#now compare update dates
	if Force:
		update = np.ones(n,dtype='bool')
	else:
		update = _CompareUpdates(UpdateDates,FileNames,idx)
	use = np.where(update)[0]
	FileNames = FileNames[use]
	Addresses = Addresses[use]
	UpdateDates = UpdateDates[use]
	Res = Res[use]
	n = use.size

	if n == 0:
		print('No files to update.')
		return 
		
	for i in range(0,n):
		print('Downloading file {0} of {1}'.format(i+1,n))
		#download file
		tmp = _DownloadFTPFile(Addresses[i],FileNames[i])
		
		print('Converting to binary')
		#convert file
		_ConvertFTPFile(tmp,FileNames[i],UpdateDates[i],Res[i])
		
		#delete text file
		_DeleteFTPFile(tmp)
		
	print('Done')
	
