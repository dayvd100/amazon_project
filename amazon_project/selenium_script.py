from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

def search_amazon_product(produto):
    browser = webdriver.Chrome()
    results = []

    try:
        browser.get('https://www.amazon.com.br/')

        search_box = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="twotabsearchtextbox"]'))
        )

        search_box.clear()
        search_box.send_keys(produto)

        btn_search = browser.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]')
        btn_search.click()

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="a-section a-spacing-base"]'))
        )

        price_products = browser.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
        products_name = browser.find_elements(By.XPATH, '//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]/a/span')
        avaliations_products = browser.find_elements(By.XPATH, '//span[contains(@class, "a-icon-alt")]')

        for price, name, avaliation in zip(price_products, products_name, avaliations_products):
            results.append(f'{name.text};{price.text};{avaliation.get_attribute("textContent")[0:3]}')

    except Exception as e:
        results = [f"Ocorreu um erro: {str(e)}"]

    finally:
        browser.quit()
        print(results)

    return results

def save_to_csv(results, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Product Name", "Price", "Rating"])
        for result in results:
            writer.writerow(result.split(';')) 

results = search_amazon_product("Monitor")
save_to_csv(results, "amazon_products.csv")
