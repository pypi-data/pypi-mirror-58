
import os, re, shutil

def read(path, params, master_dict={}):
	all_files = [] # That which will be returned

	# Preprocess parameters
	if len(params) == 0:
		curr_param = '*' # Process all files
	else:
		curr_param = params[0] # Filter by regular expression

	for curr_path_head in os.listdir(path):
		curr_attrs = master_dict.copy()

		# Are we reading attributes?
		if type(curr_param) == tuple: # Yes
			pattern = curr_param[0]
			attrs_to_read = curr_param[1:]
		else: # No
			pattern = curr_param
			attrs_to_read = []
		matches = re.findall(pattern, curr_path_head)
		if len(matches) == 0:
			continue # This one doesn't match, go to the next file/dir in path
		else:
			if len(attrs_to_read) > 0: # Read attributes
				matches = matches[0]
				if type(matches) == str:
					matches = (matches,)
				for idx in range(len(matches)):
					curr_attrs[attrs_to_read[idx]] = matches[idx] # Add attributes
			curr_path = os.path.join(path, curr_path_head)
			if os.path.isdir(curr_path): # Recursion if we're currently on a folder
				all_files += read(curr_path, params[1:], master_dict=curr_attrs)
			else: # Bottom of file hierarchy
				all_files += [{
					'path': curr_path,
					'attrs': curr_attrs.copy()
				}]
	return all_files # List of dicts

def translate(all_files, translation, direction='forward'):
	if direction != 'forward': # Swap values and keys
		translation = {attr: {new: old for old, new in entry.items()} for attr, entry in translation.items()}
	for attr in translation.keys():
		for fileidx in range(len(all_files)):
			curr_val = all_files[fileidx]['attrs'][attr]
			if curr_val in translation[attr]:
				new_val = translation[attr][curr_val]
				all_files[fileidx]['attrs'][attr] = new_val
	return all_files

def write(all_files, path, params, disp=False, key='c'):
	destinations = []
	for file in all_files:
		curr_destination = ''
		for param in params:
			if type(param) == str: # We are adding a static name to the path
				curr_path_head = param
			else: # We are adding a formatted name to the path
				curr_path_head = param[0] % tuple(file['attrs'][attr] for attr in param[1:])
			curr_destination = os.path.join(curr_destination, curr_path_head)
		curr_destination = os.path.join(path, curr_destination)
		if disp: # Let the user double check that the destination paths are ok
			print(curr_destination)
		if key != 'n': # We're actually commiting to creating new files
			os.makedirs(os.path.dirname(curr_destination), exist_ok=True)
			if key == 'c': # Copy and paste
				func = shutil.copy
			elif key == 'x': # Cut and paste
				func = shutil.move
			func(file['path'], curr_destination)
	return destinations