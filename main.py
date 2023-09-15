import requests
import os
import configparser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,os
from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions

import yt_dlp as youtube_dl



def getLastVideoUrl(username):
    url = "https://www.youtube.com/@" + username

    res = requests.get(url)

    videoId = res.text.split('"watchEndpoint":{"videoId":',1)[-1].split(',',1)[0].replace('"','').strip()
    video_url = f"https://www.youtube.com/watch?v={videoId}"

    return video_url

def getLastshortUrl(username):
    url = "https://www.youtube.com/@" + username

    res = requests.get(url)

    videoId = res.text.split('"reelWatchEndpoint":{"videoId":', 1)[-1].split(',', 1)[0].replace('"', '').strip()
    video_url = f"https://www.youtube.com/shorts/{videoId}"

    return video_url
    


    
def downloadvideo(video_url,save_path):
  
   

    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(id)s.%(ext)s',
    }
    print(ydl_opts)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Assuming the video gets saved with the title name. 
    # The actual name may vary based on the video's title and the format selected.
    info_dict = youtube_dl.YoutubeDL(ydl_opts).extract_info(video_url, download=False)
    # print(info_dict)
    video_id = info_dict.get('id', '')
    video_title = info_dict.get('title', '')
    video_format = info_dict.get('ext', 'mp4')
    video_desc = info_dict.get('description', '')
    # video_title = video_title.replace(' ','').strip()
    # path = f"{save_path}/{video_title}.{video_format}"
    path = os.path.join(save_path,str(video_id) + '.' + video_format)
    return path,video_title,video_desc



def checkForNewVideo(usernames):
    results = []
    for username in usernames:
        path = os.path.join(os.getcwd(),'history',username+"_last_video.txt")
        # desription = os.path.join(os.getcwd(),'history',username+"description.txt")

        # title = os.path.join(os.getcwd(),'history',username+"title.txt")

        lastVideoUrl = ""
        try:
            file = open(path,'r')
            lastVideoUrl = file.read().strip()
            file.close()
        except:
            file = open(path,'w')
            
            file.close()
        NewUrl = getLastVideoUrl(username)
        time.sleep(2)
        if lastVideoUrl != NewUrl:
            results.append([username,NewUrl])
            print("////////////////////new video found for"+ str(usernames))
        else:
            print("////////////////////no   new video found for??????????" + str(usernames))


    return results        


def checkForNewshort(usernames):
    results = []
    for username in usernames:
        path = os.path.join(os.getcwd(),'shortshistory',username+"_last_short.txt")
        # desription = os.path.join(os.getcwd(),'history',username+"description.txt")

        # title = os.path.join(os.getcwd(),'history',username+"title.txt")

        lastshortUrl = ""
        try:
            file = open(path,'r')
            lastshortUrl = file.read().strip()
            file.close()
        except:
            file = open(path,'w')
            
            file.close()
        NewUrl = getLastshortUrl(username)
        time.sleep(2)
        if lastshortUrl != NewUrl:
            results.append([username,NewUrl])
            print("////////////////////new short found for"+ str(usernames))
        else:
            print("////////////////////no   new short found for??????????" + str(usernames))


    return results
    
class YoutubeBot:
    def _init_(self) -> None:
        self.driver = None

    def upload(self, browserlocation,video_path, title, description):

        driver_path = "geckodriver.exe"  # Replace with your path to geckodriver
        url = "https://youtube.com"
        fp = webdriver.FirefoxProfile(browserlocation)
# browser C:\Users\Muhammad Umer\AppData\Roaming\Mozilla\Firefox\Profiles\zh4moway.default-release= webdriver.Firefox(fp)
        self.driver = webdriver.Firefox(fp,executable_path=driver_path)
        self.driver.get(url)
        time.sleep(8)
        # self.driver.get('https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Faccount%26feature%3Dredirect_login&hl=en&passive=true&service=youtube&uilel=3&ifkv=AYZoVhdkHc9zStBxCvS4mG0fI4a0Nt54FCBiOUiYTZqGSOlZMHQ_2o1_yjYgLBf4IgbM9t95fSg64Q&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        create=self.driver.find_element(By.XPATH, '//*[@aria-label="Create"]').click()
        time.sleep(1)
        upload_videos = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Upload video')])[1]")
        upload_videos.click()
        time.sleep(7)
        file_input = self.driver.find_element(By.XPATH, '//*[@id="content"]/input')
        file_input.send_keys(video_path)
        time.sleep(4)

        title_input = self.driver.find_element(By.XPATH, '(//div[@id="textbox"])[1]')
        title_input.send_keys(title)
        time.sleep(4)

        description_input = self.driver.find_element(By.XPATH, '(//div[@id="textbox"])[2]')
        description_input.send_keys(description)
        time.sleep(5)
        try:
            kkk= self.driver.find_element(By.XPATH, '//*[@name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').click()
            time.sleep(5)
        except:
            pass
        # time.sleep(4)
        kkk= self.driver.find_element(By.XPATH, '//*[@name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').click()
        time.sleep(5)
        try:
            for _ in range(4):
                next_button = self.driver.find_element(By.XPATH, '//div[text()="Next"]')
                next_button.click()
                # time.sleep(4)
                time.sleep(5)
        except:
            pass
        try:
            next_button = self.driver.find_element(By.XPATH, '//div[text()="Next"]')
            time.sleep(5)
        except:
            pass
        public_option = self.driver.find_element(By.XPATH, '//*[@name="PUBLIC"]')
        public_option.click()
        time.sleep(2)

        publish_button = self.driver.find_element(By.XPATH, '//div[text()="Publish"]')
        publish_button.click()
        time.sleep(5*60)
        self.driver.quit()




def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Get the usernames from the "Usernames" section
    usernames_str = config["Usernames"]["users"]
    usernames = [username.strip() for username in usernames_str.split(",")]
    browserlocation=config["Usernames"]["location"]
    
    while 1:
        print("** checking for new vdeos.")
        time.sleep(2)
        try:
            list_ = checkForNewVideo(usernames) #[[u,vid],[u,vid],[u,vid]]
            
            for l in list_:
                username = l[0]
                videoUrl = l[1]
                print(videoUrl)
                
                
                lastpath = os.path.join(os.getcwd(), 'history', username + "_last_video.txt")
                # description=os.path.join(os.getcwd(), 'history', username + "_last_video.txt")
                    # Save the video URL to a file within the folder
                folder = os.path.join(os.getcwd(),'videos')
                # video_desc=os.path.join(os.getcwd(),'description')
                # # download video
                # video_title=os.path.join(os.getcwd(),'title')
                # localPath = downlad(videoUrl) 
                lpath,video_title,video_desc= downloadvideo(videoUrl,folder)
                time.sleep(5)
                if os.path.exists(lastpath):
                    with open(lastpath, "w") as file:
                        file.write(videoUrl)
            
                
                # print(_)
                time.sleep(20)
                video_path = 'videos'
                title = video_title
                description = video_desc
                uploader = YoutubeBot()
                uploader.upload(browserlocation,lpath, video_title,video_desc)
                # print( " new video of "+ str(usernames)) 
        except:
            print("////////////////////// no video found in this channel")
            pass
        print ("know looking for shorts ")
        time.sleep(5)
        try:
            list__ = checkForNewshort(usernames) #[[u,vid],[u,vid],[u,vid]]

            for l in list__:
                username = l[0]
                videoUrls = l[1]
                print(videoUrls)
                
                
                lastpath = os.path.join(os.getcwd(), 'shortshistory', username + "_last_short.txt")
                # description=os.path.join(os.getcwd(), 'history', username + "_last_video.txt")
                    # Save the video URL to a file within the folder
                folder = os.path.join(os.getcwd(),'Shorts')
                # video_desc=os.path.join(os.getcwd(),'description')
                # # download video
                # video_title=os.path.join(os.getcwd(),'title')
                # localPath = downlad(videoUrls) 
                lpath,video_title,video_desc= downloadvideo(videoUrls,folder)
                time.sleep(5)
                if os.path.exists(lastpath):
                    with open(lastpath, "w") as file:
                        file.write(videoUrls)
            
                
                # print(_)
                time.sleep(20)
                # video_path = 'videos'
                title = video_title
                description = video_desc
                uploader = YoutubeBot()
                uploader.upload(browserlocation,lpath, video_title,video_desc)      
        except:
            print("///////////////////no short found in this channel")      
            pass
        print("///////////////////waiting for new video")    
        time.sleep(3*60*60)
                

            




if __name__ == "__main__":
    main()





