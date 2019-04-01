import numpy as np
import matplotlib.pyplot as plt
from .GetOMNI import GetOMNI

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

def PlotOMNI(Param,Date,ut=[0.0,24.0],Color=None,fig=None,maps=[1,1,0,0],**kwargs):
	'''
	Plots OMNI Parameters.
	'''
	nPar = np.size(Param)
	
	
