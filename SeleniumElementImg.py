from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.options import Options
from selenium.webdriver.chrome.options import Options
import os
from bs4 import BeautifulSoup

# AdBlock extension
#path_to_extension = r'C:\Users\Reuben\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\3.41.0_0'

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('load-extension=')#+ path_to_extension)
# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"\\chromedriver.exe"




driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)


driver.get("https://www.google.com/")

time.sleep(3)
counter = 1

def grabHtml():
    html = driver.execute_script('return document.documentElement.outerHTML')
    soup = BeautifulSoup(html,'html.parser')

def nextPage():
    continue_link = driver.find_element_by_link_text('next ›')
    continue_link.click()
    time.sleep(5)

def savePosts():
    global counter, driver
    elements = driver.find_elements_by_class_name('thing')
    for element in elements:
        element_png = element.screenshot_as_png
        with open(str(counter)+".png", "wb") as file:
            file.write(element_png)
        counter += 1

def main():
    
    while True:
        savePosts()
        try:
            nextPage()
        except:
            print("Did not find next button")
            break
#<article class="Post size-compact" style="z-index: 1;"><div class="Post__header-wrapper"><div class="PostContent size-compact"><a class="PostContent__image-link " href="https://www.boston.com/culture/entertainment/2015/06/16/why-the-music-of-jaws-is-still-terrifying" target="_blank" style="background-image: url(&quot;https://b.thumbs.redditmedia.com/6jbIMVCNIXJnI2-e8lcdAMAn9GvkM76g4h4y9fKdNuk.jpg&quot;);"></a></div><header class="PostHeader size-compact m-thumbnail-margin"><div class="PostHeader__metadata-container"><div class="PostHeader__post-descriptor-line"><div class="PostHeader__post-descriptor-line-overflow"><span><a href="/r/todayilearned/" class="PostHeader__subreddit-link">r/todayilearned</a><span class="PostHeader__seperator PostHeader__flush-w-icon"></span><span><!-- react-text: 204 -->4d<!-- /react-text --><span class="PostHeader__seperator PostHeader__flush-w-icon"></span><a href="/user/DivineEnergies" class="PostHeader__author-link undefined">u/DivineEnergies</a></span><span class="PostHeader__seperator PostHeader__flush-w-icon"></span><!-- react-empty: 208 --></span></div></div><div class="PostHeader__metadata"></div></div><a href="/r/todayilearned/comments/ayqz19/til_that_steven_spielberg_thought_john_williams/" class="PostHeader__post-title-line ">TIL that Steven Spielberg thought John Williams was joking the first time he played the JAWS theme for him.</a><a class="PostHeader__post-link" href="https://www.boston.com/culture/entertainment/2015/06/16/why-the-music-of-jaws-is-still-terrifying" target="_blank"><!-- react-text: 212 -->boston<!-- /react-text --><span class="PostHeader__post-link-icon icon icon-linkout blue"></span></a></header></div><footer class="PostFooter size-compact "><span class="Share"><img class="Share__image v2" src="https://www.redditstatic.com/mweb2x/img/icon_share_ios_32.png"><!-- react-text: 217 -->Share<!-- /react-text --></span><a href="/r/todayilearned/comments/ayqz19/til_that_steven_spielberg_thought_john_williams/" class="PostFooter__hit-area PostFooter__comments-link"><span class="PostFooter__comments-icon icon icon-comment"></span><!-- react-text: 220 -->47<!-- /react-text --></a><div class="PostFooter__vote-and-tools-wrapper"><div class="PostFooter__dropdown-button PostFooter__hit-area icon icon-seashells"></div><span class="PostFooter__vertical-divider"></span><div class="VotingBox"><div class="VotingBox__upvote icon icon-upvote "></div><div class="VotingBox__score ">448</div><div class="VotingBox__downvote icon icon-downvote "></div></div></div><div class="DropdownModalWrapper"><!-- react-empty: 229 --></div></footer></article>

#posts = driver.find_element_by_cssselector("article[@class='Post size-compact']")

#element = driver.find_element_by_tag_name('article')
#element_png = element.screenshot_as_png
#with open("test2.png", "wb") as file:
#    file.write(element_png)

#savePosts()
#//*[@id="siteTable"]/div[51]/span/span[3]/a
#siteTable > div.nav-buttons > span > span.next-button > a
#links = soup.find_all('a')
#button = soup.find_all('span',attrs={'class':'next-button'})
#driver.find_element_by_xpath("//*[@id='siteTable']/div[51]/span/span")

print('Add old.reddit.com##DIV[class="side"] to AdBlock and refresh page')
input("Press Enter to continue...")
#https://old.reddit.com/r/todayilearned/top/?sort=top&t=month
driver.get("https://old.reddit.com/r/todayilearned/top/?sort=top&t=month")
time.sleep(5)
main()
print('Complete')
