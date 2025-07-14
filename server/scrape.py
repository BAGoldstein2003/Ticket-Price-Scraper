import time
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains

def gametime_get_leagues(driver: uc.Chrome):
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

def get_tickpix_price_from_url(url: str, amount: int):
    driver = uc.Chrome(headless=False)
    driver.get(url)
    time.sleep(5)
    
    #get Event Name and Listings
    eventName = driver.find_element('css selector', '#perfText').text
    listings = driver.find_elements('css selector', '.listing')

    #for each listing, compare price to desired amount, and add to list if price <= desired
    cheapTickets = []
    for listing in listings:
        if (listing.text[0] == '$'):
            listingPrice = listing.text.split(' ')[0]
            if int(listingPrice[1:]) <= amount:
                listingProps = listing.text.split('\n')
                listingSection = next((prop for prop in listingProps if prop.startswith("Sect")), 'General Admission')
                cheapTickets.append({'Section': listingSection, 'Price': listingPrice})

    #save data to dict format to be transmitted via API
    data = {
        'eventName': eventName,
        'threshold': amount,
        'cheapTickets': cheapTickets,
    }

    return data


    

if __name__ == '__main__':
    print(get_tickpix_price_from_url('https://www.tickpick.com/buy-atlanta-braves-vs-new-york-yankees-tickets-truist-park-7-20-25-1pm/6575147/', 60))