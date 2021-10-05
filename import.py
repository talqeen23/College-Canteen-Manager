import subprocess

def install(name):
    subprocess.call(['pip', 'install', name])
install("flask");
install("pymysql");
install("flask_wtf");
install("flask_mail");

