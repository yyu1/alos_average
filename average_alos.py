import numpy as np

in_file = '/dataraid/roc/data/ALOS/roc_alos_2015_hh.uint'
out_file = '/dataraid/roc/data/ALOS/roc_alos_2015_hh_3.2sec.flt'


xdim = 45000
ydim = 67500

outline = np.empty(xdim/4, dtype=np.float32)

with open(in_file, "rb") as infile:
	with open(out_file, "wb") as outfile:
		for j in range(0,np.uint64((ydim/4)-1)):
			inline = np.fromfile(infile, dtype=np.uint16, count=xdim*4).reshape(4,xdim)

			for i in range(0,np.uint64((xdim/4)-1)):
                                box = inline[:,i*4:(i+1)*4]
                                count = np.count_nonzero(box)
                                if (count > 0):
			            #convert to linear power
                                    box_db = 20.0 * np.log10(np.float64(box[np.nonzero(box)])) - 83
                                    box_lp = np.power(10,0.1*box_db)
                                    outline[i] = np.float32(np.mean(box_lp))
                                else:
                                    outline[i] = 0

			outline.tofile(outfile)
