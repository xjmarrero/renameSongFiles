#! /usr/bin/python

import os, re, argparse



class RenameSongs:
    
    def __init__(self):
        self.directory = ''
        self.suffixToRemove = ''
        
    def changeDirectory(self,newDirectory):
        self.directory = newDirectory
        return self.directory
    
    def suffix(self,newSuffix):         
        self.suffixToRemove = newSuffix
        return self.suffixToRemove
    
    def removeSuffix(self):
        try:            
            for root, dirs, filenames in os.walk(self.directory):
 
                self.suffixToRemove = re.escape(self.suffixToRemove)
                patFinder1 = re.compile(self.suffixToRemove)                
                
                for filename in filenames:
                    correctSongName =""
                    findSuffix = re.search(patFinder1,filename)
                    if (findSuffix):
                        print 'Old File Name: %s' % (filename)
                        filename = os.path.join(root, filename)
                        correctSongName += filename
                        subFound = patFinder1.sub('', correctSongName)
                        os.rename(filename, subFound)
                        print 'New File Name: %s: ' % (subFound)
                    else:
                        return 'No files to rename'
                return 'Successfully renamed all the file(s)'                                      
        except IOError:
            return "The given directory does not exist" 



def main():
    parser = argparse.ArgumentParser(description="An argparse example")

    parser.add_argument('word', help='The word you would like to remove (e.g. brandname.)')
    parser.add_argument('directory', help='The directory to take')
    args = parser.parse_args()
       
    a = RenameSongs()
    a.suffix(args.word)
    a.changeDirectory(args.directory) 
    print a.removeSuffix()
     

if __name__ == '__main__' : main()