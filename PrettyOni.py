from socket import timeout
from click import option
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
from pyfiglet import figlet_format



opt = webdriver.FirefoxOptions()
opt.set_preference("dom.webdriver.enabled", False)
browser = webdriver.Firefox(options=opt)



def quit():
    logQuit = input()
    if logQuit=="y":
        browser.quit()
    else:
        quit()

def trans():
    transp = input()
    if transp=="y" and frst=="1":
        buyall()
    elif transp=="y" and frst=="2":
        buyone()
    elif transp=="y" and frst=="3":
        buycustom()
    else:
        trans()

def tryClick():
    try:
        wait = WebDriverWait(browser, 10)
        Butt = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-ky47dt')))
        Butt.click()  
    except:
        time.sleep(1)
        tryClick()

def cookie():
    wait = WebDriverWait(browser, 10)
    Butt = wait.until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
    Butt.click()
    time.sleep(15)
    wait = WebDriverWait(browser, 10)
    Butt = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-1dn3rsy')))
    Butt.click()

def buybuy(browser):
        try:
            tryClick()
            print("Поздравляем с успешной покупкой!")
            print("Если работа окончена напишите y")
            quit()
        except:
            print("Кнопка еще не нажата")
            time.sleep(1)
            buybuy(browser)
            
def MaxBtn():
    try:
        wait = WebDriverWait(browser, 10)
        ButtMax = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-f2ec0a')))
        ButtMax.click()  
    except:
        time.sleep(1)
        MaxBtn()

def buyone():
    print("Введите ссылку на nft страницу")
    url = input()
    browser.get(url)
    time.sleep(10)
    cookie()
    print("Началась проверка кнопки покупки") 
    buybuy(browser)

def BuyCust(kolvo):
    try:
        wait = WebDriverWait(browser, 10)
        howmuch = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-cecccq')))
        for i in range(kolvo-1):
            howmuch.click()  
    except:
        time.sleep(1)
        BuyCust(kolvo)

def buycustom():
    print("Введите ссылку на nft страницу")
    url = input()
    print("Сколько nft надо купить?")
    kolvo = int(input())
    browser.get(url)
    time.sleep(10)
    cookie()
    print("Началась проверка кнопки покупки") 
    BuyCust(kolvo)
    buybuy(browser)

def buyall():
    print("Введите ссылку на nft страницу")
    url = input()
    browser.get(url)
    time.sleep(10)
    cookie()
    MaxBtn()
    print("Началась проверка кнопки покупки") 
    buybuy(browser)


def login():
    browser.get("https://accounts.binance.com/en/login")
    print("Если вы вошли напишите y")
    trans()


def vybor():
    print("Введите 1, чтобы купить все доступные nft, 2 чтобы купить одно nft, 3 для покупки определенного кол-ва nft.\nВведите e чтобы выйти")
    print("")
    global frst 
    frst = input()
    if frst=="1":
        login()
        return frst
    elif frst=="2":
        login()
    elif frst=="3":
        login()
    elif frst=="e":
        browser.quit()
    else:
        vybor()

print(figlet_format("PrettyOni", font = "doom"), "\n" )
print("Release version 6.0.0 \n \n ")
vybor()

    



