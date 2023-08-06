import subprocess
import os
def html_to_picture(source_path,dest_path,phantomjs_absolute_path="phantomjs.exe"):
    current_path = os.path.dirname(__file__)
    subprocess.Popen(phantomjs_absolute_path+" "+current_path+"\\snap.js "+source_path+" "+dest_path, shell=True, stderr=subprocess.STDOUT)