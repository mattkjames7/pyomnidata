import os

#try and find the OMNIDATA_PATH variable - this is where data will be stored
ModulePath = os.path.dirname(__file__)+'/'
try:
	DataPath = os.getenv('OMNIDATA_PATH')+'/'
except:
	print('Please set OMNIDATA_PATH environment variable')
	DataPath = ''

#loaded data
loaded1 = {}
loaded5 = {}

#some dtypes

dtype1 = [('Date','int32'),('ut','float32'),
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
dtype5 = [('Date','int32'),('ut','float32'),
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
