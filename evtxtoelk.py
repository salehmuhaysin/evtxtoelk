import os
from evtxtoelk.evtxtoelk import EvtxToElk

"""
==============================================

This script used to push evtx files to elasticsearch database
change the values for:
evtx_dir: folder contains all evtx files
index: index to push to on the database
url: URL for the elasticsearch database


special thanks to Dragos [dgunter] developing the base line of this script
https://github.com/dgunter/evtxtoelk

==============================================
"""


evtx_dir = "Event_Logs1"
index = 'windows_events'
url = "http://172.16.246.131:9200"
fl = os.listdir(evtx_dir)
dir_path = os.path.dirname(os.path.realpath(__file__))+"/" + evtx_dir

for f in fl:
	path =  os.path.join(dir_path,f)
	print path
	try:
		EvtxToElk.evtx_to_elk(path,url,index)
	except:
		pass
