#! /usr/bin/python

import os
import re
import argparse

class RenameSongs:
    def __init__(self):
        self.directory = ''
        self.suffixToRemove = ''

    def change_directory(self, new_directory):
        self.directory = new_directory
        return self.directory

    def suffix(self, new_suffix):
        self.suffixToRemove = new_suffix
        return self.suffixToRemove

    def remove_suffix(self):
        try:
            for root, dirs, filenames in os.walk(self.directory):

                self.suffixToRemove = re.escape(self.suffixToRemove)
                pat_finder1 = re.compile(self.suffixToRemove)

                for filename in filenames:
                    correct_song_name = ""
                    find_suffix = re.search(pat_finder1, filename)
                    if find_suffix:
                        print 'Old File Name: %s' % filename
                        filename = os.path.join(root, filename)
                        correct_song_name += filename
                        sub_found = pat_finder1.sub('', correct_song_name)
                        os.rename(filename, sub_found)
                        print 'New File Name: %s: ' % sub_found
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
    a.change_directory(args.directory)
    print a.remove_suffix()

if __name__ == '__main__': main()