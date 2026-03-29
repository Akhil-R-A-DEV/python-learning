newFile = open("new file.txt","w")

content = newFile.write(''' this is the new conternt
                        inside the new file and 
                        this is using python ''')

newFile.close()