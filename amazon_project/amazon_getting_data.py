from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from interface_data_products import search_product

browser = webdriver.Chrome()

try:
    browser.get('https://www.amazon.com.br/')

    search_box = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="twotabsearchtextbox"]'))
    )

    btn_search = browser.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]')

    product_search_by_client = input("Insira o nome do produto: ")

    search_box.send_keys(product_search_by_client)

    btn_search.click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="a-section a-spacing-base"]'))
    )

    price_products = browser.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
    products_name = browser.find_elements(By.XPATH, '//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]/a/span')

    for price, name in zip(price_products, products_name):
        print(f'Produto: {name.text}')
        print(f'R$ {price.text}')
        print()


    breakpoint()

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

finally:
    print("Encerrando o script...")
    browser.quit()