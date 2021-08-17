local = os.getcwd()
directory = local + swc + path + swc
os.chdir(directory)
text_write = open('_env/dir.r', 'w')
text_write.write('directory = "' + directory + '"\n')
text_write.write('setwd(directory)')
text_write.close()