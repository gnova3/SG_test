import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np

def run_stress_test(driver_path="chromedriver.exe", model_name="Model 1"):
    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"chromedriver not fount in: {driver_path}")

    try:
        start_time = time.time()  
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
        driver.get("http://dcm-serious-game.tudelft.nl/model_specification")

        model_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'model-name_2'))
        )
        model_name_input.clear()
        model_name_input.send_keys(model_name)

        checklist_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'components-3_2'))
        )

        checkboxes = checklist_container.find_elements(By.CSS_SELECTOR, '#attributes-dropdown_2 input[type="checkbox"]')
        for checkbox in checkboxes:
            driver.execute_script("arguments[0].scrollIntoView();", checkbox)
            if not checkbox.is_selected():
                driver.execute_script("arguments[0].click();", checkbox)

        save_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'latex-button_2'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", save_button)
        driver.execute_script("arguments[0].click();", save_button)

        estimation_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'estimate_2'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", estimation_button)
        driver.execute_script("arguments[0].click();", estimation_button)

        end_time = time.time()

        time.sleep(20)

    finally:
        driver.quit()

    random = np.random.randint(0, 1000)

    with open(f"stress_test_{random}.txt", 'w') as f:
        f.write(f"Time taken: {end_time - start_time}")

    return end_time - start_time