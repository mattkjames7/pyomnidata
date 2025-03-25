import numpy as np
import os
from . import Globals
from urllib import request

def _DownloadF107(EndDate):
	'''
	Download F10.7 index data from OMNI
	
	'''
	#the output file:
	ofile = f"{Globals.DataPath}/F107.lst"

	#this is the wget command to run
	#cmd0 = 'wget --post-data "activity=retrieve&res=hour&spacecraft=omni2&start_date=19631128&end_date={:08d}&vars=50&scale=Linear&ymin=&ymax=&view=0&charsize=&xstyle=0&ystyle=0&symbol=0&symsize=&linestyle=solid&table=0&imagex=640&imagey=480&color=&back=" https://omniweb.gsfc.nasa.gov/cgi/nx1.cgi -O '.format(EndDate)
	
	#replaced the above with the below url and POST data
	urldata = 'activity=retrieve&res=daily&spacecraft=omni2_daily&start_date=19631128&end_date={:08d}&vars=50&scale=Linear&ymin=&ymax=&view=0&charsize=&xstyle=0&ystyle=0&symbol=0&symsize=&linestyle=solid&table=0&imagex=640&imagey=480&color=&back='.format(EndDate)
	url = 'https://omniweb.gsfc.nasa.gov/cgi/nx1.cgi'
	
	#urllib stuff
	req = request.Request(url,data=urldata.encode())
	resp = request.urlopen(req)
	
	#save it
	f = open(ofile,'w')
	f.write(resp.read().decode('utf-8'))
	f.close()
