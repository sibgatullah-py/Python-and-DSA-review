import csv

name = input("Name : ")
home = input("Address : ")

with open("info.csv", "a", newline='') as file:
    write = csv.DictWriter(file, fieldnames=["name","home"])
    write.writerow({"name":name,"home":home})