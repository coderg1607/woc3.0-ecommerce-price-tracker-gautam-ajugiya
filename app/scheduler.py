from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
import sys
from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from home.models import data
import smtplib
import time
import schedule

# This is the function you want to schedule - add as many as you want and then register them in the start() function below
def deactivate_expired_accounts():
    today = timezone.now()
    for i in data.objects.all():
        background(i.company,i.cust_email,i.cust_pro_link,int(i.cust_pro_price))
        time.sleep(20)



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # run this job every 24 hours
    scheduler.add_job(deactivate_expired_accounts, 'interval', hours=12, name='clean_accounts', jobstore='default')
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)

def background(company,cust_email,cust_pro_link,cust_pro_price):
    
    chrome_path="D:\project\web driver\chromedriver.exe"
    driver=webdriver.Chrome(executable_path=chrome_path)
#web driver setup
#closing tab
#schedule.every(12).hours.do(scraping)
    
    link=cust_pro_link
    if(company=='amazon'):
        try:
            driver.get(link)
            price=driver.find_element_by_id('priceblock_ourprice')
            str=price.text.split()[1].replace(",", "")
            title=driver.find_element_by_id('productTitle')
            price_info=int(float(str))
            title_info=title.text
        except:
            try:
                driver.get(link)
                price = driver.find_element_by_id('priceblock_dealprice')
                str = price.text.split()[1].replace(",", "")
                title = driver.find_element_by_id('productTitle')
                price_info=int(float(str))
                title_info=title.text
            except:
                print('Try again :(')

    elif(company=='flipkart'):
        try:
            driver.get(link)
            price=driver.find_element_by_class_name('_16Jk6d')
            title=driver.find_element_by_class_name('B_NuCI')
            str = price.text.split()[0].replace("₹", "")
            str=str.replace(",","")
            price_info=int(float(str))
            title_info=title.text
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
            
        except:
            print('Try again:(')

    desire_price =cust_pro_price
    rec_mail =cust_pro_link
    
    if(desire_price>=price_info):
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        sender_mail = "gattuajugiya@gmail.com"
        password = "gattu@2001"
        message = f"{title_info} is now {price_info}"
        server.starttls()
        server.login(sender_mail, password)
        print("successful login!")
        server.sendmail(sender_mail, rec_mail,
                        msg=f"Subject:{company} Price Alert!\n\n{message}\n\n here is the link:{link}")
        print("check your mailbox")
