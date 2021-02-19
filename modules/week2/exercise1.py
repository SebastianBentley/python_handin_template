import csv
import argparse

#1. Create a python file with 3 functions:

#A. def print_file_content(file) that can print content of a csv file to the console
def print_file_content(file):
    with open(file) as f:
        print(f.read())



#B. def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as f:
        for item in lst:
            for elm in item:
                f.write(elm + '\n')


            
# a.rewrite the function so that it gets an arbitrary number of strings instead of a list
def write_list_to_file2(output_file, *words):
    with open(output_file, 'w') as f:
        for item in words:
            f.write(item + '\n')



#C. def read_csv(input_file) that take a csv file and read each row into a list
def read_csv(input_file):
    with open(input_file) as f:
        lst = []
        content = f.readlines()
        for line in content:
            lst.append(line.strip())
            
    return lst



#2. Add a functionality so that the file can be called from cli with 2 arguments
parser = argparse.ArgumentParser(description='Week 2 Exercise 1')

#A. path to csv file
#parser.add_argument('csv_file', help="a csv_file")

#B. an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
#parser.add_argument('-f', '--file', default='printMe', help='Optional file written to from csv_file')
#args = parser.parse_args();

#if(args.file == 'printMe'):
#    print_file_content(args.csv_file)
#else:
#    write_list_to_file(args.file, read_csv(args.csv_file))

#3. Add a --help cli argument to describe how the module is used
# Already built in