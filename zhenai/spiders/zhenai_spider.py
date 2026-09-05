import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class ZhenaiSpiderSpider(scrapy.Spider):
    name = "zhenai_spider"
    allowed_domains = ["zhenai.com"]
    start_urls = ["https://www.zhenai.com/n/login"]

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def parse(self, response):
        self.driver.get(response.url)

        # 点击
        element = self.driver.find_element(By.XPATH, '//div[contains(@class, "tab-box")]//div[text()="账号密码登录"]')
        element.click()
        # xpath = response.xpath('//div[contains(@class, "tab-box")]//div[text()="账号密码登录"]')
        # xpath.click()
        # print(response.text)
        pass
