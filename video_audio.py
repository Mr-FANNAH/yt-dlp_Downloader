import yt_dlp

def download_video(url, download_type):
    if download_type == 'video':
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',  
            'format': 'bestvideo+bestaudio/best',  
        }
    elif download_type == 'audio':
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s', 
            'format': 'bestaudio/best',     
            'postprocessors': [{            
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        print("Type de téléchargement non valide. Veuillez choisir 'video' ou 'audio'.")
        return
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
if __name__ == '__main__':
    video_url = input("Veuillez entrer l'URL de la vidéo: ")
    download_type = input("Voulez-vous télécharger la vidéo ou l'audio? (video/audio): ").strip().lower()
    download_video(video_url, download_type)