---------------------------------------Innovaccer Infrastructure Engineering Assignment-----------------------------------


**Description :-

The python script in the file "innovaccer.py" performs two tasks 
	
- Gets the largest 10 files in the home directory of the current user
- Arranges users desktop by moving all files from desktop to documents folder into respective subfolders based on extensions

            

**Instructions For Running The Script :-

You can run the script as   
	
python innovaccer.py path_to_directory

Default value of path_to_directory is set to '/home' , but can be specified if you want top 10 files in some other directory.

Desktop directory is set as "/home/username/Desktop"
Documents directory is set as "/home/username/Documents"

           
 **Bonus work :-

 - Added support for complex file names which include spaces in the filename.
 - While cleaning the desktop it also considers all the folders and subfolders while collecting files based on extensions instead of just taking the first level files.


           
 **Special Instructions :-

 - The script is developed for Unix platform.

 - Please do not specify path_to_directory as '/' which is the root directory as it may take a lot of time and can also result in erros in case there are a large number of symbolic links to a particular file.

