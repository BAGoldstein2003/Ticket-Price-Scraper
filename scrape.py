import time
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
import pprint

def get_leagues(driver: uc.Chrome):
    #grab contents of home page
    driver.get('https://gametime.co')

    #open sports navigation menu and grab all subcategories (leagues)
    sportsNavButton = driver.find_elements('css selector', '.components-Headers-CategoriesButtonList-CategoriesButtonList-module__category-selector-button')[0]
    sportsNavButton.click()
    subCategories = driver.find_elements('css selector', '.components-Headers-HeaderDropdown-components-CategoriesDropdown-CategoriesDropdown-module__subcategory')
    subCategories = [cat for cat in subCategories if cat.text.isalnum()]
    leagues = {cat.text: {} for cat in subCategories}

    #loop through subcategories, saving each category and its teams to a list of dictionaries
    for idx, cat in enumerate(subCategories):
        hover = ActionChains(driver).move_to_element(cat)
        hover.perform()
        currTeams = driver.find_elements('css selector', '.components-GTFullWidthList-GTFullWidthList-module__link')
        leagues[cat.text] = {f'{currTeam.text}': f'{currTeam.get_attribute("href")}' for currTeam in currTeams if currTeam.text != ''}

    return leagues
    

if __name__ == '__main__':

    driver = uc.Chrome(headless=False)
    leagues = get_leagues(driver)
    pprint.pprint(leagues)
        
        