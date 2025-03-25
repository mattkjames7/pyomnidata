import numpy as np
from . import Globals
import RecarrayTools as RT

def _ReadSolarFlux():
	'''
	Read the solar flux data from disk.
	
	'''
	fname = f"{Globals.DataPath}/F107.bin"
	
	return RT.ReadRecarray(fname,Globals.fdtype)
