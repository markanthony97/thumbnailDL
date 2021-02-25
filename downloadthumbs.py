import argparse
import urllib.request
import os, re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('Link',metavar='Link')
    parser.add_argument('-f','--format',default='hq')
    parser.add_argument('-o','--output')

    args = parser.parse_args()


    vid_code=args.Link
    if args.output is None:
        outputF=os.getcwd()
    else:
        outputF=args.output

    thumbCode=args.Link.split('/')[3]
    regex_long = '(watch\?v\= *?)'
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
    urllib.request.urlretrieve(imLink, folder+code+".jpg")
    print("Saved",imLink,"at",folder+code+".jpg")
    
if __name__ == "__main__":
    main()
