# import requests,os
# import yt_dlp as youtube_dl

# def getLastVideoUrl(username):
#     url = "https://www.youtube.com/@" + username

#     res = requests.get(url)

#     videoId = res.text.split('"reelWatchEndpoint":{"videoId":', 1)[-1].split(',', 1)[0].replace('"', '').strip()
#     video_url = f"https://www.youtube.com/shorts/{videoId}"

#     # Save the HTML content to a file named 'a.json' using UTF-8 encoding
#     # with open('a.json', 'w', encoding='utf-8') as file:
#     #     file.write(res.text)

#     return video_url
# def downloadvideo(video_url,save_path):
  
   

#     ydl_opts = {
#         'format': 'best',
#         'outtmpl': f'{save_path}/%(id)s.%(ext)s',
#     }
#     print(ydl_opts)
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([video_url])

#     # Assuming the video gets saved with the title name. 
#     # The actual name may vary based on the video's title and the format selected.
#     info_dict = youtube_dl.YoutubeDL(ydl_opts).extract_info(video_url, download=False)
#     # print(info_dict)
#     video_id = info_dict.get('id', '')
#     video_title = info_dict.get('title', '')
#     video_format = info_dict.get('ext', 'mp4')
#     video_desc = info_dict.get('description', '')
#     # video_title = video_title.replace(' ','').strip()
#     # path = f"{save_path}/{video_title}.{video_format}"
#     path = os.path.join(save_path,str(video_id) + '.' + video_format)
#     print("///////////////"+video_id)
#     print("///////////////"+video_title)
#     print("///////////////"+video_format)
#     print("///////////////"+ video_desc)
    
#     return path,video_title,video_desc
# # Example usage:
# video_url = getLastVideoUrl("lindyandjlo")
# print("Latest video URL:", video_url)
# save="videos"
# downloadvideo(video_url,save)

