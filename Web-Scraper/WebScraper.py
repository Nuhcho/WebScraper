from bs4 import BeautifulSoup
import requests
import csv

urls = input("Please input the website URLs separated by a comma and a space: ")
urlList = urls.split(", ")
tempValue = True
searchWords = input("Please input the search words that you want to search for separated by a comma and a space: ")
searchWordsList = searchWords.split(", ")
count = 0
totalCount = 0
listCount = 0
allValues = [[]]

while(tempValue): 
    for x in urlList:
        for y in searchWordsList:
            html = requests.get(x).text
            soup = BeautifulSoup(html, "html.parser")
            tags = soup.body.get_text().strip()
            while y in tags:
                tags = tags.replace(y, " ", 1)
                count+=1
                totalCount+=1
            allValues.append([f" {x}", f"  {y}" , f"  {count}"])
            count = 0
    tempValue = False

allValues.append([f" Total Occurences of word: {totalCount}"])

with open("searchWordCount.csv", "w", newline="") as searchWordCount:
    writer = csv.writer(searchWordCount)
    writer.writerow(["URL", " Word", " Amount of occurences"])
    writer.writerows(allValues)

