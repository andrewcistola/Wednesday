file_README = open('README', 'w') # Open markdown file used to develop the report
file_README.write('# ' + project_title + '\n') # Report title
file_README.write('## ' + project_subtitle + ' ' + project_subject + '\n') # Descriptive title or subtitle
file_README.write('##### ' + project_author + '\n') # Report author
file_README.write(project_about + '\n') # About this file
file_README.write('For more information visit : ' + project_remote + '\n') # Primary reference
file_README.write('\n\n') # Section separator
file_README.close()