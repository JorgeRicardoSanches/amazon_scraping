from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import random
import xlsxwriter
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")

# driver.delete_all_cookies()
driver.get("https:\\facebook.com")

login_mail = "webdeveloper2843@gmail.com"
login_pass = "Hercules.1020"
newbusinessname = ["power washing", "clean", "cleaning", "construction", "home improvement", "janitorial", "roof", "flooring", "lawn care", "lawn", "spotless"]
# newbusinessname = ["clean"]

time.sleep(4)
try:
    # login
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(login_mail)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(login_pass)
    driver.find_element_by_xpath('//*[@id="u_0_b"]').click()

    for newbusinessnames in newbusinessname:
        time.sleep(4)
        driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[2]/div[2]/div/div/div[1]/div/div[3]/label/input').send_keys(newbusinessnames, Keys.ENTER)

        time.sleep(3)

        elems = driver.find_elements_by_css_selector("#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d2edcug0.rj1gh0hx.buofh1pr.g5gj957u.hpfvmrgz.dp1hu0rb > div > div > div > div > div > div > div > div:nth-child(1) > div > div > div > div.dhix69tm.sjgh65i0.wkznzc2l.tr9rh885 > a")
        links = [elem.get_attribute('href') for elem in elems]

        if driver.find_element_by_xpath("//a[contains(@class, 'oajrlxb2 tdjehn4e gcieejh5 bn081pho humdl8nn izx4hr6d rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l beltcj47 p86d2i9g aot14ch1 kzx2olss cbu4d94t taijpn5t ni8dbmo4 stjgntxs k4urcfbm tv7at329')]") != None:
            wait = WebDriverWait(driver, 20)
            Show10 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'oajrlxb2 tdjehn4e gcieejh5 bn081pho humdl8nn izx4hr6d rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l beltcj47 p86d2i9g aot14ch1 kzx2olss cbu4d94t taijpn5t ni8dbmo4 stjgntxs k4urcfbm tv7at329')]")))
            Show10.click()
        
        elif driver.find_element_by_xpath("//a[contains(@class, 'oajrlxb2 tdjehn4e qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 taijpn5t tv7at329 thwo4zme')]") != None:
            wait = WebDriverWait(driver, 20)
            Show10 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'oajrlxb2 tdjehn4e qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 taijpn5t tv7at329 thwo4zme')]")))
            Show10.click()
        
        # elif driver.find_element_by_xpath("//a[contains(@class, 'oajrlxb2 tdjehn4e qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 taijpn5t tv7at329 thwo4zme')]") != None and driver.find_element_by_xpath("//a[contains(@class, 'oajrlxb2 tdjehn4e gcieejh5 bn081pho humdl8nn izx4hr6d rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l beltcj47 p86d2i9g aot14ch1 kzx2olss cbu4d94t taijpn5t ni8dbmo4 stjgntxs k4urcfbm tv7at329')]") != None:
        #     wait = WebDriverWait(driver, 20)
        #     Show10 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'oajrlxb2 tdjehn4e gcieejh5 bn081pho humdl8nn izx4hr6d rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l beltcj47 p86d2i9g aot14ch1 kzx2olss cbu4d94t taijpn5t ni8dbmo4 stjgntxs k4urcfbm tv7at329')]")))
        #     Show10.click()

        # Scroll
 

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        results = soup.find_all("a", class_='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p dkezsu63')

        workbook = xlsxwriter.Workbook('URLs.xlsx')
        worksheet = workbook.add_worksheet("urls")
        
        row = 0
        column = 0
        
        for results_etc in results:
            print(results_etc['href'])
            driver.get(results_etc['href'])

            time.sleep(3)
            texts = driver.find_elements_by_xpath("//a[contains(@class, 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l dwo3fsh8 ow4ym5g4 auili1gw mf7ej076 gmql0nx0 du4w35lb g0qnabr5')]")
            for text in texts:
                if text.text == "About":
                    text.click()
                    break

            # time.sleep(5)
            # soup1 = BeautifulSoup(driver.page_source, 'html.parser')
            # about_info = soup1.findAll('div',{'class':'rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t buofh1pr muag1w35 enqfppq2'})
            # print(about_info)
            # if driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div/div[1]/div/div/div/div/div') != None:
            try:
                time.sleep(1)
                soup1 = BeautifulSoup(driver.page_source, 'html.parser')

                about_info = soup1.findAll('div',{'class':'rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t buofh1pr muag1w35 enqfppq2'})
                # print(about_info)
                if about_info[0].text.count("United States") > 0 and about_info[0].text.count("May 21, 2020") > 0:
                    print("ok1")
                    worksheet.write(row, 0, results_etc['href']) 
                    worksheet.write(row, 1, "United States") 
                    print("urls2: ", results_etc['href'])
                    row += 1
                        
                    # imgs = soup1.find_all("img", class_='hu5pjgll cwsop09l')
                    # if imgs['src'] == "https://static.xx.fbcdn.net/rsrc.php/v3/yf/r/4mSNCiGuFsr.png":
                    #     print(imgs.text)
            except:
                pass
            # elif driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div/div') != None:
            try:
                time.sleep(1)
                soup1 = BeautifulSoup(driver.page_source, 'html.parser')

                about_info = soup1.find('div',{'class':'db0gmjza d2edcug0 cbu4d94t j83agx80 cwj9ozl2'})
                # print(about_info)

                if about_info.text.count("United States") > 0 and about_info[0].text.count("May 21, 2020") > 0:
                    print("ok2")
                    worksheet.write(row, column, results_etc['href'])
                    print("urls2: ", results_etc['href'])
                    row += 1
            except:
                pass
            # elif driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div/div/div[4]/div/div[1]/div/div/div/div[2]') != None:
            try:
                time.sleep(1)
                soup1 = BeautifulSoup(driver.page_source, 'html.parser')

                about_info = soup1.find('div',{'class':'fjf4s8hc tu1s4ah4 f7vcsfb0 k3eq2f2k'})
                # print(about_info)

                if about_info.text.count("United States") > 0 and about_info[0].text.count("May 21, 2020") > 0:
                    print("ok3")
                    worksheet.write(row, column, results_etc['href'])
                    print("urls2: ", results_etc['href'])
                    row += 1
            except:
                pass
        workbook.close()

except NoSuchElementException:
    pass