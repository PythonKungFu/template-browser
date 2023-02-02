import os
from selenium import webdriver
from selenium_stealth import stealth
from SeleniumAuthProxy import SeleniumAuthProxy
from config import ip, port, login, password


class Bot:
    driver: webdriver.Chrome
    proxy: SeleniumAuthProxy
    opts: webdriver.ChromeOptions
    # Proxy USA
    login = login
    password = password
    port = port
    ip = ip

    def __init__(self):
        self.proxy = SeleniumAuthProxy.get_proxy_object(self.ip, self.port, self.login, self.password, 'proxy')
        self.opts = webdriver.ChromeOptions()
        self.opts.add_extension(self.proxy)
        self.opts.add_argument("start-maximized")
        # Отключение ботовидимости
        self.opts.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.opts.add_experimental_option('useAutomationExtension', False)
        self.opts.add_argument("--disable-blink-features=AutomationControlled")
        # Сохранение профиля браузера с куками и всеми данными
        self.opts.add_argument(rf"user-data-dir={os.getcwd()}\User Data")
        self.driver = webdriver.Chrome(options=self.opts)
        # Подключение режима стелс
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

    def __del__(self):
        self.driver.close()
        self.driver.quit()
