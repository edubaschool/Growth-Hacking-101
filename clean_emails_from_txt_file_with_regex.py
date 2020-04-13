import re

emails = set()

with open("emails.txt", "r") as file:
	for line in file:
		if line in emails:
			continue
		else:
			verify_email = re.search(r"\w[\w\-\.]+\@\w+\.\w{1,4}", line)
			
			if verify_email is not None:
				found = verify_email.group() 
				emails.add(found)
			
with open("emails_cleaned.txt", "w") as exit_file:
	for email in sorted(emails):
		exit_file.write(email + "\n")
		
#L'execution doit se faire dans le même dossier !
