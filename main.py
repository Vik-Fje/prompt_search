import msvcrt
import sys

def match_search(search_term, data):
	'''
	Args:
		search_term (str):
		data (list)
	
	'''
	
	for term in data:
		match = False
		if len(search_term) <= len(term):
			for i in range(len(search_term)):
				if term[i].lower() == search_term.lower()[i]:
					match = term
				else:
					match = False
					break
		
		if match:
			break
			
	return match
	
def get_data(file_name):
	with open(file_name, 'r') as f:
		lines = f.readlines()
		data = {}
		
		for line in lines:
			split_data = line.replace('\n', '').split('\t')
			data[split_data[0]] = split_data[-1]
	
	return data
	
def search_line():
	''''''
	
	# Test data
	
	data = ['super', 'test', 'long stuff', 'what, is .', '!!']
		
	match 			= False
	last 			= ''
	partial_match 	= False
	clear_search 	= False
	
	print '\n'*50
	print '-'*76
	# Header line 1
	search_header =  'Partial'.ljust(40)
	search_header += '|Draftsim'.ljust(10)
	search_header += '|Search'
	print search_header
	# Header Line 2
	search_header =  'match'.ljust(40)
	search_header += '|score'.ljust(10)
	search_header += '|text'
	search_header += '\n'
	search_header += '-'*76
	print search_header
	
	while not match:
		# User input
		if clear_search:
			input = msvcrt.getch()
			input 	= ''
			last 	= ''
			clear_search = False
		else:	# This is needed due to when DELETE is called, getch bugs
			input = msvcrt.getch()
		
		# Confirm match with ENTER
		if input == '\r':
			match = True
			break
		
		# Exit with ESC
		if input == '\x1b':
			partial_match = False
			break
		
		#Clear search with DELETE
		if input == '\xe0':
			clear_search = True
		elif input == '\x08':#Remove last character with backspace
			last = last[0:-1]
		else:
			last += input
		
		# Search for partial match
		partial_match = match_search(last, data)
		
		if partial_match:
			match_str = partial_match
			score_str = data[partial_match]
		else:
			match_str = ''
			score_str = ''
		
		# Text
		match_text  = ('%s'%(match_str)).ljust(40)
		score_text 	= ('%s'%(score_str)).ljust(9)
		search_text = '%s'%(last)
		
		output_text = '\r%s|%s|%s'%(match_text,score_text, search_text)
		
		#Flush line
		sys.stdout.write('\r%s'%(' '*60))
		
		# Refresh search line
		sys.stdout.write(output_text)
		# print last
		
		
		
	return partial_match


if __name__ == "__main__":
  search_line()	
