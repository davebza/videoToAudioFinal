#! python3
"""Takes a given folders mp4 files, and creates a folder for audio output then creates Mp3's for all of the .mp4s.
NOTE: there are no checks for video files, so this will fail if the files are not video format."""

import subprocess
import os

#Set the input and output folder names:

# Absolute paths, uncomment if needed
# inputLocation = "C:\\myPythonFiles\\videoToAudio\\videos\\"
# outputLocation = "C:\\myPythonFiles\\videoToAudio\\audioFiles\\"

# relative paths, will work when the script is in the folder with the video files:
inputLocation = "videos\\"
outputLocation = "audioFiles\\"

# Create a folder for the audio files, and create one if needed:
if not(os.path.isdir(outputLocation)):
    print("No directory for audio files. Creating a directory now:")
    try:
        os.mkdir(outputLocation)
    except OSError:
        print("Creation of the directory %s failed" % outputLocation)
    else:
        print("Successfully created the directory %s " % outputLocation)
else:
    print(f"{outputLocation} already exists.")

#Once the folders are set, get all files in the target directory:
print("Proceeding to the renaming:")
fileList = os.listdir(inputLocation)

#Remove audio for each file and rename:
for i in range(len(fileList)):

    inputFile = inputLocation + fileList[i]
    outputFile = outputLocation + "audioOutput_" + str(i+1)+".mp3"
    command = "ffmpeg -i " + inputFile +" -ab 160k -ac 2 -ar 44100 -vn " + outputFile
    subprocess.call(command, shell=True)

    # TODO: check file extension is .mp4 before working on file
    # TODO: Add readme.md