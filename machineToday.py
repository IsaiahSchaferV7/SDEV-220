from datetime import datetime

today_string = open("today.txt", "r").read().strip()

datetime_object = datetime.strptime(today_string, "%m-%d-%Y")
print(datetime_object)