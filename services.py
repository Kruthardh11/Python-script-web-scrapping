from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.common.by import By

# Set up the WebDriver
s = Service("C:/Users/kruth/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Navigate to the web page
driver.get("https://hfrs.moh.go.tz/web/index.php?r=portal%2Fadvanced-search")

# Add an implicit wait of, for example, 10 seconds
driver.implicitly_wait(10)

result_list = []
services_list =[]
facility_codes = []

try:
    # Initialize a list to store button information
    button_info_list = []
    # Loop through indices 1 to 20
    for index in range(1, 21):
        # Construct the XPath for the button with the current index
        button_xpath = f'//*[@id="w0-container"]/table/tbody/tr[{index}]/td[11]/button'
        wait = WebDriverWait(driver, 10)
        # Find and click the button
        button = driver.find_element("xpath", button_xpath)
        button.click()

        # Add a short sleep to allow the details to load (you can replace this with a WebDriverWait)
        time.sleep(4)

        # Find the div element with the details by XPath
        details_div = driver.find_element("xpath", '//*[@id="display_message_data"]/div/div[2]/div[1]/div[1]')
        wait = WebDriverWait(driver, 10)
        services_table = wait.until(EC.presence_of_element_located(("xpath", '/html/body/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody')))  
        # Get the text of the div
        details_text = details_div.text
        services_text = services_table.text
        rows = services_table.find_elements(By.TAG_NAME, 'tr')
        # Initialize a dictionary to store the data for this button
        lines = details_text.strip().split('\n')

        result = {}
        current_key = None

        # Define the keys
        keys = [
            'Facility Name', 'Common Name', 'Status', 'Facility Code', 'Date Opened',
            'Facility Type', 'Ownership', 'Address', 'Official Phone', 'Website',
            'In-Charge Qualification', 'CTC ID', 'Nearest Facility', 'MSD ID', 'MTUHA ID',
        ]

        services_data = {}
        current_key1 = None
        for row in rows:
                columns = row.find_elements(By.TAG_NAME, 'td')
                # Check the number of columns
                if len(columns) == 3:
                # If there are three columns, check if the text in the second column matches the current key
                        if columns[1].text == current_key1:
                     # If it matches, append the text in the third column to that key
                             services_data[current_key1].append(columns[2].text)
                        else:
                     # If it doesn't match, update the current key and create a new list with the value
                             current_key1 = columns[1].text
                             services_data[current_key1] = [columns[2].text]
                elif len(columns) == 2 and current_key1:
                  # If there are two columns, the text in the second column becomes a value for the current key
                         services_data[current_key1].append(columns[1].text)
        # Process the first line separately
        first_line = lines[0].split(':')
        result[first_line[0].strip()] = first_line[1].strip()

        # Iterate through the lines and populate the dictionary
        for line in lines:
            line = line.strip()
            if line in [
                'Common Name', 'Status', 'Facility Code', 'Date Opened',
                'Facility Type', 'Ownership', 'Address', 'Official Phone', 'Website',
                'In-charge Qualification', 'CTC ID', 'Nearest Facility', 'MSD ID', 'MTUHA ID'
            ]:
                current_key = line
                result[current_key] = ''
            else:
                result[current_key] = line
    
        back_button = driver.find_element("xpath", '/html/body/div/div/div[1]/div[2]/nav/ul/li[2]/a')
        back_button.click()
        
        result_list.append(result)
        facility_codes.append(result['Facility Code'])
        services_list.append(services_data)
        print(result['Facility Name'], "\n")
        #print("\n")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    df_result = pd.DataFrame.from_records(result_list)
    df_services = pd.DataFrame.from_records(services_list)
    df_services['Facility Code'] = facility_codes
    df_result.rename(columns= {None:'Common Name'}, inplace=True) 

#To make two sheets in an excel file using datad frames
    with pd.ExcelWriter("Final_data.xlsx", engine='xlsxwriter') as writer:
         df_result.to_excel(writer, sheet_name='Facility Details Sheet', index=False)

         df_services.to_excel(writer, sheet_name="Facility Services Sheet", index=False)

    driver.quit()  #close the WebDriver
