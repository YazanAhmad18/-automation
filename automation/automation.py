import re

def emails(file):
    email_regex = r"[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z0-9]+"
    list_emails = []

    with open(file,'r') as file:
        file = file.read()
        result_emailts = re.findall(email_regex, file)

    for email in result_emailts:
        if email not in list_emails:
            list_emails.append(email) 

    with open('emails.txt','w') as text_file:
        for email in sorted(list_emails):
            text_file.write(f"{str(email)}\n")

    return list_emails



def edit_format_phone_number(phone_number):
    if len(phone_number) == 7:
        phone_number = f"206{phone_number}"
    if "." in phone_number or  "(" in phone_number or ")" in phone_number or  "-" in phone_number:
        phone_number = phone_number.replace(".", "")
        phone_number = phone_number.replace("-", "")
        phone_number = phone_number.replace(")", "")
        phone_number = phone_number.replace("(", "")
      
    phone_number = f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"
    return phone_number



def phone(file):
    phone_regex = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    
    with open(file,'r') as file:
        file = file.read()
        phone_numbers = re.findall(phone_regex, file)

    with open('phone_numbers.txt','w') as phone_file:
        list_numbers = []
  
        for phone_number in phone_numbers:
            phone_number = edit_format_phone_number(phone_number) 

            if phone_number not in list_numbers:
                list_numbers.append(phone_number)
        
        for phone_number in sorted(list_numbers):
            phone_file.write(f"{phone_number}\n")

    return list_numbers



if __name__ == "__main__":
    print("Emails: \n", emails("./potential-contacts.txt"))
    print("Phone Numbers: \n", phone("./potential-contacts.txt"))
