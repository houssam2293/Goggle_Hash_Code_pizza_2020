import argparse
import re

def get_args():
	'''Gets the arguments from the command line.'''
	parser = argparse.ArgumentParser("Run the script on an input file")
	
	# -- Create the descriptions for the commands
	i_desc = "The location of the input file"
	o_desc = "The location where to output the file"
	
	# -- Add required and optional groups
	parser._action_groups.pop()
	required = parser.add_argument_group('required arguments')
	optional = parser.add_argument_group('optional arguments')
	
	# -- Create the arguments
	required.add_argument("-i", help=i_desc, required=True)
	optional.add_argument("-o", help=o_desc, default='')
	args = parser.parse_args()
	
	return args


def get_pizzas(args):
	input = open(args.i,"r")
	
	list=re.split("\s",input.read())
	list.remove("")
	input.close()
	M = list[0]
	N = list[1]
	list = list[2:]
	
	pos=[]
	sum=0
	mx_pos=0
	for i in range(1, len(list), 1):
		if (int(list[i])+int(list[i-1])>int(M)):
			mx_pos=i-1
		else:
			mx_pos=i
	
	
	for i in range(mx_pos, -1, -1):
		if(sum+int(list[i])<=int(M)):
			sum+=int(list[i])
			pos.append(i)
		else:
			continue
	pos.sort()
	exist=False
	if(args.o!=""):
		f = open(args.o+".out", "w")
	else:
		f = open(args.i[:-3]+".out", "w")
		exist=True
	f.write("%d\n"%(len(pos)))
	for x in pos:
		f.write("%s "%(x))
	f.close()
	
	if(exist):
		f = open(args.i[:-3]+".out", "r")
		print(f.read()) 
	else:
		f = open(args.o+".out", "r")
		print(f.read()) 
		
		
	
	
	
def main():
    
	args = get_args()
	get_pizzas(args)

if __name__ == "__main__":
    main()
