import subprocess
def easy_snap(source_path,dest_path,phantomjs_absolute_path="phantomjs.exe"):
    subprocess.Popen(phantomjs_absolute_path+" snap.js "+source_path+" "+dest_path, shell=True, stderr=subprocess.STDOUT)