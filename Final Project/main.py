from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.headless = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = input("Enter the URL of the website you want to scrape: ")

try:
    driver.get(url)

    try:
        headlines = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, 'h3'))
        )

        if not headlines:
            print("No headlines found.")
        else:
            for index, headline in enumerate(headlines):
                print(f"{index + 1}. {headline.text.strip()}")

    except Exception as e:
        print(f"An error occurred while waiting for elements: {str(e)}")

finally:
    driver.quit()
