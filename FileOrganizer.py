########################################################################
#
# File Name :   FileOrganizer.py
# Description:  Automation Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
#
########################################################################
"""
File Copy Successfully
Total Number of .txt Files Moved are :  3

"""

import sys
import os
import shutil

def MoveFileExtension(path):
    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)
    
    flag = os.path.exists(path)
    if(flag == False):
        print("Directory Not Found")
        return

    flag = os.path.isdir(path)
    if(flag == False):
        print("Its File Not Directory")
        return

    
    fd = open("Demo4.txt",'a')
    fd.write("\n\n"+"Files Moved From "+path+" to their respective Directories "+"\n")

    iCount = 0



    for FolderName, SubFolderName , FileName in os.walk(path):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)

            name,ext = os.path.splitext(fname)


            Dir_Name = path+ext
            path2 = os.path.join(FolderName,Dir_Name)

            flag = os.path.exists(path2)

            if(flag == False):
                os.mkdir(path2)
                shutil.move(fname,path2)
                iCount = iCount + 1
               
                fd.write(ext+" Files Copied From "+path+" to "+Dir_Name+"\n")

            else:
                shutil.move(fname,path2)
                iCount = iCount + 1

                fd.write(ext+" Files Copied From "+path+" to "+Dir_Name+"\n")

    fd.write("Total Number of "+ext+" Files Copied are :  "+str(iCount)+"\n")

    fd.close()

    print("Total Number of "+ext+" Files Copied are :  "+str(iCount))



   
def main():

        if(len(sys.argv) == 2 ):
            if(sys.argv[1] == "-h" or sys.argv[1] == "-H"):
                print("This Script Accepts 3 Arguments")
                print("Usage : ScriptName DirectoryName ")
                print("Example : Demo.py Demo.txt .txt")
                return
            elif(sys.argv[1] == "-u" or sys.argv[1] == "-U"):
                print("This Script moves  the File of same Extension to their respective Directories and create its log file and returns Number of Files with Given Extension has been renamed")
                print("Usage : ScriptName DirectoryName Extension")
                print("Example : Demo.py Demo.txt .txt")
                return


            else:
                path = sys.argv[1]

                MoveFileExtension(path)


        else:
            print("Invalid Arguments")
            return

    

if(__name__ == "__main__"):
    main()