#Task: clean and split emails into username and domain

def clean_and_split_email(email):
    Cleaned_email = email.strip().lower()
    username, domain = Cleaned_email.split("@")
    return {"Username": username, "Domain": domain}

print(clean_and_split_email("bovic2023@gmail.com"))