
import os,sys,stat
import shutil,subprocess,time


class historyManager(object):
    def __init__(self):
        self.command_history = []

		
    def push_command(self,cmd):
        self.command_history.append(cmd)
        
    
    def get_commands(self):
        return self.command_history
        
    
    def number_commands(self):
        return len(self.command_history)


class parserManager(object):
    def __init__(self):
        self.parts = []
		
    def parse(self,cmd):
        self.parts = cmd.split(" ")
        return self.parts


class commandManager(parserManager):
    def __init__(self):
        self.command = None


    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command

    #ls (directory listing)
    def ls(self):
        for dirname, dirnames, filenames in os.walk('.'):
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))
    
        for filename in filenames:
            print(os.path.join(dirname, filename))
    #ls flags
    def lsf(self,flag):
        files_info=[]
        for file_name in os.listdir('.'):
            file_stats=os.stat(file_name)
            file_info = [
            file_name,
            file_stats [stat.ST_SIZE],
            oct(stat.S_IMODE(file_stats.st_mode))[2:],
            time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_MTIME])),
            time.strftime("%m/%d/%Y %I:%M:%S %P",time.localtime(file_stats[stat.ST_ATIME])),
            time.strftime("%m/%d/%Y &I:%M:%S %p",time.localtime(file_stats[stat.ST_CTIME]))
            ]
            files_info.append(file_info)
        #long listing
        if(flag=='-l'):
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---- ----","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t\t{}\t\t{}\t\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        #ordered by mtime
        if(flag=='-m'): 
            files_info.sort(key=lambda x:time.strftime((x[3])))#sorts files_info.sort based on 3 item in list(Mtime)
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t\t{}\t\t{}\t\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        #ordered by size
        elif(flag=='-s'):
            files_info.sort(key=lambda x:time.strftime((x[2])))#sorts files_info.sort based on 3 item in list(Size)
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t\t{}\t\t{}\t\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        #ordered by atime
        elif(flag=='-a'):
            files_info.sort(key=lambda x:time.strftime((x[4])))#sorts files_info.sort based on 3 item in list(Atime)
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t\t{}\t\t{}\t\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        #ordered by ctime
        elif(flag=='-c'):
            files_info.sort(key=lambda x:time.strftime((x[5])))#sorts files_info.sort based on 3 item in list(Ctime)
            
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t\t{}\t\t{}\t\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))


    #cat command(lists a file)
    def cat(self,file):
        f = open(file,'r')
        print(f.read())
    
    #mv command(renames a file)	
    def mv(self,file1,file2):
        os.rename(file1,file2)
        print("file has been renamed")

	
    #chmod command(changes permissions)
	def chmod(self,file):
		os.chmod("file1.txt",0777)
		print("changed mode successfully")
    
	
	#rm command(removes files)
    def rm(self,file):
        if os.path.exists(file):
            try:
                os.remove(file)
                print("removed successfully")
            except IOError as e:
                print("file doesnot exist")
    

    #wc command(counts the number of words,lines,charecters)
	def wc(self,file):
        lines=0
        words=0
        chars=0	
        with open(file,'r')as fileObject:
           for i in fileObject:
              wordsFind=i.split
              lines += 1
              words += len(wordsFind)
              chars += len(i)
              print("lines:",lines)
              print("words:",words)
              print("characters:",chars)
    
                
    #cd command(changes the directory)	
    def cd(newDir):
		try:
			os.chdir(newDir) #given directory
		except:
			print("could find the folder entered")
		if newDir[0]=="..":
			os.chdir(os.newDir.oldpwd(newDir)) #previous directory
		elif newDir[0]=="~":
			os.chdir(os.newDir.expanduser(newDir)) # open home directory

    #cp command(copies content from one file to another)
	
    def cp(self,src,dest):
        if(os.path.isfile(dest)):
            shutil.copyfile(src, dest)
            print("copy success")
        else:
            file = open0('dest','w+')
            shutil.copyfile(src, dest)
            print("copy success")

    #history command(shows the command history)
    def history(self):
        s=0
        history=self.get_commands()
        for cmd in commandlist:
            s += 1
            ouput = str(s)+ " " +cmd
            print(output)
		
        

class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0
        
 
    def runShell(self):
        number_commands = 0
        while True:
            self.input = input("parser-$ ")         # get command
            self.history.push_command(self.input)   # put in history
            parts = self.commands.run_command(self.input)
            print(parts)
            #print(parts)
            for k in parts:           
                if k == 'cat':
                    filename=(parts[1])
                    self.commands.cat(filename)
                elif k == 'rm':
                    file=(parts[1])
                    self.commands.rm(file)
                elif parts[0]=='ls':
                    if(len(parts)==1):
                        self.commands.ls()
                    elif (len(parts)==2):
                        self.commands.lsf(parts[1])
                    else:
                        print("more arguments for ls command")
                elif k == 'mv':
                    file1=(parts[1])
                    file2=(parts[2])
                    self.commands.mv(file1,file2)
                elif k == 'chmod':
                    file1=(parts[1])
                    file2=(parts[2])
                    self.commands.chmod(file1,file2)
                elif k == 'history':
                    self.commands.history()
                elif k == 'wc':
                    file=(parts[0])
                    if(len(parts)==2):
                        self.commands.wc(parts[1],"0")
                    elif(len(parts)==3):
                        self.commands.wc(parts[1],parts[2])
                    elif(len(parts)>3):
                        printf("more arguments for wc command")
                    else:
                        printf("missing operands in wc")
                elif k == 'cd':
                    self.commands.cd(parts[1])
                elif k == 'cp':
                    src=(parts[1])
                    dest=(parts[2])
                    self.commands.cp(src,dest)
				
            
			
if __name__=="__main__":
    d = driver()    
    d.runShell()


