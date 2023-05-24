import linecache as lc

#raw_input is used as Python 2 was used, this is now deprecated and input should be used instead if using a later version of Python
file_name = raw_input("Enter the name of the file(with extension): ")

line_num = input("Enter the line number: ")

data = lc.getline(file_name, int(line_num)).strip()

output = open('line_' + str(line_num) + '_'  + str(file_name), "w")

output.write(data)

output.close()
