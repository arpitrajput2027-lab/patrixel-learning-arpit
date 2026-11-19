import requests
import csv


url = "https://dummyjson.com/quotes/random"

try:
    # send a api request
    response = requests.get(url, timeout=10)
  

    # check the http error
    response.raise_for_status()

    # json to dic
    data = response.json()
    # print(data) 

    # Required data extract and clean
    quote = data["quote"].strip()
    author = data["author"].strip()

    # save the recieved data in the csv
    with open("quotes.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([quote, author])

    print("Quote saved successfully!")

except requests.exceptions.RequestException:
    print("Data not fected .")

except (KeyError, TypeError, AttributeError, ValueError):
    print("Wrong Data in the Response.")

except OSError:
    print("CSV file Save Issue.")