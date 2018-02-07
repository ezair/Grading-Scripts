'''
Author: Eric Zair
File:	grade.py
Description:	This file grades 203 Hw Assignments.
				Make sure that you give this file the proper
				name for grading(as in the proper assignment
				name when prompted for it) Do NOT include the 
				file extension(.java).
				IMPORTANT:
							Make sure that this file is in the proper
							folder. This script must be put into the folder
							that contains the zip file of all student assignmnets
							and the main program.
							Do not have anything put the one zip file and this program
							in that folder.
'''

import os
import shutil
from os import system
from pyunpack import Archive	#run the following command in order to install the dependencies.
								#sudo apt-get install pyunpack && sudo apt-get install patool


'''
Get the name of the assingment the students
are working on.
Return type: String(name of the assignment)
'''
def getAssignmentName():
	assignment_name = raw_input("Enter the name of the assignment(do not include the file extension): ")
	if '.' in assignment_name:
		print("DO NOT INCLUDE THE FILE EXTENSION")
		return getAssignmentName()
	return assignment_name


'''
Unzip the folder from moodle that contains
all of the student's assignments.
After the extraction, delete the zip file.
Return type: void
'''
def unzip():
	#The zip folder downloaded from moodle that must be unziped
	zip_file = ""
	for file in os.listdir("."):
		if ".zip" in file:
			zip_file = file
			break
	Archive(zip_file).extractall(".")
	#After unzipping the file, rm it from the directory.


'''
Create a log file that will be used to store comments
about students assignments.
Return type: void
'''
def createLogFile():
	#log file that will be used to write comments about the users assignment.
	if not os.path.exists("output.log"):
		with open("output.log", "a") as log_file:
			pass


#------------------------------------------------------------------------------------------
def main():
	#grab the assignment name(without the file extension)
	assignment_name = getAssignmentName()

	#Unzip the zip file to get assignments and then delete it after.
	unzip()

	#Make a log file to store student assignmnet comments in.
	createLogFile()

	for folder in sorted(os.listdir(".")):
		#get the zip file to extract and run
		if os.path.isdir(folder):
			zip_file = os.listdir(folder)[0]

			print "it works here"
			#extract each individual folder.
			if (zip_file.endswith(".zip")) or (zip_file.endswith(".rar")) or (zip_file.endswith(".tar")) or (zip_file.endswith(".gz")):
				Archive(folder + "/" + zip_file).extractall(".")

				#run all of the java programs.
				student_name = folder[0 : folder.index(',')]
				print("The following assignment is " + student_name + "'s.\n\n")
				
				#compile java programs.
				system("javac " + assignment_name + ".java")
				
				#if there is no class file, then it means that the program did not compile.
				if assignment_name + ".class" not in os.listdir("."):
					#write to the log file that the assignment did not compile.
					with open("output.log", 'a') as log_file:
						log_file.write(student_name + ":\n\t did not compile\n\n")
					
				#It Compiled. Run the java program
				else:
					system("java " + assignment_name)

					#have grader write a comment about the assignment to the log_file
					comment = raw_input("Grader's Comment: ")
					with open("output.log", 'a') as log_file:
						log_file.write(student_name + ":\n\t" + comment + "\n\n")
	
	#exit the program.
	print("Have a nice day, Grader!")


#Call main-----------------------------------------------------------------------------------
if __name__ == "__main__":
    main()