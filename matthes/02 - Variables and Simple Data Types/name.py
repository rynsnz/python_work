first_name = "  ada"
last_name = "lovelace  "
first_name = first_name.strip()
last_name = last_name.strip()
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)