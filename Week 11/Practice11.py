import os

def countFiles(path):
    if os.path.isdir(path)==False:
        return 1
    else:
        count=0
        for elem in os.listdir(path):
            filename= path+ "/" + elem
            count+= countFiles(filename)
        return count
                
def test():
    print("test")
    assert(countFiles("sampleFiles/folderB/folderF/folderG") == 0)
    assert(countFiles("sampleFiles/folderB/folderF") == 0)
    assert(countFiles("sampleFiles/folderB") == 2)
    assert(countFiles("sampleFiles/folderA/folderC") == 4)
    assert(countFiles("sampleFiles/folderA") == 6)
    assert(countFiles("sampleFiles") == 10)
    print("passed")

test()
