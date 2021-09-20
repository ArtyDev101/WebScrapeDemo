from selenium import webdriver
#from bs4 import BeautifulSoup as soup
#In time I will learn how to use beautifulSoup to do this.

def main():

    #setup driver
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://euw.op.gg/summoner/userName=Halloweenn")

    #GameItemWrap is the class name for each game as it appears on the website.
    #It seems that this is the container for all the elements of each "game"
    games = driver.find_elements_by_class_name('GameItemWrap')
    #this code gets the games as an array of web elements
    for game in games:
        print (getStats(game))

    #close the page once we have done.
    driver.quit()

    print("Session over")

def getStats(game):
    try:
        #try to find a winning game
        gameItem = game.find_element_by_xpath('.//div[@class="GameItem Win  "]')
    except:
        try:
            #try to find a losing game
            gameItem = game.find_element_by_xpath('.//div[@class="GameItem Lose  "]')
        except:
            print("No game found")

    result = gameItem.get_attribute("data-game-result")
    
    #if we were to go further inside the webpage to find stats such as champion played etc,
    # we would use the following code.
    #content = gameItem.find_element_by_xpath('.//div[@class="Content"]')
    #gameSettingInfo = content.find_element_by_xpath('.//div[@class="GameSettingInfo"]')

    return (result)

if __name__ == "__main__":
    main()