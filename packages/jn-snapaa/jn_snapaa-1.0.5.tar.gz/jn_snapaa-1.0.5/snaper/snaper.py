import subprocess
def jn_snap(source_name,dest_name)
    subprocess.Popen("phantomjs.exe snap.js "+"main.html "+"main.png", shell=True, stderr=subprocess.STDOUT)


