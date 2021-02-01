import numpy as np
import os
from . import Globals

def _DownloadF107(EndDate):
	'''
	Download F10.7 index data from OMNI
	
	'''
	#this is the wget command to run
	cmd0 = 'wget --post-data "activity=retrieve&res=hour&spacecraft=omni2&start_date=19631128&end_date={:08d}&vars=50&scale=Linear&ymin=&ymax=&view=0&charsize=&xstyle=0&ystyle=0&symbol=0&symsize=&linestyle=solid&table=0&imagex=640&imagey=480&color=&back=" https://omniweb.gsfc.nasa.gov/cgi/nx1.cgi -O '.format(EndDate)
	
	#the output file:
	ofile = Globals.DataPath + 'F107.lst'
	
	#run it
	os.system(cmd0 + ofile)
