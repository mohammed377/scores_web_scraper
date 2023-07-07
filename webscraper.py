from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
logging.basicConfig(level=logging.INFO)

INPUT_LOCATOR = By.NAME, "x_st_settingno" 
SUBMIT_BUTTON_LOCATOR = By.ID, "Submit"
LINK_LOCATOR = By.XPATH, '//a[text()="معاينة"]'

driver = webdriver.Chrome() 

def get_name():
    return driver.find_element(By.TAG_NAME,"form").find_elements(By.TAG_NAME,"table")[0].find_elements(By.TAG_NAME,"tr")[2].find_elements(By.TAG_NAME,"td")[1].text

def get_score():
    grades = driver.find_elements(By.TAG_NAME,"table")[2].find_elements(By.TAG_NAME,"tr")[2:7]
    sum =0
    for grade in grades:
        td = grade.find_elements(By.TAG_NAME,"td")[3]  
        try:
            sum += int(td.text.strip())
        except ValueError:
            pass 
    return sum   

# Enter value in input
value = 230001

while value <= 230615:

    driver.get("http://app1.helwan.edu.eg/FaslAU/EngHelwan/HasasnUpMlist.asp")
    reset = driver.find_element(By.NAME,"Reset")
    reset.click()

    try: 
        input = driver.find_element(*INPUT_LOCATOR)
        input.send_keys(value)

        # Click submit button    
        button = driver.find_element(*SUBMIT_BUTTON_LOCATOR)
        button.click()

        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LINK_LOCATOR)
        )

        # Click link 
        link.click()
        
        name = get_name()
        score = get_score()   

        logging.info(f"{name} score is {score}/750")  
        
    except NoSuchElementException:
        logging.exception(f"Element with value {value} not found.") 
    except TimeoutException:
        logging.exception(f"Timed out waiting for page to load with value {value}.")
        
    value +=1  

    
