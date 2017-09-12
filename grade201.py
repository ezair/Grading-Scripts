'''
Author: Eric Zair
File:	grade.py
Description:	This file grades 201 Hw Assignments.
				Make sure that you give this file the proper
				name for grading(as in the proper assignment
				name when prompted for it).
				IMPORTANT:
							Make sure that this file is in the proper
							folder. This script must be put into a folder
							where all of the java files are.
'''

import os
import shutil
from os import system


'''
This function returns a list string containing
the name of all java files in a given path.
Parameters: string path (path to java files).
return type: list of strings (contains filenames).
'''
def getJavaFiles(path):
	files = os.listdir(path)
	for file in files:
		if not file.endswith(".java"):
			list.remove(file)
	return files



'''
Creates the required directories and files if they do not exist.
The dirs required are (Graded/, Failed/, Assignments, and output.log)
The function then moves all java files in the current dir to Assignments/
parameters: none.
return type: void.
'''
def createRequirements():
	if not os.path.exists("Failed/"):
		os.makedirs("Failed/")

	if not os.path.exists("Graded/"):
		os.makedirs("Graded/")

	if not os.path.exists("Assignments/"):
		os.makedirs("Assignments/")

	if not os.path.exists("output.log"):
		with open("output.log", "a") as log_file:
			pass


'''
Move all java files in a given dir
parameters: string path(Where you wanna grab the java file)
			string location(Where you wanna move the java files)
return type: void
'''
def moveAllJavaFiles(path, location):
	for file in os.listdir(path):
		if file.endswith(".java"):
			shutil.move(file, location)

'''
Checks to see if a class file exists in a given dir.
Returns True if one of the files in the given dir is a class file.
Parameters: string filename (name of the class file that we are looking for).
return type: boolean
'''
def classFileExists(assignment_name):
	classfile =  assignment_name + ".class"
	return os.path.exists("./" + classfile)


'''
Ask the user for the name java file
that is the assignment to be graded.
file extention is not to be given.
If the file extention is given, the function
is recursively re-run.
Parameters: none.
return type: string (filename given by the user)
'''
def nameOfAssignment():
	filename = raw_input("Enter the filename for the assignment(Do NOT INCLUDE FILE EXTENTION): ")
	if "." in filename:
		print "Do Not Include The File Extention!"
		nameOfAssignment()
	else:
		#system("clear")
		return filename


'''
Run all java programs and check to see if they work.
Prints out the name of the file above before running it.
After the java program ends, user is prompted for comments.
Comments are written to a file named "output.log"
Parameters:	string files (path to where java files exists).
'''
def runJavaPrograms(files, assignment_name):
	for file in files:
		#Print out whose file it is.
		print "\nThe following file is " + file + "\n\n"

		#Change the name of file to a valid name so it compiles properly.
		java_file = assignment_name + ".java"
		shutil.move("Assignments/" + file, "./" + java_file)
		#Compile the java program.
		system("javac " + java_file)

		#Run it and then add a comment about the assignment.
		if classFileExists(assignment_name):
			#Run the class file.
			system("java " + assignment_name)

			#Remove the class file after it is run.
			#move the java program back to its original dir.
			os.remove(assignment_name + ".class")
			shutil.move(java_file, "Graded/" + file)

			#Ask grader to write comment about file.
			#Write the comment to output.log file.
			comment = raw_input("Enter a comment about the assingment: ")
			with open("output.log", "a") as log_file:
				log_file.write("\nComment for " + file +":\n\t" + comment + "\n")		

		#Write to log file, that assignment did not compile.
		#move this file back to its name, and move it to Failed/.
		else:
			with open("output.log", "a") as log_file:
				log_file.write("\n" + file + " \n\tdid not compile\n")
			shutil.move(java_file, "Failed/" + file)


#Main_____________________________________________________________________
def main():

	#Ask the grader for the name of the java assignment(without the file extention).
	assignment_name = nameOfAssignment()

	#create all requirements for program to work.
	createRequirements()

	#Move all of students java files to from here to Assignments/ dir.
	moveAllJavaFiles(".", "Assignments/")

	#Get a list of all java programs in the Assignments/ dir.
	#Files are sorted.
	files = sorted(getJavaFiles("Assignments/"))

	#Run all of the students java programs.
	runJavaPrograms(files, assignment_name)


#Run main
if __name__ == "__main__":
	main()
