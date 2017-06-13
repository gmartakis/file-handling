"""
Author: Ioannis Martakis
Python: program File-handling
Version 1.0
"""
import csv
import os
import codecs
import shutil


rootdir = os.path.expanduser("~development\python")
destdir = os.path.expanduser("~development\csv")


#Storing the first rows from the csvs
csv1 = []
csv2 = []
csv3 = []
name = ''
counter=0
filename='00'
counterPlus=0
#counterPdf=0

#copy files from source to destination folder
def copy(src, dest):
    shutil.copy(src, dest)

def column(matrix, i):
    return [row[i] for row in matrix]

def find(needle,haystack):
  if needle == haystack: return []
  # Strings are iterable, too
  if isinstance(haystack,str) and len(haystack)<=1: return None
  try:
    for i,e in enumerate(haystack):
      r = find(needle,e)
      if r is not None:
        r.insert(0,i)
        return r
  except TypeError:
    pass
  return None

text = []
pdf= []

def copyPdf(rootdir, destdir):
     for subdir, dirs, files in os.walk(rootdir):
        counterPdf=0
        for file in files:
            if file.endswith(".pdf"):
                f=codecs.open(rootdir+file, 'r', 'utf-8')
                filename_split = os.path.splitext(file) # filename and extensionname (extension in [1])
                filename_zero = filename_split[0]
                filename_ext = filename_split[1]
                split_filename = filename_zero.split('_')
                newname = filename+str(counterPdf+1)+filename_ext
                if(os.path.exists(destdir+str(split_filename[1])+'\\')):
                  0
                else:
                  os.makedirs(destdir+str(split_filename[1])+'\\')
                copy(rootdir+file, destdir+str(split_filename[1]))
                counterPdf+=1

#remove subdirectories and files if they exist
def remove(destdir):
    for dir,subdir,files in os.walk(destdir):
        #print(dir + " has crossed limit, " + "total files: " + str(subdir) + str(len(files)))
        for x in files:
          if os.path.isfile(os.path.join(dir, x)):
            shutil.rmtree(os.path.join(dir))

#copy from csv files the first row "company name" and create the corresponding folders
#Then copy files to destination folder
def create(counterPlus, rootdir, destdir, counter, text):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(".csv"):
                f=codecs.open(rootdir+file, 'r', 'utf-8')
                filename_split = os.path.splitext(file) # filename and extensionname (extension in [1])
                filename_zero = filename_split[0]
                filename_ext = filename_split[1]
                try:
                  reader = csv.reader(f)
                  for row in reader:
                     if len(row) <= 1:
                       pass
                     else:
                         csv1.append(row[0])
                         if len(row) <= 1:
                            pass
                         else:
                             text = csv1[::3]
                             #print(text)
                             if(os.path.exists(destdir+str(text[counterPlus])+'\\')):
                               0
                             else:
                                os.makedirs(destdir+str(text[counterPlus])+'\\')
                             copy(rootdir+file, destdir+str(text[counterPlus]))
                             if(os.path.isfile(destdir+str(text[counterPlus])+'\\'+file)):
                              0
                             else:
                              os.rename(destdir+str(text[counterPlus])+'\\'+file, destdir+str(text[counterPlus])+'\\'+filename+str(counterPlus+1)+filename_ext)
                             counter+=1
                finally:
                    f.close()
                counterPlus+=1

def rename(destdir):
    for dir,subdir,files in os.walk(destdir):
            your_limit=0
            pdfCounter=0
            for x in files:
              if x.endswith(".csv"):
                filename_split = os.path.splitext(x) # filename and extensionname (extension in [1])
                filename_zero = filename_split[0]
                filename_ext = filename_split[1]
                newname = filename+str(your_limit+1)+filename_ext
                if os.path.isfile(os.path.join(dir, x)):
                    os.rename(os.path.join(dir, x), os.path.join(dir, newname))
                your_limit+=1
              elif x.endswith(".pdf"):
                filename_split = os.path.splitext(x) # filename and extensionname (extension in [1])
                filename_zero = filename_split[0]
                #print(filename_zero)
                filename_ext = filename_split[1]
                #print(filename_ext)
                newname = filename+str(pdfCounter+1)+filename_ext
                if os.path.isfile(os.path.join(dir, x)):
                    os.rename(os.path.join(dir, x), os.path.join(dir, newname))
                pdfCounter+=1

#call the remove function to remove the Dirs if the exist
remove(destdir)
#Copy files from source to destinations folders
create(counterPlus, rootdir, destdir, counter, text)
#copy PDF files
copyPdf(rootdir, destdir)
#rename files in subdirectories with counters
rename(destdir)
