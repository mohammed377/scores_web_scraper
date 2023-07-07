from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from .models import 
driver = webdriver.Chrome()

# Enter value in input
value = 230001

while value <= 230620:
    driver.get("http://app1.helwan.edu.eg/FaslAU/EngHelwan/HasasnUpMlist.asp")
    reset = driver.find_element(By.NAME,"Reset")
    reset.click()
    try:
        input = driver.find_element(By.NAME,"x_st_settingno")
        input.send_keys(value)

        # Click submit button    
        button = driver.find_element(By.ID,"Submit")
        button.click()

        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="معاينة"]'))
        )

        # Click link
        link.click()

        # Get URL of current page 
        name=driver.find_element(By.TAG_NAME,"form").find_elements(By.TAG_NAME,"table")[0].find_elements(By.TAG_NAME,"tr")[2].find_elements(By.TAG_NAME,"td")[1]
        # Get all tr elements from index 2 to 4 (inclusive)
        grades = driver.find_elements(By.TAG_NAME,"table")[2].find_elements(By.TAG_NAME,"tr")[2:7]
        sum =0
        for grade in grades:
            # Get the 3rd td element (index 2)
            td = grade.find_elements(By.TAG_NAME,"td")[3]  
            sum += int(td.text.strip()) 
   

        print(f"{name} score is {sum}/750")
        

        value +=1
    except:
        value+=1
        continue
