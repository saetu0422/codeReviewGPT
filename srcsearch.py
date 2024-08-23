import glob
import os

def fileAll():
    # 스크립트가 위치한 디렉토리를 기준으로 경로를 설정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_list = glob.glob(os.path.join(base_dir, '../**'), recursive=True)
    return file_list

def filePy():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_list = glob.glob(os.path.join(base_dir, '../**/*.py'), recursive=True)
    return file_list

def fileRQ():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_list = glob.glob(os.path.join(base_dir, '../**/*.txt'))
    return file_list