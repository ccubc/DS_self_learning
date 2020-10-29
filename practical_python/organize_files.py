import os

def get_file_list_name_startswith(prefix_str):
	# within a folder, create a list with filenames starting with specific string
	file_name_list = [filename for filename in os.listdir('.') if filename.startswith(prefix_str)]
	return file_name_list


def concat_files_between_texts(start_str, end_str, input_list, output_name):
	# for a list of files, concat the content between "start_str" and "end_str" in each of them
	for f in input_list:
		with open(f) as infile, open(output_name, 'a') as outfile:
			outfile.write('\n\n')
			copy = False
			for line in infile:
				if start_str in line.strip():
					copy = True # starting line found
					continue
				elif end_str in line.strip():
					copy = False # ending line found
					continue
				elif copy: # copy = True: this line is the target line
					outfile.write(line)
	return outfile


def create_folder_move_files(prefix_str, move_path):
	# within current folder, look for filenames starting with prefix_str, and move them to move_path
	os.makedirs(os.path.dirname(move_path), exist_ok=True)
	list_move_file = [filename for filename in os.listdir('.') if filename.startswith(prefix_str)]
	print(list_move_file)
	for f in list_move_file:
		os.rename(f, move_path+'/'+f)


# unit test
if __name__=='__main__':
	print(get_file_list_name_startswith('get'))
	create_folder_move_files('get', 'move/')


