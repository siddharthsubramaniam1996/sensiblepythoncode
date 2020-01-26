import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# #ACCEPTING INPUTS
uname=input("ENTER USERNAME: ")
passwd=input("ENTER PASSWORD :")
pname=input("ENTER PROJECT NAME: ")

browser = webdriver.Firefox()
browser.get('https://onex.osourceglobal.com/MZSK/Attendance/frmEmpSelfAttendance.aspx')

#ENTERING THE USER ID
username=browser.find_element_by_id('Login1_UserName')
username.send_keys(uname)

#ENTERING THE PASSWORD
password=browser.find_element_by_id('Login1_Password')
password.send_keys(pass)


#CLICKIKING THE LOGIN BUTTON
loginbutton=browser.find_element_by_id('Login1_LoginButton')
loginbutton.click()

#CLICKING THE SESSION OK BUTTON
sessionokbutton=browser.find_element_by_id('imgOkBtn')
sessionokbutton.click()


#CLICKING THE HUMAN RESOURCES BUTTON
hrbutton=browser.find_element_by_id('ctl00_ImgBtn_HR')
hrbutton.click()

browser.get('https://onex.osourceglobal.com/MZSK/Attendance/frmEmpSelfAttendance.aspx')

#SELECTING THE OPTION
optionselect=Select(browser.find_element_by_id('ctl00_ContentPlaceHolder_dtgAttendance_ctl03_DrpDwnStatus'))
optionselect.select_by_value('PS005553')
browser.minimize_window


#FILLING IN THE REMARKS ENTRY - NOT WORKING AS OF NOW
textentry=browser.find_element_by_id('ctl00_ContentPlaceHolder_dtgAttendance_ctl03_TxtRemarks')

#FILLINF IN THE REMARKS- 2nd attempt - not working
textentry=browser.find_element_by_name('ctl00$ContentPlaceHolder$dtgAttendance$ctl03$TxtRemarks').send_keys(pname)
textentry.click()
time.sleep(5)
