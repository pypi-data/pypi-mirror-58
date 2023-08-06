# Example Package

#Download ffmpeg.

windows:-https://ffmpeg.zeranoe.com/builds/

#Set 2 Environment variable to :-

1)Variable:-pydub

Path:- Path where pydub is installed like(C:\Program Files\Python37\Lib\site-packages\pydub)

2)Variable:- Path
Path :- Path where ffmpeg installed like(C:\ffmpeg-20191022-0b8956b-win64-static\bin\)


#type following code in python shell after installing library.
1st step :

 from   EtmAudio2Text import  AudioTextConverter

2nd step:

AudioTextConverter.A2T('Type of Your Audio file','Path_of_your_AUDIO_file')


In ('Type of Your Audio file','Path_of_your_AUDIO_file') here write the type and path of audiofile that u want extract the text from.
for example 'AudioTextConverter.A2T('mp3',r'C:\Users\Dell\Downloads\AudioFiles\Models_Etc.mp3')'like that only
