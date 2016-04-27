# lightwave-translator
Little Python script to translate object names from a language to another

Put translator.py in

C:\Program Files\NewTek\[LightWave_DIR]\support\plugins\scripts\Python\PRIS


Change directories with correct ones:

For example:

translate.txt directory
work_dir = "D:\\Temp\\Lightwave\\work\\"

Original lwo files directory
files_dir = "D:\\Temp\\Lightwave\\orig\\Objects\\"

Translates lwo files directory
dest_dir = "D:\\Temp\\Lightwave\\orig\\ObjectTrans\\"

Copy full scene to D:\Temp\Lightwave\orig and create an empty ObjectTrans directory.
Then run script from Lightwave Modeler and all .lwo files will be copied to dest_dir using word translations in translate.txt file.

translate.txt file will be full with words to trnaslate in word<TAB>translation format.
