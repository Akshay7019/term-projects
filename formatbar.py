import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
file_extension = ('Binary','Text', 'Xml', 'Zip')
y_pos = np.arange(len(file_extension))
total_count = [22440,160369,561,1044]


##total = Binary+Text+Xml+Zip

#sizes.append((Binary/total)*100)
#sizes.append((Text/total)*100)
#sizes.append((Xml/total)*100)
#sizes.append((Zip/total)*100)

plt.bar(y_pos, total_count, align='center', alpha=0.5,)
plt.xticks(y_pos, file_extension,rotation = 'vertical')
plt.ylabel('file_formats')
plt.title('count of all file format')
 
plt.show()
