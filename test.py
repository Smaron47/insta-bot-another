# import requests
# import re

# def extract_emails_from_text(text):
#     email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#     emails = re.findall(email_pattern, text)
#     return emails

# def process_csv_file(input_file, output_file):
#             link=input_file
#             response = requests.get(f"https://{link}/")
#             if response.status_code == 200:
#                     emails = extract_emails_from_text(response.text)
#                     email_string = ', '.join(emails)
#                     print(f"Processed: {link} email: {email_string}")
#             else:
#                     print('Error')
            
            
            
# k="businessplus.es"           
# process_csv_file(k,'')


global p
p=0

def k():
        global p
        p=p+1

for i in range(0,49):
        if p<10:
                print(p)
                k()