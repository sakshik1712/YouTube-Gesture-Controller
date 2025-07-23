from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class YouTubeController:
    def __init__(self, video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(video_url)
        time.sleep(5)
        self.player = self.driver.execute_script("return document.querySelector('video')")

    def play(self):
        self.driver.execute_script("document.querySelector('video').play()")

    def pause(self):
        self.driver.execute_script("document.querySelector('video').pause()")

    def next_video(self):
        self.driver.execute_script("document.querySelector('.ytp-next-button').click()")

    def previous_video(self):
        self.driver.execute_script("document.querySelector('.ytp-prev-button').click()")

    def volume_up(self):
        self.driver.execute_script(
            "document.querySelector('video').volume = Math.min(1, document.querySelector('video').volume + 0.1)")

    def volume_down(self):
        self.driver.execute_script(
            "document.querySelector('video').volume = Math.max(0, document.querySelector('video').volume - 0.1)")

