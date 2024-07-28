import sys
import webbrowser

urls = {
    "Work" : ["https://outlook.office.com", "https://calendar.google.com/calendar", "https://www.slack.com"],
    "Social" : ["https://www.facebook.com", "https://www.instagram.com", "https://www.twitter.com"],
    "Entertainment" : ["https://www.netflix.com","https://www.youtube.com", "https://www.disneyplus.com"]
}


def open_websites():
    print("Welcome to the website automator!")
    print("Here are the categories you can choose from:")
    for category in urls:
        print(category)
    category = input("Which category would you like to open? ")
    if category in urls:
        for url in urls[category]:
            webbrowser.open(url)
    else:
        print("Invalid category. Please try again.")
        open_websites()
    
open_websites()