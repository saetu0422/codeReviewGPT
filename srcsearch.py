import glob

def fileAll():
    file_list = glob.glob('../../AI-Scientist-main/AI-Scientist-main/**', recursive=True)
    return file_list

def filePy():
    file_list = glob.glob('../../AI-Scientist-main/AI-Scientist-main/**/*.py', recursive=True)
    return file_list

def fileRQ():
    file_list = glob.glob('../../AI-Scientist-main/AI-Scientist-main/*.txt')
    return file_list