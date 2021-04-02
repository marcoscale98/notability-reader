import os
import zipfile

def note_extractor(path:str, extract_dir:str):
    '''
    :param path: path of the .note file
    :param extract_dir: path of the directory where you want to place all the files extracted
    :return: None
    '''
    path = os.path.relpath(path)
    extract_dir = os.path.relpath(extract_dir)
    with zipfile.ZipFile(path, "r") as zip_ref:
        zip_ref.extractall(extract_dir)

note_extractor("../13_retiNeurali-17-48.note","../13_retiNeurali-17-48")