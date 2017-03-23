import numpy as np

in_file = '/dataraid/roc/data/alos'
out_file = '/dataraid/roc/outfile'


xdim = 4000
ydim = 4000

outline = np.empty(xdim/4, dtype=np.int16)

with infile = open(in_file, "rb"):
	with outfile = open(out_file, "wb"):
		for j in range(0,(ydim/4)-1):
			inline = np.fromfile(infile, dtype=np.int16, count=xdim*4).reshape(4,xdim)
			#convert to linear power
			inline_db = 20.0 * np.log10(np.float64(inline)) - 83
			inline_lp = np.power(10,0.1*inline_db)

			for i in range(0,(xdim/4)-1):
				outline[i] = np.int16(np.mean(inline_lp[:,i*4:i*4+3]))

			outline.tofile(outfile)
