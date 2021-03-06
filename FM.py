#!/usr/bin/python3
#automation script console thing
import os, sys
try:
    from to_encode_or_to_decode import *
    print("Ah nice; imported 'to encode or to decode.py'!")
except ImportError:
    print("Sorry, error importing 'to_encode_or_to_decode.py'.")
cmdlist = ["cmdlist:\nList's all available commands with a brief description.",
    "exit:\nExits the program.",
    "clear:\nClears the current screen.",
    "ldir:\nLists all the files in the current directory.",
    "ldirperm:\nLists all the files in the current directory; in the longer format, displaying read and write permisions.",
    "mkfile:\nPrompts the user for input (@ the '$'). Then makes a file with that name(Linux only for the moment)",
    "rmfile:\nPrompts a user for input then removes a file that matches that input.",
    "pwd:\nPrints the current working directory.",
    "mkdir:\nPrompts the user for a name and makes a directory.",
    "rmdir:\nPrompts the user for a name and then removes a directory.",
    "chdir:\nPrompts the user to provide a path. e.g. '/home/admin/otherdirectory', then changes the current directory to that path.",
    "b64console:\nProvides the user with a console to base64 encode data.",
    "printf:\nPrints out the text to the screen e.g 'printf sometext'.",
    "read:\nPrints out the content of a file in the terminal window(or command line under windows).",
    "write:\nWrites input to a file.",
    "usr:\nPrints the name of the current user.",
    "printl:\nPrints a given argument is a letter by letter format."
    "ping:\nTests a network for latency but is a good way to see if your network is reaching the Internet.",
    "fullforms:\nPrints out a short list of full names for file extensions. E.g: '.txt', '.gif'.",
    "odhc:\nDisplays info about the American Standard Code for Information Interchange(ASCII). character set. It's encoded in octal, decimal, and hexadecimal.",
    "digfile:\nPrompts you for a filename and string of text to search. If it finds a match will print out a result. Note: you must be in the right directory.",
    "digdir:\nPrompts you for a path to a directory and for content to search for recursively and match. For example: '/home/user/dir' < [path example]",
    "findStr:\nAsks for a filename and then searches it for a specific string based on another input.(The file you are searching must be in the same directory)",
]
OSIS=sys.platform
print("Ah nice we can see your operating system is %s.\nWill make a note of that!"%(OSIS))
def BasicSH():
    return input("$ ") #very useful
def pleasefilename():
    print("Please enter a filename at the prompt. ('$')\n") #Ah that too
def pleasedirectoryname():
    print("Please enter a directory name at the prompt. ('$')\n")
def pleasepath():
    print("Please enter a valid path. ( '/home/username/myfiles')\n")
def start():
    print("Welcome, we hope this helps better navigate file-systems...")
    cwd=os.getcwd(); print("The current directory is:"+cwd+".")
    print("For a full list of commands just type 'cmdlist'.\nYour command: ")
    cmd=input("$"); return cmd
def init_msg():
    print("[+]FileManagerProgram[+]")
def issue_cmd(cmd):
    if cmd == "cmdlist":
        for each in cmdlist:
                print("\n%s"%(each))
    elif cmd == "clear":
        command_list.clear()
    elif cmd == "exit":
        exit()
    elif cmd == "mkfile":
        pleasefilename()
        command_list.mkfile(BasicSH())
    elif cmd == "rmfile":
        pleasefilename()
        command_list.rmfile(BasicSH())
    elif cmd == "pwd":
        command_list.pwd()
    elif cmd == "mkdir":
        pleasedirectoryname()
        command_list.mkdir(BasicSH())
    elif cmd == "rmdir":
        pleasedirectoryname()
        command_list.mkdir(BasicSH())
    elif cmd == "chdir":
        pleasepath()
        command_list.chdir(BasicSH())
    elif cmd == "ldir":
        command_list.ldir()
    elif cmd == "ldirperm":
        command_list.ldirperm()
    elif cmd == "b64console":
        to_encode_or_to_decode()
    elif cmd == "printf":
        command_list.printf()
    elif cmd == "read":
        command_list.read()
    elif cmd == "write":
        command_list.write()
    elif cmd == "usr":
        command_list.usr()
    elif cmd == "printl":
        command_list.printl()
    elif cmd == "fullforms":
        command_list.fullforms()
    elif cmd == "odhc":
        command_list.odhc()
    elif cmd == "digfile":
        command_list.digfile()
    elif cmd == "digdir":
        command_list.digdir()
    elif cmd == "findStr":
        command_list.findStr()
#space
class command_list:
    def clear():
        if OSIS:
            return os.system("cls")
        else:
            return os.system("clear")
    def ldir():
        if OSIS:
            return os.system("dir")
        else:
            return os.system("ls -a")
    def ldirperm():
        if OSIS == "win32" or OSIS == "cygwin":
            print("Sorry, not on window's you don't!")
        else:
            return os.system("ls -la")
    def mkfile(filename):
        if OSIS:
            print("Not available under windows!")
        else:
            try:
                os.system("touch %s"%(filename))
            except IOError:
                print("""Sorry error making the file\n
                Already a file with this name in this directory?""")
    def rmfile(filename):
        return os.remove(filename)
    def pwd():
        return os.getcwd()
    def mkdir(dirname):
        return os.mkdir(dirname)
    def rmdir(dirname):
        return os.rmdir(dirname)
    def chdir(path):
        return os.chdir(path)
    def printf():
        print("Please enter some text to be printed: \n")
        i=BasicSH(); print("%s"%(i))
    def read():
        print("Filename to print to screen:\n"); arg=BasicSH()
        try:
            if OSIS:
                try:
                    tmpVar=open("%s"%(arg),"r")
                    for each in tmpVar.readlines():
                            print(each)
                except FileNotFoundError:
                    print("File not found!(please check the file name)")
                finally:
                    tmpVar.close()
            else:
                os.system("cat %s"%(arg))
        except IOError:
            print("Sorry file not found...")
        finally:
            print("\n")
    def write():
        print("filename please:\n"); filename=BasicSH()
        print("Content to write to file:\n"); content=BasicSH()
        print("Existing file or new file?('e'|'n').\n"); noe=BasicSH()
        try:
            if noe == "e":
                open_file=open("%s"%(filename),"a+"); open_file.write(content)
                open_file.close()
                print("Written to file!")
            elif noe == "n":
                open_file=open("%s"%(filename),"w+"); open_file.write(content)
                open_file.close()
                print("Written to file!")
        except FileNotFoundError:
            print("Sorry, file not found!\nWrong directory?\nWrong file name?\n")
        except IOError:
            print("Sorry an error has taken place!")
    def usr():
        return os.system("echo $USER")
    def printl():
        print("Content:\n"); arg=BasicSH()
        for all in arg:
            print(all)
    def ping():
        return os.system("ping %s"%(BasisSH()))
    def fullforms():
        info = [
        "3GP: 3rd generation Project.",
        "3GPP: 3rd generation Partnership Project.",
        "ACC: Advanced Audio Coding.",
        "AMR: Adaptive Multi-Rate Codec.",
        "AVI: Audio video Interleave.",
        "BMP: Bitmap.",
        "DOC: Document.",
        "DVX: DivX Video.",
        "GIF: Graphic Interchangeable format.",
        "JAD: Java Application Descriptor.",
        "JAR: Java Archive.",
        "JPEG: Joint Photographic Expert Group.",
        "M3G: Mobile 3D Graphics.",
        "M4A: MPEG-4 Audio File.",
        "MP3: Moving Picture Experts Group PhasePHASE3 (MPEG-3).",
        "MP4: MPEG-4 video file.",
        "MPEG: Moving Pictures Experts Group.",
        "(MPEG) MPEG1: Moving Pictures Experts Group.",
        "(MPEG-1)MPEG2: Moving Picture Experts Group.",
        "PhasePHASE 2 (MPEG-2).",
        "PDF: Portable Document Format.",
        "PNG: Portable Network Graphics.",
        "RTS: Real Time Streaming.",
        "SIS: Symbian OS Installer file.",
        ]
        for x in info:
            print("%s\n"%(x))
    def odhc():
       os.system("man ascii")
    def digfile():
        print("Filename: \n"); filename=BasicSH()
        print("Search-terms: \n"); searchterms=BasicSH()
        os.system("grep -i %s %s"%(searchterms,filename))
    def digdir():
        print("Directory: \n"); directory=BasicSH()
        print("Search-terms: \n"); searchdir=BasicSH()
        os.system("grep -R -i %s %s"%(searchdir,directory))
    def findStr():
        print("Filename please: \n")
        filename=BasicSH()
        try:
            with open("%s"%(filename),"r+") as file:
                i=input("String: ")
                search = re.compile(r'%s'%(i))
                for line in file:
                    find=search.findall("%s"%(i))
                if find == []:
                    print("Sorry nothing found.")
                else:
                    for each in find:
                        print("Found: %s"%(each))
        except IOError:
            print("There was an error in some input or output operation. Could it be the filename?")
        finally:
            file.close()
def main():
    issue_cmd(start())
    while 1 == True:
        init_msg(); issue_cmd(BasicSH())
if __name__ == "__main__":
    main()
