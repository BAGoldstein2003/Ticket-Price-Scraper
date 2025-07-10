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
    leagues = [{'league': cat.text} for cat in subCategories]

    #loop through subcategories, saving each category and its teams to a list of dictionaries
    for idx, cat in enumerate(subCategories):
        ActionChains(driver).move_to_element(cat).perform()
        currTeams = driver.find_elements('css selector', '.components-GTFullWidthList-GTFullWidthList-module__link')
        leagues[idx]['teams'] = [currTeam.text for currTeam in currTeams if currTeam.text != '']
        time.sleep(0.5)

    #pretty-print results and return Sub-Categories
    pprint.pprint(leagues)
    return subCategories
    

if __name__ == '__main__':
    driver = uc.Chrome(headless=True)
    subCategories = get_leagues(driver)
        
        