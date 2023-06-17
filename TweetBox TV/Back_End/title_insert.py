import os

header = "title,created_at,followers_count,friends_count,text,latitude,longitude\n"

for filename in os.listdir("./"):
    if filename.endswith(".csv"):
        with open(filename, "r") as file:
            content = file.readlines()
        with open(filename, "w") as file:
            file.write(header)
            file.writelines(content)
