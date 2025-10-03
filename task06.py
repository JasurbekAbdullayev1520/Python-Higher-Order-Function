emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
reslut = filter(lambda email: email.endswith("@gmail.com"), emails)
print(list(reslut))