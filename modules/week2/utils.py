import os

# """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
def get_file_names(folderpath,out='output.txt'):
    entries = os.listdir(folderpath)
    for entry in entries:
        with open(folderpath+out, 'a') as file_obj:
            file_obj.write(entry + '\n')


# """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
def get_all_file_names(folderpath,out='output.txt'):
    for root, subdirs, files in os.walk(folderpath):
        with open(folderpath+out, 'a') as file_obj:
            for file in files:
                file_obj.write(file + '\n')




# """takes a list of filenames and print the first line of each"""
def print_line_one(file_names):
    for file in file_names:
        with open(file) as f:
            line = f.readlines()
            print(line[0].strip())

# """takes a list of filenames and print each line that contains an email (just look for @)"""
def print_emails(file_names):
    for file in file_names:
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                if('@' in line):
                    print(line)

# """takes a list of md files and writes all headlines (lines starting with #) to a file"""
def write_headlines(md_files, out='output.txt'):
    for file in md_files:
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                if('#' in line):
                    with open(out, 'a') as o:
                        o.write(line)



# Make sure your module can be called both from cli and imported to another module Create a new module that imports utils.py and test each function.