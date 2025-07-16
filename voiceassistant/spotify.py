from selenium import webdriver

class music():

    def __init__(self):
            self.driver = webdriver.Chrome(executable_path='C:\Windows\chromedriver-win32\chromedriver.exe')

    def play(self, query):
            self.query = query
            self.driver.get(url="https://www.spotify.com")


#assist = music()
#assist.play(' ')
