# Mail-Spinny

Mail Spinny is a python utility script designed to automate the process of sending cold emails to different organizations/individuals. The script replaces specified words in the mail body (for example "company name," "contact number," and "contact name") with data from a CSV file containing the relevant information, and automatically send the mail to all the company mails listed in the CSV file.

The script can be used to send multiple emails with personalized information to different companies, making it a valuable tool for individuals or organizations seeking sponsorship, referrals, etc. This functionality allows users to create a personalized email template and automate the process of sending cold emails to multiple parties.

The script is is fully customizable and can be changed to the specific needs just by changing the column names in the csv files

In summary, this Python utility script project is an efficient way to automate the process of sending cold emails, reducing the time and effort required for manual processing. It is a valuable tool for individuals or organizations seeking sponsorship, providing a customizable and organized method for sending multiple emails to different organizations.


## Usage
1. Get the latest version of python (built with 3.11) and install numpy and pandas
2. Follow the steps in this documentation to get the Gmail API keys as a 'credentials.json' file: https://developers.google.com/gmail/api/quickstart/python
3. Authorize the mail that you will be using to send the emails as a test email from the google cloud console platform, and download the dependencies that are mentioned in the above documentation. 
3. Store the csv file that you want to use as 'data.csv' and store a 'body.txt' file in the same folder as the script(See the example files provided). The script will replace any words that match with the column names in 'data.csv' with their values in from the 'body.txt' file and send that mail to the 'company email'.
4. Run the 'send_mail.py' file.


## Example
Here is an example of the body and the subject file.
<img width="677" alt="body" src="https://user-images.githubusercontent.com/67830226/229368415-765d338f-9394-47ba-8b4a-a67939db226a.png">
<img width="296" alt="subject" src="https://user-images.githubusercontent.com/67830226/229368425-754c4359-9409-4115-8f65-df17e533858e.png">

Here is the data.csv file. Note that the column names here match the specific strings that we need to replace in the body of the mail.
<img width="922" alt="data" src="https://user-images.githubusercontent.com/67830226/229368419-f3381e77-f63b-4ee9-81d3-98cac72be6a2.png">

This is the output we will get after running the send_mail.py script and successfully authorizing the Gmail account.
<img width="741" alt="output" src="https://user-images.githubusercontent.com/67830226/229368423-caf268ae-4346-446a-9437-bace2bd6f130.png">

This is the sent mail. Note that the keywords are replaced as per the data file.
<img width="739" alt="sent_mail" src="https://user-images.githubusercontent.com/67830226/229368424-5bdb2757-7c01-40c2-b08c-e5f9b119fdc2.png">
