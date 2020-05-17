from bs4 import BeautifulSoup as soup
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import requests
import re
import random
import xlwt
import time

# generage the xls file and define the title
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Sheet Name')

style = xlwt.easyxf('font: bold 1')

titles=['P url', 'C1', 'C2', 'C3', 'C4', 'C5', 'Asin', 'Title', 'Brand', 'Product Summary','Product Description','Product information', 'Shipping Weight','Product Dimensions','Price', 'ERP','Sale', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'imaage7']

row=0
col=0
for title in titles:
  worksheet.write(row, col, title, style)
  col += 1
page_url = "https://www.amazon.co.uk/s?i=electronics&bbn=3581866031&pf_rd_i=3581866031&pf_rd_m=A3P5ROKL5A1OLE&pf_rd_p=e15e0137-54cc-4cc7-ad74-4fb4410de3b4&pf_rd_r=10CW948YZXHD6K1HD854&pf_rd_s=merchandised-search-5&pf_rd_t=101&ref=s9_acss_bw_cg_AWUK20_1c1_w"

# setup proxy
proxies = [
  "18.204.70.192:3128",
  # "74.121.98.90:8080",
  # "35.187.58.241:3128",
  # "64.225.84.202:3128",
  # "69.162.89.243:5836",
  # "6.42.50.30:8080",
  # "18.237.67.131:3128"
]

def proxy_init():
  current_proxy = random.choice(proxies)
  proxy = {
          "http": "http://{}".format(current_proxy),
          "https": "https://{}".format(current_proxy)
  }
  session = requests.Session()
  session.proxies = proxy
  return session
driver = webdriver.Chrome("E:/working_folder/amazon_scraping/chromedriver.exe")
def main(define_url, row, page_number):
  
  # driver.delete_all_cookies()
  # time.sleep(5)
  driver.get(define_url)
 
  # _session = proxy_init()
  # product_list_page = _session.get(define_url, headers = {'user-agent': 'Mozilla/5.0'})
  page_number += 1
  print("------------------------------------"+str(page_number)+"th page---------------------------------------------")
  product_content_list = soup(driver.page_source, 'html.parser')
  if (product_content_list.find('li',{'class':'a-last'}).a != None):
    page_num = product_content_list.find('li',{'class':'a-last'})
    url = "https://www.amazon.co.uk/" + page_num.a['href']
    product_lists = product_content_list.findAll('h2',{'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'})
    if (row == 0):
      time.sleep(3)
    for x in range(len(product_lists)):
      col = 0
      row += 1
      print(str(row)+"th product")
      product_info = ['','','','','','','','','','','','','','','','','','','','','','','','']
      product_info[0] = "https://www.amazon.co.uk/" +product_lists[x].a['href']
      driver.get(product_info[0])
      if (row==1):
        time.sleep(5)
      time.sleep(1)
      product_page_response = driver.page_source

      product_content = soup(product_page_response, 'html.parser')

      product_info[7] = re.sub('\s\s+',' ',product_content.find(id = 'productTitle').text)
      try:
        product_info[8] = product_content.find(id = 'bylineInfo').text.replace('Visit the ','').replace(' Store','')
      except:
        pass
      if(product_content.find(id = 'priceblock_ourprice') != None):
        product_info[14] = product_content.find(id = 'priceblock_ourprice').text
      if(product_content.find('span', {'class': "priceBlockStrikePriceString a-text-strike"}) != None):
        product_info[15] = product_content.find('span', {'class': "priceBlockStrikePriceString"}).text
        if(product_content.find('td', {'class': "priceBlockSavingsString"}) != None):
          product_info[16] = product_content.find('td', {'class': "priceBlockSavingsString"}).text

      # get image list
      image_list=[]
      image_lists = product_content.findAll('li', {'class': "imageThumbnail"})
      
      for x in range(len(image_lists)):
        if(x<7):
          image_list.append(image_lists[x].find('img')['src'])
      index = 17
      for x in range(len(image_list)):
        product_info[index] = image_list[x]
        index += 1

      # get product_dimension, weight, asin 
      if (product_content.find(id = 'productDetailsTable') != None):
        detail_list = product_content.find(id = 'productDetailsTable').findAll('li')
        for li_val in detail_list:
          if (li_val.text.count("Dimensions") > 0):
            product_info[13] = li_val.text.replace(li_val.b.text, '')
          elif (li_val.text.count("Weight") > 0):
            product_info[12] = li_val.text.replace(li_val.b.text, '')
          elif (li_val.text.count('ASIN') > 0):
            product_info[6] = li_val.text.replace(li_val.b.text, '')

      if (product_content.find('div',{'class':'wrapper GBlocale'}) != None ):
        info_list = product_content.find('div',{'class':'wrapper GBlocale'}).findAll('td')
        for x in range(len(info_list)):
          if(info_list[x].text == "Package Dimensions"):
            product_info[13] = info_list[x+1].text
          elif(info_list[x].text == "Item Weight"):
            product_info[12] = info_list[x+1].text
          elif(info_list[x].text == "ASIN"):
            product_info[6] = info_list[x+1].text

      # get description, information, summary 
      if (product_content.find('div',{'class':'wrapper GBlocale'}) != None):
        if (product_content.find(id = 'productDescription') != None):
          product_info[10] = product_content.find(id = 'productDescription').text
      if (product_content.find('div',{'class':'wrapper GBlocale'})):
        product_info[11] = product_content.find('div',{'class':'wrapper GBlocale'}).text
      try:
        product_info[9] = product_content.find('ul',{'class':'a-unordered-list a-vertical a-spacing-mini'}).text
      except:
        pass
      for product_item in product_info:
        worksheet.write(row, col, product_item)
        col += 1
        workbook.save("amazon_product_info.xls")
    main(url, row, page_number)
main(page_url,0,0)

