os.chdir(directory)
os.chdir('_vars')
os.system(copy_local + ' generic generic.py')
os.system(copy_local + ' generic generic.r')
os.system(copy_local + ' project project.py')
os.system(copy_local + ' project project.r')
os.system(copy_local + ' user user.py')
os.system(copy_local + ' user user.r')
os.chdir(directory)