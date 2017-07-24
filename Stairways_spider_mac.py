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
        time.sleep(3)
        browser.find_element_by_xpath(sel).click()
        time.sleep(3)


browser = webdriver.Chrome('/Users/xyz/git/Scraping/Scraping/chromedriver')
url = 'http://stairways.org/Join/Find-a-Member'
time.sleep(2)
browser.get(url)
time.sleep(7)
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
print("Total number of companies: " + str(len(all_companies_links))) # temp

# total number of companies infos
numbCompanies = len(all_companies_links)
browser = webdriver.Chrome('/Users/xyz/git/Scraping/Scraping/chromedriver')

for i in range(numbCompanies):


    time.sleep(5)
    url = all_companies_links[i]
    browser.get(url)
    time.sleep(10)
    print("Company No.: " + i)
    # Organization ###################################
    try:
        organization = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl00_TextBoxLabel887512"]')
        print(organization.text)
        organization_for_json = str(organization.text)
    except:
        print("No Organization")
        organization_for_json = "No Organization"
        pass
    ##################################################

    # Phone Number ###################################
    try:
        try:
            phone = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl01_TextBoxLabel887514"]')
        except:
            try:
                phone = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl02_TextBoxLabel887514"]')
            except:
                try:
                    phone = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl03_TextBoxLabel887514"]')
                except:
                    try:
                        phone = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl04_TextBoxLabel887514"]')
                    except:
                        try:
                            phone = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl05_TextBoxLabel887514"]')
                        except:
                            try:
                                phone = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl06_TextBoxLabel887514"]')
                            except:
                                try:
                                    phone = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl07_TextBoxLabel887514"]')
                                except:
                                    pass

        print(phone.text)
        phone_for_json = str(phone.text)
    except:
        print("No Phone Number")
        phone_for_json = "No Phone Number"
        pass

    ##################################################

    # Address ########################################
    try:
        try:
            address = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl02_TextBoxLabel7373682"]')
        except:
            try:
                address = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl03_TextBoxLabel7373682"]')
            except:
                try:
                    address = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl04_TextBoxLabel7373682"]')
                except:
                    try:
                        address = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl05_TextBoxLabel7373682"]')
                    except:
                        try:
                            address = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl06_TextBoxLabel7373682"]')
                        except:
                            try:
                                address = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl01_TextBoxLabel7373682"]')
                            except:
                                pass
        print(address.text)
        address_for_json = str(address.text)
    except:
        print("No Address")
        address_for_json = "No Address"
        pass
    ##################################################

    # City ###########################################
    try:
        try:
            city = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl03_TextBoxLabel7373683"]')
        except:
            try:
                city = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl02_TextBoxLabel7373683"]')
            except:
                try:
                    city = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl04_TextBoxLabel7373683"]')
                except:
                    try:
                        city = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl05_TextBoxLabel7373683"]')
                    except:
                        try:
                            city = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl06_TextBoxLabel7373683"]')
                        except:
                            try:
                                city = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl07_TextBoxLabel7373683"]')
                            except:
                                try:
                                    city = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl08_TextBoxLabel7373683"]')
                                except:
                                    pass
        print(city.text)
        city_for_json = str(city.text)
    except:
        print("No City")
        city_for_json = "No City"
        pass
    ##################################################

    # Province #######################################
    try:
        try:
            province = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl04_DropDownLabel7373684"]')
        except:
            try:
                province = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl05_DropDownLabel7373684"]')
            except:
                try:
                    province = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl06_DropDownLabel7373684"]')
                except:
                    try:
                        province = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl03_DropDownLabel7373684"]')
                    except:
                        try:
                            province = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl07_DropDownLabel7373684"]')
                        except:
                            try:
                                province = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl08_DropDownLabel7373684"]')
                            except:
                                pass
        print(province.text)
        province_for_json = str(province.text)
    except:
        print("No Province")
        province_for_json = "No Province"
        pass
    #################################################

    # Postal ########################################
    try:
        try:
            postal = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl05_TextBoxLabel7373685"]')
        except:
            try:
                postal = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl03_TextBoxLabel7373685"]')
            except:
                try:
                    postal = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl04_TextBoxLabel7373685"]')
                except:
                    try:
                        postal = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl06_TextBoxLabel7373685"]')
                    except:
                        try:
                            postal = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl07_TextBoxLabel7373685"]')
                        except:
                            try:
                                postal = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl08_TextBoxLabel7373685"]')
                            except:
                                pass
        print(postal.text)
        postal_for_json = str(postal.text)
    except:
        print("No Postal")
        postal_for_json = "No Postal"
        pass
    #################################################

    # Country #######################################
    try:
        try:
            country = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl06_DropDownLabel7373686"]')
        except:
            try:
                country = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl05_DropDownLabel7373686"]')
            except:
                try:
                    country = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl04_DropDownLabel7373686"]')
                except:
                    try:
                        country = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl07_DropDownLabel7373686"]')
                    except:
                        try:
                            country = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl08_DropDownLabel7373686"]')
                        except:
                            try:
                                country = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl09_DropDownLabel7373686"]')
                            except:
                                pass
        print(country.text)
        country_for_json = str(country.text)
    except:
        print("No Country")
        country_for_json = "No Country"
        pass
    #################################################

    # Website #######################################
    try:
        try:
            webCompany = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl05_TextBoxLabel887519"]/a')
        except:
            try:
                webCompany = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl06_TextBoxLabel887519"]/a')
            except:
                try:
                    webCompany = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl07_TextBoxLabel887519"]/a')
                except:
                    try:
                        webCompany = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl08_TextBoxLabel887519"]/a')
                    except:
                        try:
                            webCompany = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl09_TextBoxLabel887519"]/a')
                        except:
                            try:
                                webCompany = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl10_TextBoxLabel887519"]/a')
                            except:
                                pass
        print(webCompany.text)
        URL_for_json = str(webCompany.text)
    except:
        print("No Website")
        URL_for_json = "No Website"
        pass
    #################################################

    # Directory Listing text ########################
    try:
        try:
            directory = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl07_TextBoxLabel1182880"]')
        except:
            try:
                directory = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl08_TextBoxLabel1182880"]')
            except:
                try:
                    directory = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl09_TextBoxLabel1182880"]')
                except:
                    try:
                        directory = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl10_TextBoxLabel1182880"]')
                    except:
                        try:
                            directory = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl06_TextBoxLabel1182880"]')
                        except:
                            try:
                                directory = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl11_TextBoxLabel1182880"]')
                            except:
                                pass


        directory_filter = directory.text
        directory_filter = directory_filter.replace("\n", " ")
        print(directory_filter)
        directory_for_json = str(directory_filter)
    except:
        print("No Directory")
        directory_for_json = "No Directory"
        pass
    #################################################

    # Business Tags #################################
    try:
        try:
            tags = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl07_BulletedList923216"]')
        except:
            try:
                tags = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl08_BulletedList923216"]')
            except:
                try:
                    tags = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl09_BulletedList923216"]')
                except:
                    try:
                        tags = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl10_BulletedList923216"]')
                    except:
                        try:
                            tags = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl11_BulletedList923216"]')
                        except:
                            try:
                                tags = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl12_BulletedList923216"]')
                            except:
                                try:
                                    tags = browser.find_element_by_xpath('//*[@id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl13_BulletedList923216"]')
                                except:
                                    pass
        tags_filter = tags.text
        tags_filter = tags_filter.replace("\n", " ")
        print(tags_filter)
        tags_for_json = str(tags_filter)
    except:
        print("No Business Tag")
        tags_for_json = "No Business Tags"
        pass
    #################################################
    print("Start JSON...") # temp
    # recording all the company informations ########
    dataArr = []
    try:
        data = {
            'a. Company Name': organization_for_json,
            'b. Phone Number': phone_for_json,
            'c. Address': address_for_json,
            'd. City': city_for_json,
            'e. Province': province_for_json,
            'f. Postal Code': postal_for_json,
            'g. Country': country_for_json,
            'h. Company Website': URL_for_json,
            'i. Directory Listing Text': directory_for_json,
            'j. Company Tags': tags_for_json,
            'k. Source URL': str(all_companies_links[i])
        }
        dataArr.append(data)
        for j in dataArr:
            print(dataArr[j])

    except:
        print("No data to record")
        pass

    time.sleep(2)
    with open('stairways_spider_result.json', 'a', encoding='utf8') as outfile:
        str_ = json.dumps(dataArr,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(str_)
        time.sleep(3)
    ################################################
    # temp developing
    # cancel = input("Stop? Y/N ")
    # print("")
    # if cancel == "y":
    #     browser.quit()
browser.quit()



"""

"""
