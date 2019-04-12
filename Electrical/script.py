import os
import pandas as pd 

def make_folders(filename):
	data = pd.read_csv(filename)
	names = data["Names"]
	for name in names:
		os.mkdir(name)
		os.chdir(name)
		# linux users do touch filename .txt
		os.system("echo$null >> "+ name+".txt")
		f = open(name+".txt", "w+")
		f.write("Hi ! I am "+ name)
		f.close()
		os.chdir("../")

make_folders("elec.csv")