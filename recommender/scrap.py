from .models import details
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def image(id,link):
    print(id)
    df = pd.DataFrame(list(details.objects.filter(id=id).values()))
    print(df['image_link'][0])
    if df['image_link'][0]=='0':
        print('hiiiiiiii')
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome(r'E:\anaconda\chromedriver.exe')
        print('hello')
        #driver.maximize_window()
        driver.get(link)
        image=[]
        try:
            images = driver.find_element(By.XPATH,
                                         '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div[1]/div/div[1]/img')
            print('hii')
            image.append(images.get_attribute('src'))
        except:
            try:
                images = driver.find_element(By.XPATH,
                                             '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div/div[1]/div/div/div[1]/img')
                print('hiiiiooo')
                image.append(images.get_attribute('src'))
            except:
                try:
                    images = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div/div/div[1]/img')
                    print('hiiiiooo11111')
                    image.append(images.get_attribute('src'))
                except:
                    print('ddafds')
                    image.append('https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png')
        df =details.objects.get(id=id)
        print('kkk')
        df.image_link=image[0]
        print(image[0])
        df.save(update_fields=['image_link'])
        print('dsfhbdsjbf')
        df = pd.DataFrame(list(details.objects.filter(id=id).values()))
        print(df)
    return df['image_link'][0]