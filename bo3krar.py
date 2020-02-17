#!/usr/bin/python

import rarfile 
import optparse 
from threading import Thread

print ("STARTING BO3KZIP") 
def extractFile(rfile,password):
    try:
       rfile.extractall(pwd=password) 
       print "[+] Found password: " + password+"\n" 
    except:
        pass

def main(): 
    parser=optparse.OptionParser("%prog -f <Rar file> -d <Dictionary.txt> ") 
    parser.add_option("-f",dest="rar_name",type="string",help="Specify rar file") 
    parser.add_option("-d",dest="dictionary_name",type="string",help="Specify dictionary") 
    (options, args)=parser.parse_args()
    if(options.rar_name==None)|(options.dictionary_name==None):  
        print parser.usage
        exit(0)
    else: 
        rar_name=options.rar_name
        dictionary_name=options.dictionary_name

    rar_name=rarfile.RarFile(rar_name)
    passFile=open(dictionary_name)

    for line in passFile.readlines():
        password=line.strip("\n")
        t=Thread(target=extractFile,args=(rar_name,password))
        t.start()
    print "password not found" 
main()

