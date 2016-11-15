import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
file_extension = ('jpeg', 'dde', 'm4', 'sn', 'xml', 'lef', 'pak', 'jar', 'txt', 'tel', 'h', 'pdf', 'state', 'o', 'sv', 'png', 'lib', 'db')
y_pos = np.arange(len(file_extension))
total_count = [9,10,20,47,58,106,121,160,225,243,260,369,399,431,1229,1566,2639,3558]

plt.bar(y_pos, total_count, align='center', alpha=10)
plt.xticks(y_pos, file_extension,rotation = 'vertical')
plt.ylabel('file_count')
plt.title('count of all type files')
 
plt.show()