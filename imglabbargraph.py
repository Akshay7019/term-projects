import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
file_extension = ('ql', 'pyc', 'w', 'ch', 'fig', 'tr', 'lo', 'w', 'am', 'xbm', 'pl', 'tcx', 'gz', 'cur', 'gif', 'in', 'sh', 'enc', 'test', 'msg', 'py', 'cc', 'txt', 'tcl', 'ino', 'o', 'html', 'c', 'h')
y_pos = np.arange(len(file_extension))
total_count = [1,4,10,22,22,27,35,47,51,66,69,78,78,78,80,106,153,158,244,294,478,615,678,947,1386,1771,1896,2492,5495]

plt.bar(y_pos, total_count, align='center', alpha=10)
plt.xticks(y_pos, file_extension,rotation = 'vertical')
plt.ylabel('file_count')
plt.title('count of all type files')
 
plt.show()
