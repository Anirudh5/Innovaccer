import sys,os
import heapq
import commands
import string

files = []
ext_dict = {}

def find_files(root):
	
	"""
	Finds all the files recursively given the root directory
	"""
	
	dirs = []
	try:
		dirs += [ os.path.join(root, f) for f in os.listdir(root) ]
	except OSError:
   		try :
			files.append((os.path.getsize(root), root))
		except OSError:
			pass

	for Dir in dirs :
		find_files(Dir)

def get_top_N(root,n):
	
	"""
	Returns top n files based on their sizes
	"""

	global files
	find_files(root)
	heapq.heapify(files)
	ret = heapq.nlargest(n,files)
	files = []
	return ret

def get_files_with_extensions(root):
	
	"""
	Gets a dictionary of extension : [file]
	"""
	
	find_files(root)
	global files
	for filesize,filepath in files:
		filename, file_extension = os.path.splitext(filepath)
		
		filename = filename.replace(' ','\ ')
		filepath = filepath.replace(' ','\ ')

		if file_extension == '' :
			file_extension = '.EMPTY'
		if file_extension not in ext_dict :
			ext_dict[file_extension] = []
		
		ext_dict[file_extension].append(filepath)

def make_directory(path,dirname):
	
	"""
	Makes a directory given path and directory name
	"""

	directory_path = path + '/' + dirname
	command = 'mkdir ' + directory_path
	
	try :
		st = commands.getstatusoutput(command)
	except Exception:
		raise

def movefile(destpath,filename,sourcepath):
	
	"""
	Moves a file to the destination path
	"""

	command = 'mv ' + filename + ' ' + destpath
	
	try :
		st = commands.getstatusoutput(command)
	except Exception:
		raise

def arrange_desktop_files(documentspath,desktoppath):
	
	"""
	Cleans up the desktop by moving files into respective subfolders
	in the documents folder based on their extension.
	Ignore '.desktop' files extensions as they are shortcut files.
	Files with no extensions are moved into EMPTY folder.
	"""

	print "\n\n------------------Arranging Your Desktop-------------------\n\n"

	for ext in ext_dict :
		if ext != 'desktop':
			make_directory(documentspath,ext[1:].upper())
			for file in ext_dict[ext]:
				print file , "----------------------->" , documentspath+'/'+ext[1:] , '\n'
				movefile(documentspath+'/'+ext[1:].upper(),file,desktoppath)



def printfiles(Files):
	print "\n\n------------------Largest 10 Files in your home directory-------------------\n\n"
	for filesize,file in Files :
		print file , filesize

	print "\n\n"

if __name__ == "__main__":
	
	#Getting current user name
	current_user = commands.getstatusoutput('whoami')[1]
	
	#Generating paths to various directories
	desktop_path = '/home/' + current_user + '/Desktop'
	documents_path = '/home/' + current_user + '/Documents'
	
	try :
		home_path = sys.argv[1]
	except Exception:
		home_path = '/home'

	#Getting top 10 files in our home directory
	printfiles(get_top_N('/',10))

	# Arranging desktop files into documents folder according to extensions
	get_files_with_extensions(desktop_path)
	arrange_desktop_files(documents_path , desktop_path)





