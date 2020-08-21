import requests

#TODO - Add feature to check for 'live' or not, and define the request payload
#Check the geckodriver

	#Add your own login url here
login_url = "http://172.172.172.100:8090/httpclient.html"
username = "<your_username_OR_enrollmentNum>"
passwd = "<your_password>"

global login_session
login_session = requests.Session()

	#This is login without a browser
def requests_login(action_val): #action_val=0 means login
    header = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
    }

    form_data = {
        "mode":"191",
        "username": username,
        "password": passwd,
	    #On our LAN login page, the form had this 'a' field (was hidden), you will have to find yours LOGIN page form tag
        "a":"1581616003458",	
        "producttype":"0"
        }

    global login_session
    if action_val == 0:
        login_resp = login_session.get(login_url, headers = header)
        #page_soup = BeautifulSoup(login_resp.content, 'html5lib')
        #form_a_element = page_soup.find('input', attrs = { '' : '' })
        login_resp = login_session.post(login_url, data = form_data, headers = header)
        print(login_resp)
    elif action_val == 1:
        logout_resp = login_session.post(login_url, data = logout_data, headers = header)
        print(logout_resp)

	#This is automated login on browser, this requires research on finding login on your side 
def selenium_login():
    import selenium
    from selenium import webdriver
    import time

	#GeckoDriver(in case of firefox, for chrome, use the chrome webdriver) path
    path_to_geckodriver = r"C:\Users\adity\Desktop" #the r'' allows us to pass backslash instead of forwardslash
    ######SHOWING DIRECTORY NAME INVALID, EVEN THOUGH LOCATION VERIFIED
    global __userid
    global __passwd

    def try_cred():
        global __userid
        global __passwd
        __userid = "<your_username_OR_enrollmentNum>"
        __passwd = "<your_password>"

    def get_cred():
        global __userid
        global __passwd
        __userid = input("Enter your UserID")
        __passwd = input("Enter the Password : ")

    def login():
        try:
	        userid = web_driver.find_element_by_name('username')   #given in captive portal one was that use find_by_name
	        passid = web_driver.find_element_by_name('password')
	        signinButton = web_driver.find_element_by_name('btnSubmit')

	        userid.send_keys(__userid)
	        passid.send_keys(__passwd)
	        signinButton.click()
	        time.sleep(3)     #rjust to make sure that the favourites page has opened up
	        print(web_driver.current_url)

        except Exception:
            print ("Some error!")
            return 1
        web_driver.quit()
        return 0    #Success

    web_driver = webdriver.Firefox()#path_to_geckodriver)
#    web_driver.manage().window().setPosition(Point(-2000,0))
    web_driver.get(login_url)
    try_cred()
    login()

requests_login(0)
print("You are already here, now do anything between these...")
input("When Done, press any key")
requests_login(1)
