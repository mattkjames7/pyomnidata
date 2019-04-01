import os
from . import Globals
import numpy as np
import PyFileIO as pf
import RecarrayTools as RT
import DateTimeTools as TT
from ._ReadDataIndex import _ReadDataIndex
from ._UpdateDataIndex import _UpdateDataIndex


def _ConvertFTPFile(FullPath,fname,UpdateDate,Res):
	'''
	Converts standard OMNI ASCII files to binary, replaces missing data 
	flags with NAN where possible.
	
	Inputs:
		FullPath: full apth and file name of the input file
		fname: just the name of the input file
		UpdateDate: The date which this was last upated on the OMNI site.
		Res:	time resolution (1 or 5)
	
	'''

	#define the data type
	ErrVal = {'Year':999,
				'DOY':999,
				'Hour':99,
				'Minute':99,
				'SC_IMF':99,
				'SC_Plasma':99,
				'N_IMF':999,
				'N_Plasma':999,
				'PercInterp':999,
				'TimeShift':999999,
				'RMSTimeShift':999999,
				'RMSPhaseFrontNorm':99.99,
				'dTime':999999,
				'B':9999.99,
				'BxGSE':9999.99,
				'ByGSE':9999.99,
				'BzGSE':9999.99,
				'ByGSM':9999.99,
				'BzGSM':9999.99,
				'RMSSDBScalar':9999.99,
				'RMSSDFieldVector':9999.99,
				'FlowSpeed':99999.9,
				'Vx':99999.9,
				'Vy':99999.9,
				'Vz':99999.9,
				'ProtonDensity':999.99,
				'Temp':9999999.0,
				'FlowPressure':99.99,
				'E':999.99,
				'Beta':999.99,
				'MA':999.9,
				'Xsc':9999.99,
				'Ysc':9999.99,
				'Zsc':9999.99,
				'Xbsn':9999.99,
				'Ybsn':9999.99,
				'Zbsn':9999.99,
				'AE':99999,
				'AL':99999,
				'AU':99999,
				'SymD':99999,
				'SymH':99999,
				'AsyD':99999,
				'AsyH':99999,
				'PC':999.99,
				'Ms':99.9,
				'Pflux10':99999.99,
				'Pflux30':99999.99,
				'Pflux60':99999.99}
	if Res == 1:
		indtype = [('Year','int32'),('DOY','int32'),('Hour','int32'),('Minute','int32'),
					('SC_IMF','uint8'),('SC_Plasma','uint8'),('N_IMF','int32'),('N_Plasma','int32'),
					('PercInterp','float32'),('TimeShift','float32'),('RMSTimeShift','float32'),
					('RMSPhaseFrontNorm','float32'), ('dTime','float32'),('B','float32'),
					('BxGSE','float32'),('ByGSE','float32'),('BzGSE','float32'),('ByGSM','float32'),
					('BzGSM','float32'),('RMSSDBScalar','float32'),('RMSSDFieldVector','float32'),
					('FlowSpeed','float32'),('Vx','float32'),('Vy','float32'),('Vz','float32'),
					('ProtonDensity','float32'),('Temp','float32'),('FlowPressure','float32'),
					('E','float32'),('Beta','float32'),('MA','float32'),('Xsc','float32'),
					('Ysc','float32'),('Zsc','float32'),('Xbsn','float32'),('Ybsn','float32'),
					('Zbsn','float32'),('AE','float32'),('AL','float32'),('AU','float32'),
					('SymD','float32'),('SymH','float32'),('AsyD','float32'),('AsyH','float32'),
					('PC','float32'),('Ms','float32')]
		outdtype = Globals.dtype1
	else:
		indtype = [('Year','int32'),('DOY','int32'),('Hour','int32'),('Minute','int32'),
					('SC_IMF','uint8'),('SC_Plasma','uint8'),('N_IMF','int32'),('N_Plasma','int32'),
					('PercInterp','float32'),('TimeShift','float32'),('RMSTimeShift','float32'),
					('RMSPhaseFrontNorm','float32'), ('dTime','float32'),('B','float32'),
					('BxGSE','float32'),('ByGSE','float32'),('BzGSE','float32'),('ByGSM','float32'),
					('BzGSM','float32'),('RMSSDBScalar','float32'),('RMSSDFieldVector','float32'),
					('FlowSpeed','float32'),('Vx','float32'),('Vy','float32'),('Vz','float32'),
					('ProtonDensity','float32'),('Temp','float32'),('FlowPressure','float32'),
					('E','float32'),('Beta','float32'),('MA','float32'),('Xsc','float32'),
					('Ysc','float32'),('Zsc','float32'),('Xbsn','float32'),('Ybsn','float32'),
					('Zbsn','float32'),('AE','float32'),('AL','float32'),('AU','float32'),
					('SymD','float32'),('SymH','float32'),('AsyD','float32'),('AsyH','float32'),
					('PC','float32'),('Ms','float32'),('Pflux10','float32'),('Pflux30','float32'),
					('Pflux60','float32')]
		outdtype = Globals.dtype5

	#read the file
	data = pf.ReadASCIIData(FullPath,Header=False,dtype=indtype)
	
	#create output array
	n = np.size(data)
	out = np.recarray(n,dtype=outdtype)

	#convert dates
	for i in range(0,n):
		out.Date[i] = TT.DayNotoDate(data.Year[i],data.DOY[i])

	#convert time
	out.ut = data.Hour + data.Minute/60.0
	

	#copy new data across
	fields = data.dtype.names
	for f in fields:
		if f in out.dtype.names:
			out[f] = data[f]
			bad = np.where(out[f] == ErrVal[f])[0]
			if bad.size > 0:
				if 'float' in str(out[f].dtype):
					out[f][bad] = np.nan

				
			
	#get the year from the file name		
	Year = np.int32(fname[-8:-4])
	
	
	#save file
	outfname = 'OMNI-{:1d}min-{:4d}.bin'.format(Res,Year)
	outpath = Globals.DataPath+'{:1d}/'.format(Res)
	if not os.path.isdir(outpath):
		os.system('mkdir -pv '+outpath)
	RT.SaveRecarray(out,outpath+outfname)
	print('Saved file: '+outfname)
	
	
	#update index
	idx = _ReadDataIndex()
	use = np.where(idx.OldFileName == fname)[0]
	if use.size == 0:
		#this file does not yet exist within the index file
		tmp = np.recarray(1,dtype=idx.dtype)
		tmp[0].FileName = outfname
		tmp[0].OldFileName = fname
		tmp[0].UpdateDate = UpdateDate
		tmp[0].Res = Res
		idx = RT.JoinRecarray(idx,tmp)
	else:
		#file exists, update the information
		idx[use[0]].FileName = outfname
		idx[use[0]].OldFileName = fname
		idx[use[0]].UpdateDate = UpdateDate
		idx[use[0]].Res = Res
	_UpdateDataIndex(idx)
