import subprocess
def easy_snap(source_name,dest_name):
    subprocess.Popen("phantomjs.exe snap.js "+source_name+" "+dest_name, shell=True, stderr=subprocess.STDOUT)


