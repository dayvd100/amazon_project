from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_amazon_product(produto):
    browser = webdriver.Chrome()

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

        results = []
        for price, name in zip(price_products, products_name):
            results.append(f'Produto: {name.text}\n')
            results.append(f'R$ {price.text}\n\n')

        return results

    except Exception as e:
        return [f"Ocorreu um erro: {str(e)}"]

    finally:
        browser.quit()
