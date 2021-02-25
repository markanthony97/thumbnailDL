import argparse
import urllib.request
import os, re
from sys import platform

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('Link',metavar='Link')
    parser.add_argument('-f','--format',default='hq')
    parser.add_argument('-o','--output')

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

    download(thumbCode,args.format,outputF)


def download(code,format,folder):
    if format=="hq":
        imLink="https://i3.ytimg.com/vi/"+code+"/hqdefault.jpg"
    else:
        imLink="https://i3.ytimg.com/vi/"+code+"/maxresdefault.jpg"
    try:
        urllib.request.urlretrieve(imLink, folder+code+".jpg")
    except:
        imLink=re.sub('i3','i',imLink,count=1)
        urllib.request.urlretrieve(imLink, folder+code+".jpg")
    print("Saved",imLink,"at",folder+code+".jpg")


if __name__ == "__main__":
    main()
