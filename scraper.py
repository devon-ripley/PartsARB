from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

def time_randomizer(times):
    per = random.randrange(1, 20)
    ran_time = times * ((per * 0.01) + 1)
    print(f'Sleep {times} randomized to {ran_time}')
    time.sleep(ran_time)

def scrape_ebay(num_pages, search_term, debug=False):
    # random set up
    print(f'Scraping: {search_term}')
    driver = webdriver.Firefox()
    driver.get("https://www.ebay.com/b/Auto-Parts-Accessories/6028/")
    time_randomizer(1)
    elem = driver.find_element(By.ID, "gh-ac")
    time_randomizer(1)
    elem.clear()
    time_randomizer(1)
    elem.send_keys(search_term)
    elem.send_keys(Keys.RETURN)
    time_randomizer(5)
    price_list = []
    for page in range(num_pages):
        time_randomizer(2)
        pageText = driver.find_element(By.XPATH, "/html/body").text
        time_randomizer(2)
        # skip first 6 '$'
        skip = 0
        read = False
        num_str = ''
        for char in pageText:
            if read:
                if char == ',':
                    continue
                if char == '.':
                    price_list.append(int(num_str))
                    num_str = ''
                    read = False
                if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    read = False
                if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    num_str += char
            if skip > 5 and char == '$':
                read = True
            elif char == '$':
                skip += 1
        #next page
        driver.find_element(By.XPATH, "//a[@type='next']").click()
    driver.close()
    time_randomizer(1)
    if debug:
        print(f'pageText:')
        print(pageText)
        print('price_list:')
        print(price_list)
    return price_list

def scrape_test(num_pages, search_term):
    scrape_ebay(num_pages, search_term, debug = True)

def run(num_pages, parts, cars):
    cars_dict = {}
    for car in cars:
        cars_dict[car] = {}
        for part in parts:
            search_term = car + part
            cars_dict[car][part] = scrape_ebay(num_pages, search_term)
            print(f'Scrape results: {search_term}')
            print(cars_dict[car][part])
    return cars_dict

if __name__ == '__main__':
    scrape_test(1, '1998 jeep wrangler fuel injectors')