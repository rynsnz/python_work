first_name = "  ryan"
last_name = "kelleher  "
first_name = first_name.lstrip()
last_name = last_name.rstrip()

full_name = f"{first_name} {last_name}"

message = f"Hello, {full_name.title()}!"

print(message)