#!python3

# searches for orphaned XMP files


import os, sys, shutil, glob

def isOrphan(path):
    originalPath = path[:-4]
    
    isPathFile = os.path.isfile(originalPath)

    return isPathFile
    

# returns list of XMP files that are orphans
def getOrphanXMPFiles(path):
    listing = glob.glob(path+os.path.sep+'*')
    
    for f in listing:
        fullname = os.path.abspath(f)

        if os.path.isfile(fullname):
            if fullname[-4:] == '.xmp':
                if not isOrphan(fullname):
                    print(fullname)
        elif os.path.isdir(f):
            getOrphanXMPFiles(fullname)


getOrphanXMPFiles('.')

