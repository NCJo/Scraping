# TODO: fully customized input

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import re
import json
import io


def searching_element_to_click(elem, sel):
        time.sleep(2)
        browser.find_element_by_xpath(elem).click()
        time.sleep(5)
        browser.find_element_by_xpath(sel).click()
        time.sleep(5)


browser = webdriver.Chrome('/Users/xyz/git/Scraping/Scraping/chromedriver')
url = 'http://stairways.org/Join/Find-a-Member'
time.sleep(2)
browser.get(url)
time.sleep(10)
main_page_repeat = 3

# use this var to track the "Show" selection
page = 0

# find all links in the main page
all_companies_links = []

for i in range(main_page_repeat):
    # finding 'Show' element to slect 1-46, 50-100, etc
    show = '//*[@id="idPagingData"]/select'
    select = ['STUB', '//*[@id="idPagingData"]/select/option[2]', '//*[@id="idPagingData"]/select/option[3]']

    # this to prevent clicking error
    if page != 0:
        selected_page = select[page]
        searching_element_to_click(show, selected_page)

    for a in browser.find_elements_by_xpath('//*[@title="Go to member details"]'):
       # need "get attribute" to get the actual content
       print(a.get_attribute('href'))
       all_companies_links.append(a.get_attribute('href'))

    page += 1

# close first session
browser.quit()
print("len of array is " + str(len(all_companies_links))) # temp

# set number of companies infos
numbCompanies = len(all_companies_links)
for i in range(numbCompanies):
    #TODO: move this out of for loop
    browser = webdriver.Chrome('/Users/xyz/git/Scraping/Scraping/chromedriver')

    url = all_companies_links[i]
    browser.get(url)
    time.sleep(10)

    ###############################################################################
    # Organization ###################################
    try:
        organization = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl00_TextBoxLabel887512"]')
        print(organization.text)
        organization_for_json = organization.text
    except:
        print("No Organization")
        pass
    ##################################################

    # Phone Number ###################################
    try:
        phone = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl01_TextBoxLabel887514"]')
        print(phone.text)
        phone_for_json = phone.text
    except:
        print("No Phone Number")
        pass
    ##################################################

    # Address ########################################
    try:
        address = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl02_TextBoxLabel7373682"]')
        print(address.text)
        address_for_json = address.text
    except:
        print("No Address")
        pass
    ##################################################

    # City ###########################################
    try:
        city = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl03_TextBoxLabel7373683"]')
        print(city.text)
        city_for_json = city.text
    except:
        print("No City")
        pass
    ##################################################

    # Province #######################################
    try:
        province = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl04_DropDownLabel7373684"]')
        print(province.text)
        province_for_json = province
    except:
        print("No Province")
        pass
    #################################################

    # Postal ########################################
    try:
        postal = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl05_TextBoxLabel7373685"]')
        print(postal.text)
        postal_for_json = postal
    except:
        print("No Postal")
        pass
    #################################################

    # Country #######################################
    try:
        country = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl06_DropDownLabel7373686"]')
        print(country.text)
        country_for_json = country
    except:
        print("No Country")
        pass
    #################################################

    # Website #######################################
    try:
        webCompany = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl07_TextBoxLabel887519"]/a')
        print(webCompany.text)
        URL_for_json = webCompany
    except:
        print("No Website")
        pass
    #################################################

    # Directory Listing text ########################
    try:
        directory = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl09_TextBoxLabel1182880"]')
        print(directory.text)
        directory_for_json = directory
    except:
        print("No Directory")
        pass
    #################################################

    # Business Tags #################################
    try:
        tags = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl11_BulletedList923216"]')
        print(tags.text)
        tags_filter = re.findall(r',?([^,]+)(?:,|\n)', tags.text)
        print(tags_filter)
        tags_for_json = tags_filter
    except:
        print("No Business Tag")
        pass
    #################################################

    time.sleep(2)

    for seatLink in allSeatLinks:
        # wait until element is visible
        visible = WebDriverWait(browser, 10).until(EC.visibility_of(seatLink))
        browser.execute_script("return arguments[0].scrollIntoView();", seatLink)
        browser.execute_script("window.scrollBy(0, -150);")
        visible.click()
        time.sleep(5)
        # plane type and flight number (read after click on "Seats")
        planeType = browser.find_elements_by_class_name('equipment-type')
        time.sleep(2)

        # match read connection flights to return correct flight numbers
        connection = re.findall(r'\b\d+\b',  flightConnections.pop(0).text)
        if len(connection) != 0:
            numOfConnection = int(connection.pop())
            numOfFlightConnectionJSON = numOfConnection
            flNum = flightNumbers.pop(0).text
            flNumJSON = flNum[7:]
            print(flNum[7:])
            for i in range(numOfConnection):
                flightNumbers.pop(0)
        else:
            numOfFlightConnectionJSON = 0
            flNum = flightNumbers.pop(0).text
            flNumJSON = flNum[7:]
            print(flNum[7:])
        # need try statement for plane type
        planeTypeJSON = planeType[-1].text
        print(planeType[-1].text)
        time.sleep(1)
        allSeats = browser.find_elements_by_class_name('seat')
        allOccupiedSeats = browser.find_elements_by_class_name('occupied')
        if flightNumberReplication(visitedFlightReplicate, flNum):
            for allSeatID in allSeats:
                if allSeatID._id not in visitedSeatIDArr:
                    visitedSeatIDArr.append(allSeatID._id)
                    allSeatsToCountArr.append(allSeatID)
            for occupiedSeatID in allOccupiedSeats:
                if occupiedSeatID._id not in visitedSeatIDArr:
                    visitedSeatIDArr.append(occupiedSeatID._id)
                    occupiedSeatsToCountArr.append(occupiedSeatID)
            # all the calculations for seats
            totalSeatsJSON = len(allSeatsToCountArr)
            occupiedSeatsJSON = len(occupiedSeatsToCountArr)
            emptySeatsJSON = len(allSeatsToCountArr) - len(occupiedSeatsToCountArr)

            # recording all the company informations ###########################
            try:
                data = {
                    'a. Company Name': organization_for_json,
                    'b. Phone Number': phone_for_json,
                    'c. Address': address_for_json,
                    'd. City': city_for_json,
                    'e. Province/State': province_for_json,
                    'f. Postal Code': postal_for_json,
                    'g. Country': country_for_json,
                    'h. Website': URL_for_json,
                    'i. Company Information': tags_for_json
                }
                dataArr.append(data)

            except:
                print("No data to record")
                pass

        else:
            print("Replicate Flight: not record")
            print("")
            pass

    with open('stairways_spider_result.json', 'a', encoding='utf8') as outfile:
        str_ = json.dumps(dataArr,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(str_)
            ####################################################################

    browser.close()



"""

"""
