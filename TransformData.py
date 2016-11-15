class TransformData:

	def __init__(self):
		self._path = "/home/deepika/FINAL PROG/ALLIMAGING/img01.txt"
		self.infile = open(self._path,"r")
		self.outfile = open("/home/deepika/FINAL PROG/ALLIMAGING/sorted.csv","w")
		self.__read_file()
       
	def __read_file(self):
   		for record in self.infile:
   			self.__process_data(record)
   			self.combine_data()
   	

	def __process_data(self,record):
		if record != '\n':
			strings = record.split()
			self.permissions = strings[0]
			self.charecters = list(strings[0])
			if self.charecters[0] == '-':
				self.links = strings[1]
				self.user = strings[2]
				self.group = strings[3]
				self.memory = strings[4]
				self.month = strings[5]
				self.date = strings[6]
				self.time = strings[7]
				self.fname = strings[8]

	def combine_data(self):
		if self.charecters[0] == '-':
			record = self.permissions + "," +self.links +"," + self.user + "," + self.group + "," +self.memory+ "," +self.month+","+self.date +"," +self.time+","+self.fname
			self.outfile.write(record)
			self.outfile.write("\n")

T1 = TransformData()
