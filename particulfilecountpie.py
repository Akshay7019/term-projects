import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
file_extension = ('.pyc','.py', '.h', '.js', '.png', '.c', '.dat', '.txt', '.html', '.jar', '.json', '.hpp', '.csv', '.xml', '.css', '.pdf', '.ipynb')
y_pos = np.arange(len(file_extension))
total_count = [27831,24549,4961,3644,813,1739,1580,1483,923,734,482,427,372,319,303,55,52]

plt.bar(y_pos, total_count, align='center', alpha=10,)
plt.xticks(y_pos, file_extension,rotation = 'vertical')
plt.ylabel('file_count')
plt.title('count of all type files')
 
plt.show()
