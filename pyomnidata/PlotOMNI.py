import numpy as np
import matplotlib.pyplot as plt
from .GetOMNI import GetOMNI
import DateTimeTools as TT
from ._DTPlotLabel import _DTPlotLabel

ParInfo = {'N_IMF':'# of points in IMF averages',
			'N_Plasma':'# of points in Plasma averages',
			'PercInterp':'% Interpolated',
			'TimeShift':'Time Shift (s)',
			'RMSTimeShift':'RMS Time Shift (s)',
			'RMSPhaseFrontNorm':'RMS Phase Front Normal',
			'dTime':'Time Between Observations (s)',
			'B':'|B| (nT)',
			'BxGSE':'$B_{xGSE}$ (nT)',
			'ByGSE':'$B_{yGSE}$ (nT)',
			'BzGSE':'$B_{zGSE}$ (nT)',
			'ByGSM':'$B_{yGSM}$ (nT)',
			'BzGSM':'$B_{zGSM}$ (nT)',
			'RMSSDBScalar':'RMS SD B Scalar (nT)',
			'RMSSDFieldVector':'RMS SD Field Vector (nT)',
			'FlowSpeed':'Flow Speed (km s$^{-1}$)',
			'Vx':'$V_x$ (km s$^{-1}$)',
			'Vy':'$V_y$ (km s$^{-1}$)',
			'Vz':'$V_z$ (km s$^{-1}$)',
			'ProtonDensity':'Proton Density (cm$^{-3}$)',
			'Temp':'Temperature (K)',
			'FlowPressure':'Flow Pressure (nPa)',
			'E':'Electric Field (mV m$^{-1}$)',
			'Beta':'$\beta$',
			'MA':'$M_A$',
			'Xsc':'$X_{sc}$ (Re)',
			'Ysc':'$Y_{sc}$ (Re)',
			'Zsc':'$Z_{sc}$ (Re)',
			'Xbsn':'$X_{bsn}$ (Re)',
			'Ybsn':'$Y_{bsn}$ (Re)',
			'Zbsn':'$Z_{bsn}$ (Re)',
			'AE':'AE (nT)',
			'AL':'AL (nT)',
			'AU':'AU (nT)',
			'SymD':'Sym-D (nT)',
			'SymH':'Sym-H (nT)',
			'AsyD':'Asy-D (nT)',
			'AsyH':'Asy-H (nT)',
			'PC':'PC Index',
			'Ms':'$M_{ms}$',
			'Pflux10':'Proton Flux (>10 MeV)',
			'Pflux30':'Proton Flux (>30 MeV)',
			'Pflux60':'Proton Flux (>60 MeV)'}

def PlotOMNI(Param,Date,ut=[0.0,24.0],Color=None,fig=None,maps=[1,1,0,0],Res=5,Clip=None,**kwargs):
	'''
	Plots OMNI Parameters.
	
	Inputs:
		Param: string or list of string containing parameter string(s)
			to plot
		Date:	Integer or 2-element array of integer dates to plot on or
			between in the format yyyymmdd.
		ut: Time range to plot between.
		Color: Color(s) for each parameter, if just one color is provided
			all lines will be the same color, if None then colors are 
			picked automatically by matplotlib.
		fig:	Set this to  a matplotlib.pyplot object to use an 
			existing plot window.
		maps: 4-element list/tuple/array containing the grid map of the
			subplot [xmaps,ymaps,xmap,ymap], where xmaps and ymaps are 
			the total number of subplots in each direction; xmap and 
			ymap control the position of the current subplot, starting
			at 0.
		Res: 5 or 1, for 5 minute or 1 minute data.
		Clip: If set to a 2 element list/tuple/array it defines the 
			parameter range within which to plot, otherwise None will
			plot everything finite.
		
	Returns:
		matplotlib.pyplot.axis
	
	'''
	nPar = np.size(Param)
	pars = np.array([Param]).flatten()
	
	#load data
	Year = np.unique([np.array(Date)//10000])	
	data = GetOMNI(Year,Res)
	
	if np.size(Date) == 1:
		use = np.where((data.Date == Date) & (data.ut >= ut[0]) & (data.ut <= ut[1]))[0]
	else:
		use = np.where(((data.Date == Date[0]) & (data.ut >= ut[0])) |
						((data.Date == Date[1]) & (data.ut <= ut[1])) |
						((data.Date > Date[0]) & (data.Date < Date[1])))
	data = data[use]
	
	#create continuous time axis
	utc = np.copy(data.ut)
	dt = np.where(utc[1:] < utc[:-1])[0]
	for i in range(0,dt.size):
		dd = TT.DateDifference(data.Date[dt[i]],data.Date[dt[i]+1])
		utc[dt[i]+1:] += 24.0*dd
		
	#create plot window and axis
	if fig is None:
		fig = plt
		fig.figure()
	ax = fig.subplot2grid((maps[1],maps[0]),(maps[3],maps[2]))
	
	#plot each parameter
	for i in range(nPar):
		y = data[pars[i]]
		if Color is None:
			col = None
		elif np.size(Color) in [3,4]:
			col = Color
		else:
			col = Color[i % np.shape(Color)[0]]
		if not Clip is None:
			bad = np.where((y < Clip[0]) | (y > Clip[1]))[0]
			y[bad] = np.nan
		ax.plot(utc,y,color=col,label=ParInfo[pars[i]],**kwargs)
		
	_DTPlotLabel(fig,utc,data.Date)
	ax.legend()
	return ax
	
