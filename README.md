yt-dlp Video/Audio Downloader
This Python script allows you to download videos or audio from YouTube using yt_dlp.

Prerequisites
Python 3.x installed on your machine.
yt_dlp installed. You can install it using pip.
Installation
Clone the Repository

sh
Copier le code
git clone https://github.com/yourusername/yt-dlp-downloader.git
cd yt-dlp-downloader
Install Required Packages

Install yt_dlp using pip:

sh
Copier le code
pip install yt-dlp
(Optional) Install FFmpeg

For audio extraction, yt_dlp uses FFmpeg. You can download and install FFmpeg from FFmpeg.org.

Usage
To download a video or audio file, follow these steps:

Open a Command Prompt or Terminal

Navigate to the Script Directory

sh
Copier le code
cd path/to/yt-dlp-downloader
Run the Script

sh
Copier le code
python downloader.py
Provide the Video URL and Download Type

The script will prompt you to enter the video URL and the type of download (video or audio).

sh
Copier le code
Veuillez entrer l'URL de la vidéo: <Enter the video URL here>
Voulez-vous télécharger la vidéo ou l'audio? (video/audio): <Enter 'video' or 'audio'>
Example
Here's an example of how to use the script:

Run the script:

sh
Copier le code
python downloader.py
Enter the URL of the video you want to download:

sh
Copier le code
Veuillez entrer l'URL de la vidéo: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Choose the download type (video or audio):

sh
Copier le code
Voulez-vous télécharger la vidéo ou l'audio? (video/audio): video
The video will start downloading, and you'll see messages indicating the download progress. Once the download is complete, the file will be saved in the current directory.
