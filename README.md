# Mail-Spinny

Mail Spinny is a python utility script designed to automate the process of sending sponsorship emails to different companies. The script replaces specified words such as "company name," "contact number," and "contact name" with data from a CSV file containing the relevant information, and automatically send the mail to all the company mails listed in the CSV file.

The script can be used to send multiple emails with personalized information to different companies, making it a valuable tool for individuals or organizations seeking sponsorship. This functionality allows users to create a personalized email template and automate the process of sending sponsorship requests to multiple companies.

The script is is fully customizable and can be changed to the specific needs just by changing the column names in the csv files

In summary, this Python utility script project is an efficient way to automate the process of sending sponsorship emails, reducing the time and effort required for manual processing. It is a valuable tool for individuals or organizations seeking sponsorship, providing a customizable and organized method for sending multiple emails to different companies.


## Usage
1. Get the latest version of python (built with 3.11) and install numpy and pandas
2. Follow the steps in this documentation to get the Gmail API keys as a 'credentials.json' file: https://developers.google.com/gmail/api/quickstart/python
3. Authorize the mail that you will be using to send the emails as a test email from the google cloud console platform, and download the dependencies from 
3. Store the csv file that you want to use as 'data.csv' and store a 'body.txt' file in the same folder as the script(See the example files provided). The script will replace any words that match with the column names in 'data.csv' with their values in from the 'body.txt' file and send that mail to the 'company email'.


