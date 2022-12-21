from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome driver
driver = webdriver.Chrome('/Users/home/Documents/Development/googleCheck/chromedriver')

# Navigate to the Google homepage
driver.get("https://www.google.com/")

# Find the Google logo element
logo = driver.find_element(By.ID, "hplogo")

# Get the font-size of the logo
font_size = logo.value_of_css_property("font-size")

# Verify that the font-size is correct
try:
    assert font_size == "14px"
except AssertionError:
    print("Error: Unexpected font-size value")
    print("Expected: 14px")
    print("Actual: " + font_size)

# Get the color of the logo
color = logo.value_of_css_property("color")

# Verify that the color is correct
try:
    assert color == "rgba(32, 33, 36, 1)"
except AssertionError:
    print("Error: Unexpected color value")
    print("Expected: rgba(32, 33, 36, 1)")
    print("Actual: " + color)

# Close the browser
driver.quit()
