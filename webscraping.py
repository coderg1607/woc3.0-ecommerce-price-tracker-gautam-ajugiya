from selenium import webdriver
import smtplib
import time
import schedule

company=['Amazon','Flipkart','Snapdeal']

import json


chrome_path="E:\webdriver\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_path)
#web driver setup
#closing tab

newproduct=1
def scraping():
    newproduct=2

newproduct=int(input('Enter 1 for new product'))
schedule.every(12).hours.do(scraping)
if(newproduct==1):
    print("1:for amazon product\n2:flipkart product\n3:snapdeal product")
    choice=int(input("enter your choice:"))
    link=input('enter amazon product link:')
    if(choice==1):
        try:
            driver.get(link)
            price=driver.find_element_by_id('priceblock_ourprice')
            str=price.text.split()[1].replace(",", "")
            title=driver.find_element_by_id('productTitle')
            price_info=int(float(str))
            title_info=title.text
            print("price of product is:RS.",price_info)
            print("product name:",title_info)
        except:
            try:
                driver.get(link)
                price = driver.find_element_by_id('priceblock_dealprice')
                str = price.text.split()[1].replace(",", "")
                title = driver.find_element_by_id('productTitle')
                price_info=int(float(str))
                title_info=title.text
                print("price of product is:RS.",price_info)
                print("product name:",title_info )
            except:
                print('Try again :(')

    elif(choice==2):
        try:
            driver.get(link)
            price=driver.find_element_by_class_name('_16Jk6d')
            title=driver.find_element_by_class_name('B_NuCI')
            str = price.text.split()[0].replace("₹", "")
            str=str.replace(",","")
            price_info=int(float(str))
            title_info=title.text
            print("price of product is:",price_info,title_info)
        except:
            print('Try again :(')

    else:
        try:
            driver.get(link)
            price=driver.find_element_by_class_name('payBlkBig')
            str=price.text.split()[0].replace(",","")
            title=driver.find_element_by_class_name('pdp-e-i-head')
            price_info = int(float(str))
            title_info = title.text
            print("price of product is:", price_info, title_info)
        except:
            print('Try again:(')

    def write_json(data, filename='temp.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    with open('temp.json') as json_file:
        data = json.load(json_file)
        temp = data['details']
    # python object
        x = {"product_name":title_info,
         "url": link,
         "price":price_info ,
          "company":company[choice-1]
         }
        temp.append(x)
    write_json(data)


#messaging
    desire_price=int(input("enter your desire prise"))

    rec_mail=input("enter your username")

    if(desire_price>=price_info):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        sender_mail="kyakamhehamara@gmail.com"

        password="kyakamhe"

        message = f"{title_info} is now {price_info}"
        server.starttls()
        server.login(sender_mail,password)
        print("successful login!")
        server.sendmail(sender_mail,rec_mail,msg=f"Subject:{company[choice-1]} Price Alert!\n\n{message}\n\n here is the link:{link}")
        print("check your mailbox")
else:
    with open('temp.json') as data_file:
        data = json.load(data_file)
        for v in data.values():
            link=v['url']
            choice =company.index(v['company'])


    if (choice == 1):
        try:
            driver.get(link)
            price = driver.find_element_by_id('priceblock_ourprice')
            str = price.text.split()[1].replace(",", "")
            title = driver.find_element_by_id('productTitle')
            price_info = int(float(str))
            title_info = title.text

        except:
            try:
                driver.get(link)
                price = driver.find_element_by_id('priceblock_dealprice')
                str = price.text.split()[1].replace(",", "")
                title = driver.find_element_by_id('productTitle')
                price_info = int(float(str))
                title_info = title.text

            except:
                print('Try again :(')

    elif (choice == 2):
        try:
            driver.get(link)
            price = driver.find_element_by_class_name('_16Jk6d')
            title = driver.find_element_by_class_name('B_NuCI')
            str = price.text.split()[0].replace("₹", "")
            str = str.replace(",", "")
            price_info = int(float(str))
            title_info = title.text

        except:
            print('Try again :(')

    else:
        try:
            driver.get(link)
            price = driver.find_element_by_class_name('payBlkBig')
            str = price.text.split()[0].replace(",", "")
            title = driver.find_element_by_class_name('pdp-e-i-head')
            price_info = int(float(str))
            title_info = title.text

        except:
            print('Try again:(')

    # messaging
    desire_price = int(input("enter your desire prise"))

    rec_mail = input("enter your username")

    if (desire_price >= price_info):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        sender_mail = "kyakamhehamara@gmail.com"

        password = "kyakamhe"

        message = f"{title_info} is now {price_info}"
        server.starttls()
        server.login(sender_mail, password)
        print("successful login!")
        server.sendmail(sender_mail, rec_mail,
                        msg=f"Subject:{company[choice - 1]} Price Alert!\n\n{message}\n\n here is the link:{link}")
        print("check your mailbox")
