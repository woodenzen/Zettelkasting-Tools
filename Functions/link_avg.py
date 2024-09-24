import os

def count_and_average_links(directory):
	md_file_count = 0
	total_link_count = 0
	
	for item in os.listdir(directory):
		if item.endswith('.md'):
			md_file_count += 1
			file_path = os.path.join(directory, item)
			try:
				with open(file_path, 'r', encoding='utf-8') as file:
					content = file.read()
					link_count = content.count(" [[")
					total_link_count += link_count
					# print(f"{item}: {link_count} occurrences of ' [['")
			except Exception as e:
				print(f"Error reading {file_path}: {e}")
	
	if md_file_count > 0:
		average_links = round(total_link_count / md_file_count, 1)
		print(f"Average ' [[' per .md file: {average_links}")
	else:
		print("No .md files found.")

# Example usage
directory_path = '/Users/will/Dropbox/zettelkasten'
count_and_average_links(directory_path)