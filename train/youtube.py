from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = '../chromedriver-mac-x64/chromedriver'
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.youtube.com")

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".yt-spec-touch-feedback-shape.yt-spec-touch-feedback-shape--touch-response-inverse"))
)
element.click()

input_element = driver.find_element(By.NAME, "search_query")
input_element.clear()
time.sleep(2)
input_element.send_keys(
    "The Amazing World of Gumball | I'm On My Way | Cartoon Network")
time.sleep(2)
button_element = driver.find_element(By.ID, "search-icon-legacy")
button_element.click()

video_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                "//yt-formatted-string[contains(text(), \"I'm On My Way\")]"))
)
video_element.click()

while True:
    try:
        # Votre code ici
        print("Le programme est en cours d'exécution...")

    except KeyboardInterrupt:
        print("Interruption par l'utilisateur. Le programme va s'arrêter.")
        break
