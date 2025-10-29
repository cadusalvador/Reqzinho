import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import log

def login_almox(driver, config):
    log("🌐 Acessando página de login...")
    driver.get(config["ALMOX_URL_LOGIN"])
    time.sleep(2)

    try:
        wait = WebDriverWait(driver, 30)
        email_input = wait.until([EC.presence_of_element_located((By.ID, "login_email"))])
        email_input.send_keys(config["ALMOX_USER"])
        password_input = wait.until([EC.presence_of_element_located((By.ID, "login_password"))])
        password_input.send_keys(config["ALMOX_PASSWORD"])

        driver.find_element(By.CLASS_NAME, "btn-login").click()
        
        log("✅ Login enviado. Aguardando autenticação...")
        time.sleep(5)
    except Exception as e:
        log(f"❌ Erro no login: {e}")
