### Selenium Script Checking Google CSS properties
## This Selenium script uses the ChromeDriver to open the Chrome browser, navigate to the Google homepage, find the element with the id "hplogo" (which represents the Google logo), get the font-size and color CSS properties for that element, and verify that the values are correct.

Requirements
Selenium
ChromeDriver
Running the Script
To run the script, make sure you have installed the necessary requirements and have the ChromeDriver executable in your PATH. Then, run the script using Python:

Copy code
python google_logo_css_test.py
If the script runs successfully, you should see no output. If an assertion fails, you will see an error message indicating the expected and actual values for the failed property.

Here is a sample requirements.txt file that lists the necessary dependencies for the Selenium script:

Copy code
selenium
To install the dependencies, you can use the following command:

Copy code
pip install -r requirements.txt
