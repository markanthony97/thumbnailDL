import argparse
import urllib.request
import os, re
from sys import platform

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('Link',metavar='Link')
    parser.add_argument('-f','--format',help="Download format (max or hq)")
    parser.add_argument('-o','--output',help="Output Folder")
    parser.add_argument('-n','--filename',help="Output filename")
    args = parser.parse_args()
    vid_code=args.Link

    if platform == "win32" or platform == "cygwin" or platform == "msys":
        pathsep = "\\"
    else:
        pathsep="/"

    if args.output is None:
        outputF=os.getcwd()+pathsep
    else:
        outputF=args.output+pathsep

    regex_long = '(watch\?v\= *?)'
    thumbCode=args.Link.split('/')[3]
    LongMatch = re.search(regex_long, thumbCode)

    if LongMatch:
        thumbCode=re.findall('watch\?v\=(.*)',thumbCode)
        thumbCode=thumbCode[0]

    download(thumbCode,args.format,outputF,args.filename)


def download(code,format,folder,filename):
    if filename=="":
        filename==code

    if format=="max":
        imLink="https://i3.ytimg.com/vi/"+code+"/maxresdefault.jpg"
    elif format=="hq":
        imLink="https://i3.ytimg.com/vi/"+code+"/hqdefault.jpg"
    else:
        imLink1="https://i3.ytimg.com/vi/"+code+"/maxresdefault.jpg"
        imLink2="https://i3.ytimg.com/vi/"+code+"/hqdefault.jpg"
    try:
        if format!="hq" or format!="max":
            urllib.request.urlretrieve(imLink1, folder+filename+"_max.jpg")
            urllib.request.urlretrieve(imLink2, folder+filename+"_hq.jpg")
        else:
            urllib.request.urlretrieve(imLink, folder+filename+".jpg")
    except:
        imLink=re.sub('i3','i',imLink,count=1)
        if format!="hq" and format!="max":
            urllib.request.urlretrieve(imLink1, folder+filename+"_max.jpg")
            urllib.request.urlretrieve(imLink2, folder+filename+"_hq.jpg")
            print("Saved",imLink1,"and",imLink2,"at",folder)
        else:
            urllib.request.urlretrieve(imLink, folder+filename+".jpg")
            print("Saved",imLink,"at",folder+filename+".jpg")



if __name__ == "__main__":
    main()
