from flask import Flask
from shutil import copyfile
import subprocess


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Server ready to serve! <br> <a href="/decompile">Check Services of apk</a>'


@app.route('/decompile')
def decompile():
    apkName='slice'
    copyfile('./apks/{}.apk'.format(apkName), './temp/{}.apk'.format(apkName))
    subprocess.call(['apktool','d','./temp/{}.apk'.format(apkName),'-f', '-o','temp/{}_re'.format(apkName)], stdin=subprocess.DEVNULL, shell=True)
    manifest=open('./temp/{}_re/AndroidManifest.xml'.format(apkName),'r')
    services=set()
    for line in manifest.readlines():
        if 'uses' in line:
            line=line[line.find('android:name="')+14:]
            line=line[:line.find('"')]
            services.add(line[line.rfind('.')+1:])
    str=''
    for i in services:
        str=str+i+'<br>'
    return '<h1>services used by {}:</h1><p>{}</p>'.format(apkName, str)



app.run()