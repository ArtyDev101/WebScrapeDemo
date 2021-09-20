from selenium import webdriver
#from bs4 import BeautifulSoup as soup
#import time

def main():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://euw.op.gg/summoner/userName=Halloweenn")
    print (driver.current_url)
    games = driver.find_elements_by_class_name('GameItemWrap')
    for game in games:
        printStats(game)
    driver.quit()
    print("Session over")

def printStats(game):
    try:
        gameItem = game.find_element_by_xpath('.//div[@class="GameItem Win  "]')
    except:
        try:
            gameItem = game.find_element_by_xpath('.//div[@class="GameItem Lose  "]')
        except:
            print("No game found")
    result = gameItem.get_attribute("data-game-result")
    #content = gameItem.find_element_by_xpath('.//div[@class="Content"]')
    #gameSettingInfo = content.find_element_by_xpath('.//div[@class="GameSettingInfo"]') 
    print (result)

if __name__ == "__main__":
    main()