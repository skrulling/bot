

from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


#Hvor er listen


n = 1

toppliste1 = "//*[@id='tab-toplist-visited']/div[1]/ol/li["
toppliste2 = ']/a'
artikkel = ".//*[@id='main']/article[1]/h1/a"
artikkel2 = ".//*[@id='main']/div[1]/h2/a"
artikkel3 = "//*[@id='content']/div[1]/center/div/h3/a"
artikkel4 = ".//*[@id='overskrift']/h2/a"
navn = ".//*[@id='comment_author']"
mail = ".//*[@id='comment_authoremail']"
nettside = ".//*[@id='comment_authorurl']"
kommentar_felt = ".//*[@id='comment_text']"
kommentaren1 = "Hei, vi er en nyoppstartet side som lager headere og redigerer bilder gratis"
kommentaren2 = ", stikk innom www.espolin.net :D"
min_url = "espolin.net"
meg = "Espolin.net"
min_mail = "espolinproductions@gmail.com"
send_knapp = ".//*[@id='comment_submit']"
submit = ".//*[@id='publish']"
vis = ".//*[@id='tab-toplist-visited']/div[2]/p[1]/a"

a = "http://blogg.no/"
b = "http://blogg.no/f/13-17"
c = "http://blogg.no/f/18-24"
d = "http://blogg.no/f/25-39"
e = "http://blogg.no/f/40-100"
f = "http://blogg.no/m/13-17"
g = "http://blogg.no/m/18-24"
h = "http://blogg.no/m/25-39"
i = "http://blogg.no/m/40-100"

print("a="+a)
print("b="+b)
print("c="+c)
print("d="+d)
print("e="+e)
print("f="+f)
print("g="+g)
print("h="+h)
print("i="+i)

url = input("Pick which list to spam:")

start = input("Where to start?")
stop = input("Where to stop?")



print("Let the spam begin!")






browser = webdriver.Firefox()
browser.get(url)




for z in range(start,stop):
    x = n+z
    y=str(x)
    toppliste3 = toppliste1+y+toppliste2

    browser.find_element_by_xpath(vis).click()
    browser.implicitly_wait(1)

    browser.find_element_by_xpath(toppliste3).click()
    browser.implicitly_wait(5)
    print("trying to post at blogg number:"+y)


    try:
        #browser.find_element_by_xpath(artikkel).click()
        browser.find_element_by_xpath(artikkel2).click() and browser.find_element_by_xpath(artikkel).click()\
        and browser.find_element_by_xpath(artikkel3).click()\
        and browser.find_element_by_xpath(artikkel4).click()

        browser.implicitly_wait(2)

        try:

            browser.find_element_by_xpath(navn).send_keys(meg)
            browser.find_element_by_xpath(mail).send_keys(min_mail)
            browser.find_element_by_xpath(nettside).send_keys(min_url)
            browser.find_element_by_xpath(kommentar_felt).click()
            browser.find_element_by_xpath(kommentar_felt).send_keys(kommentaren1+kommentaren2)
            browser.find_element_by_xpath(send_knapp).click()

            browser.find_element_by_xpath(submit).click()
            print("Kommenterte paa blogg nummer "+y)
            browser.get(url)

        except NoSuchElementException:
            browser.get(url)

    except NoSuchElementException and WebDriverException:
        browser.get(url)







