from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

def chat(name):

	# chrome driver
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get("https://web.whatsapp.com/")
	wait = WebDriverWait(driver, 600)

	condition=True
	while condition:
		print("1. Chat")
		print("2. Quit")
		option = int(input("Enter choice: "))
		# if option 1 is selected
		if option==1:
			# enter the name of the person by the user
			receiver =  str(name) #str(input("Enter the name of receiver: "))
			message = str(input("Enter your message: "))

			# finds the person and navigate to it
			x_arg = '//span[contains(@title, '+ '"' +receiver + '"'+ ')]'
			person_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
			print(receiver)
			person_title.click()

			# navigate to text part
			xpath = '//div[@class="_3u328 copyable-text selectable-text"]'
			message_area = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

			# sends message
			message_area.send_keys(message + Keys.ENTER)
		# if option 2 is selected
		if option==2:
			condition=False
			exit()
