import mod.tools as tool
import shutil

if __name__ == '__main__':

    fileName = tool.downloadAudio()
    print(fileName)

    newFile = tool.findKey(fileName)

    tool.ripStems(str(newFile))

    shutil.move(f"{newFile}", f"{newFile[0:-4]}/")
