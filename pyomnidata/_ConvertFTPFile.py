import os
from . import Globals
import numpy as np
import PyFileIO as pf
import RecarrayTools as RT
import DateTimeTools as TT

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
	if Res == 1:
		indtype = [('Year','int32'),('DOY','int32'),('Hour','int32'),('Minute','int32'),
					('SC_IMF','uint8'),('SC_Plasma','uint8'),('N_IMF','int32'),('N_Plasma','int32'),
					('PercInterp','float32'),('TimeShift','float32'),('RMSTimeShift','float32'),
					('RMSPhaseFrontNorm','float32'), ('dTime','float32'),('B','float32'),
					('BxGSE','float32'),('ByGSE','float32'),('BzGSE','float32'),('ByGSM','float32'),
					('BzGSM','float32'),('RMSSDBScalar','flaot32'),('RMSSDFieldVector','float32'),
					('FlowSpeed','float32'),('Vx','float32'),('Vy','float32'),('Vz','float32'),
					('ProtonDensity','float32'),('Temp','float32'),('FlowPressure','float32'),
					('E','float32'),('Beta','float32'),('MA','float32'),('Xsc','float32'),
					('Ysc','float32'),('Zsc','float32'),('Xbsn','float32'),('Ybsn','float32'),
					('Zbsn','float32'),('AE','float32'),('AL','float32'),('AU','float32'),
					('SymD','float32'),('SymH','float32'),('AsyD','float32'),('AsyH','float32'),
					('PC','float32'),('Ms','float32')]
		outdtype = [('Date','int32'),('ut','float32'),
					('SC_IMF','uint8'),('SC_Plasma','uint8'),('N_IMF','int32'),('N_Plasma','int32'),
					('PercInterp','float32'),('TimeShift','float32'),('RMSTimeShift','float32'),
					('RMSPhaseFrontNorm','float32'), ('dTime','float32'),('B','float32'),
					('BxGSE','float32'),('ByGSE','float32'),('BzGSE','float32'),('ByGSM','float32'),
					('BzGSM','float32'),('RMSSDBScalar','flaot32'),('RMSSDFieldVector','float32'),
					('FlowSpeed','float32'),('Vx','float32'),('Vy','float32'),('Vz','float32'),
					('ProtonDensity','float32'),('Temp','float32'),('FlowPressure','float32'),
					('E','float32'),('Beta','float32'),('MA','float32'),('Xsc','float32'),
					('Ysc','float32'),('Zsc','float32'),('Xbsn','float32'),('Ybsn','float32'),
					('Zbsn','float32'),('AE','float32'),('AL','float32'),('AU','float32'),
					('SymD','float32'),('SymH','float32'),('AsyD','float32'),('AsyH','float32'),
					('PC','float32'),('Ms','float32')]
	else:
		indtype = [('Year','int32'),('DOY','int32'),('Hour','int32'),('Minute','int32'),
					('SC_IMF','uint8'),('SC_Plasma','uint8'),('N_IMF','int32'),('N_Plasma','int32'),
					('PercInterp','float32'),('TimeShift','float32'),('RMSTimeShift','float32'),
					('RMSPhaseFrontNorm','float32'), ('dTime','float32'),('B','float32'),
					('BxGSE','float32'),('ByGSE','float32'),('BzGSE','float32'),('ByGSM','float32'),
					('BzGSM','float32'),('RMSSDBScalar','flaot32'),('RMSSDFieldVector','float32'),
					('FlowSpeed','float32'),('Vx','float32'),('Vy','float32'),('Vz','float32'),
					('ProtonDensity','float32'),('Temp','float32'),('FlowPressure','float32'),
					('E','float32'),('Beta','float32'),('MA','float32'),('Xsc','float32'),
					('Ysc','float32'),('Zsc','float32'),('Xbsn','float32'),('Ybsn','float32'),
					('Zbsn','float32'),('AE','float32'),('AL','float32'),('AU','float32'),
					('SymD','float32'),('SymH','float32'),('AsyD','float32'),('AsyH','float32'),
					('PC','float32'),('Ms','float32'),('Pflux10','float32'),('Pflux30','float32'),
					('Pflux60','float32')]
		outdtype = [('Date','int32'),('ut','float32'),
					('SC_IMF','uint8'),('SC_Plasma','uint8'),('N_IMF','int32'),('N_Plasma','int32'),
					('PercInterp','float32'),('TimeShift','float32'),('RMSTimeShift','float32'),
					('RMSPhaseFrontNorm','float32'), ('dTime','float32'),('B','float32'),
					('BxGSE','float32'),('ByGSE','float32'),('BzGSE','float32'),('ByGSM','float32'),
					('BzGSM','float32'),('RMSSDBScalar','flaot32'),('RMSSDFieldVector','float32'),
					('FlowSpeed','float32'),('Vx','float32'),('Vy','float32'),('Vz','float32'),
					('ProtonDensity','float32'),('Temp','float32'),('FlowPressure','float32'),
					('E','float32'),('Beta','float32'),('MA','float32'),('Xsc','float32'),
					('Ysc','float32'),('Zsc','float32'),('Xbsn','float32'),('Ybsn','float32'),
					('Zbsn','float32'),('AE','float32'),('AL','float32'),('AU','float32'),
					('SymD','float32'),('SymH','float32'),('AsyD','float32'),('AsyH','float32'),
					('PC','float32'),('Ms','float32'),('Pflux10','float32'),('Pflux30','float32'),
					('Pflux60','float32')]

	#read the file
	data = pf.ReadASCIIData(FullPath,Header=False,dtype=indtype)
	
	#create output array
	n = np.size(data)
	out = np.recarray(n,dtype=outdtype)

	#convert dates
	for i in range(0,n):
		out.Date[i] = TT.DayNoToDate(data.Year[i],data.DOY[i])

	#convert time
	out.ut = data.Hour + data.Minute/60.0
	

	#copy new data across
	fields = data.dtype.names
	for f in fields:
		if f in out.dtype.names:
			out[f] = data[f]
			
	#save file
	
	
	#update index
