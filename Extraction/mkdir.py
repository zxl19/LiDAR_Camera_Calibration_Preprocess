import os


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print "Destination directory %s created!" % (path)
    else:
        print "Destination directory %s exists!" % (path)
