from selenium import webdriver
from PIL import Image
from os import remove


def get_screen(web: str = 'https://banki24.by/exchange/currencymarket', width: int = 1024, height: int = 768):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(web)
        driver.set_window_size(width=width, height=height)
        driver.save_screenshot("my_screenshot.png")
        print('[!]Screenshot saved.')
    except Exception as ex:
        print(f'[!] Error: {ex}')
    finally:
        driver.quit()

def get_cutched_screenshot():
    img = Image.open('my_screenshot.png')
    im_crop = img.crop((266, 280, 995, 735))
    im_crop.save('cut.png', quality=100)
    remove('my_screenshot.png')
    print('[!]Screen successfully cut.')

def main():
    get_screen()
    get_cutched_screenshot()
    print('[!]Script executed')


if __name__ == '__main__':
    main()
