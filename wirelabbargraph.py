import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
file_extension = ('xlsm', 'xlsx', 'exe', 'out', 'ipynb', 'sav', 'n', 'gif', 'sh', 'cc', 'hpp', 'json', 'c', 'tcl', 'gz', 'sip', 'so', 'java', 'txt', 'png', 'js', 'html', 'conf', 'h', 'py', 'pyc')
y_pos = np.arange(len(file_extension))
total_count = [150,162,179,234,277,417,579,736,817,1595,2362,2413,3541,3693,4653,5110,5268,5539,6086,6429,18265,23913,25678,25885,123704,139337]

plt.bar(y_pos, total_count, align='center', alpha=10)
plt.xticks(y_pos, file_extension, rotation = 'vertical')
plt.ylabel('file_count')
plt.title('count of all type files')
 
plt.show()
