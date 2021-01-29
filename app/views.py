from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from home.models import data
import smtplib
import time
import schedule

# Create your views here.
#def home(request):
#   return HttpResponse("hello from home function")

def sendmail(desire_price,price_info,title_info,rec_mail,link,choice):
    if (desire_price >= price_info):
        company=['amazon','flipkart','snapdeal']
        server = smtplib.SMTP('smtp.gmail.com', 587)
        sender_mail = "gattuajugiya@gmail.com"
        password = "gattu@2001"
        message = f"{title_info} is now {price_info}"
        server.starttls()
        server.login(sender_mail, password)
        print("successful login!")
        server.sendmail(sender_mail, rec_mail,
                        msg=f"Subject:{company[choice]} Price Alert!\n\n{message}\n\n here is the link:{link}")
        print("check your mailbox")

def home(request):
    return render(request,'index.html')

def amazon(request):
    if request.method=="POST":
        email=request.POST['amazonid']
        link=request.POST['amazonproduct']
        price1=int(request.POST['amazonprice'])
        
        #webscraing part
        chrome_path="D:\project\web driver\chromedriver.exe"
        driver=webdriver.Chrome(executable_path=chrome_path)
        try:
            driver.get(link)
            price=driver.find_element_by_id('priceblock_ourprice')
            str=price.text.split()[1].replace(",", "")
            title=driver.find_element_by_id('productTitle')
            price_info=int(float(str))
            title_info=title.text
            temp='amazon'
            a=data(cust_email=email,cust_pro_link=link,cust_pro_price=price1,company=temp)
            a.save()
            sendmail(price1,price_info,title_info,email,link,0)
        except:
            try:
                driver.get(link)
                price = driver.find_element_by_id('priceblock_dealprice')
                str = price.text.split()[1].replace(",", "")
                title = driver.find_element_by_id('productTitle')
                price_info=int(float(str))
                title_info=title.text
                temp='amazon'
                a=data(cust_email=email,cust_pro_link=link,cust_pro_price=price1,company=temp)
                a.save()
                sendmail(price1,price_info,title_info,email,link,0)
            except:
                print('Try again :(')
        
    return render(request,'amazon.html')
def flipkart(request):
    if request.method=="POST":
        email=request.POST['flipkartid']
        link=request.POST['flipkartproduct']
        price1=int(request.POST['flipkartprice'])
        temp='flipkart'
        chrome_path="D:\project\web driver\chromedriver.exe"
        driver=webdriver.Chrome(executable_path=chrome_path)
        
        driver.get(link)
        price=driver.find_element_by_class_name('_16Jk6d')
        title=driver.find_element_by_class_name('B_NuCI')
        str = price.text.split()[0].replace("₹", "")
        str=str.replace(",","")
        price_info=int(float(str))
        title_info=title.text
        a=data(cust_email=email,cust_pro_link=link,cust_pro_price=price1,company=temp)
        a.save()
        
        sendmail(price1,price_info,title_info,email,link,1)
        

    return render(request,'flipkart.html')    
def snapdeal(request):
    if request.method=="POST":
        email=request.POST['snapdealid']
        link=request.POST['snapdealproduct']
        price1=int(request.POST['snapdealprice'])
        temp='snapdeal'
        chrome_path="D:\project\web driver\chromedriver.exe"
        driver=webdriver.Chrome(executable_path=chrome_path)
        driver.get(link)
        price=driver.find_element_by_class_name('payBlkBig')
        str=price.text.split()[0].replace(",","")
        title=driver.find_element_by_class_name('pdp-e-i-head')
        price_info = int(float(str))
        title_info = title.text
        a=data(cust_email=email,cust_pro_link=link,cust_pro_price=price1,company=temp)
        a.save()
       
        sendmail(price1,price_info,title_info,email,link,2)
    return render(request,'snapdeal.html')
