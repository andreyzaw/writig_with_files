def count_line_fail(file_name):
# Counting the number of lines in a file
    with open(file_name, encoding="utf-8") as f:
        line_file = f.readlines()
        return len(line_file)

def sort_files(list_file_names):
    dict_files = {}
# Creating dict {fail_name: count_line}
    for fail_name in list_file_names:
        dict_files[fail_name] =  count_line_fail(fail_name)
# Sorting dict
    sorted_dict = {}
    for key in sorted(dict_files, key=dict_files.get):
        sorted_dict[key] = dict_files[key]
    return sorted_dict

def write_in_file(file_name, sorted_file):
    for current_file_name, count_line in sorted_file.items():
        with open(file_name, 'a', encoding="utf-8") as f_result:
# Recording of service information
            f_result.write(f' {current_file_name}\n')
            f_result.write(f'{count_line}\n')
# Reading file and writing in result file
            with open(current_file_name, encoding="utf-8") as f_current:
                lines_file = f_current.readlines()
            f_result.writelines(lines_file)
            f_result.write(f'\n')
    return

dict_sort_files = sort_files(["sorted/1.txt", "sorted/2.txt", "sorted/3.txt"])
write_in_file("sorted/result.txt", dict_sort_files)