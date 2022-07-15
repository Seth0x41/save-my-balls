import os
import sys
from vtt_to_srt.vtt_to_srt import vtt_to_srt
subtitle_list=[]
video_list=[]
dir_path=os.getcwd()


def convert_to_srt(path=os.getcwd()):
    for subtitle in os.listdir(path):
        if subtitle.split()[-1][-3:] == "vtt":
            vtt_to_srt(subtitle)

def delete_old_files(path=os.getcwd()):
    for subtitle in os.listdir(path):
        if subtitle.split()[-1][-3:] == "vtt":
            os.remove(subtitle)
def creating_lists(path,video_format,subtitle_format):
    for file in os.listdir(path):
        if file.split()[-1][-3:] == subtitle_format:
            subtitle_list.append(file)
        elif file.split()[-1][-3:] == video_format:
            video_list.append(file)

def subtitle_rename(subtitle_format='vtt'):        
    for video in video_list:
        for subtitle in subtitle_list:
            if os.path.splitext(video)[0].split(".")[-1].split() == os.path.splitext(subtitle)[0].split()[:-1]:
                new_name = ' '.join(map(str,os.path.splitext(video)[0].split()))+"."+subtitle_format
                old_name = subtitle
                os.rename(old_name,new_name)
    print("Done!")
                



def main():

        creating_lists(dir_path,'mp4','vtt')
        subtitle_rename()
        if len(sys.argv) == 2 and sys.argv[1] == '-c':
            convert_to_srt()
        if len(sys.argv) == 3 and  sys.argv[1] == '-c' or sys.argv[2] == '-c' or sys.argv[1] == '-r'  or sys.argv[2] == '-r':
            convert_to_srt()
            delete_old_files()


main()
