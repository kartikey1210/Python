import pandas as pd

# The file we have taken is a comma separated values
data = pd.read_csv("student.txt", header=0)

# column_list = list(data.columns)
out_file = {}
marks = {}

'''Open the template file to get the lables, for e.g id, name, subject, marks'''
template = open("template.txt", "r")
# remove all the whiteapces and special characters
# template_val = template.readline().replace("<","").replace(">","").replace("{","").replace("}","").split(",")
# extracting out the lables for the output
# lables = [i.split(":")[0] for i in template_val]

value = template.readline().replace(" ", "")

# Find the separator for the data that has been provided in the tamplate.txt file
sep_index = value.find(">") + 1
sep_value = value[sep_index]

ref_dict = value.replace("{", "").replace("}", "").split(sep_value)

# storing the symbol for the corresponding labels that will reference the data
symbols = [i.split("<") for i in ref_dict]
pair_symbol = {i[0][0:-1].lower(): i[0][-1] for i in symbols}

'''  for each row we will read inputs and then we will push the result into the file'''

for i in data.index:
    filename = str(data['name'][i]) + "." + str(data['rollno'][i]) + ".txt"
    '''Open the file in a append mode as we will be appending the results for duplicate student'''
    with open(filename, 'a') as file:

        ''' this loop is for categorizing the column name according to it's values '''
        for j in pair_symbol.keys():
            if j.lower() == "id":
                out_file[j.upper()] = data.rollno[i]
            else:
                out_file[j.upper()] = data[j.lower()][i]
        name = filename
        marks_ind = out_file['MARKS']
        if name in marks.keys():
            marks[name] = marks_ind + marks[name]
        else:
            marks[name] = marks_ind
        file.write('{')
        for k, v in out_file.items():
            if k == 'rollno':
                file.write('Id ' + pair_symbol['id'] + " " + str(v) + " " + sep_value + " ")
            else:
                file.write(str(k) + " " + pair_symbol[k.lower()] + " " + str(v) + " " + sep_value + " ")
        file.write('}\n')

# Here we are taking total marks for each student mapped to their files
for key, values in marks.items():
    with open(key, 'a') as file:
        file.write(40 * ' ' + 'Total: ' + str(values))
