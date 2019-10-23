""" nasa06.py Harvest APOD from NASA and print cleanly"""
import requests

#!/usr/bin/python3
# define URL as global

NASAURL = "https://api.nasa.gov/planetary/apod?api_key="

def main():
    """ Code to talk to NASA APOD """
    with open("/home/student/nasa.creds", 'r') as ncreds:
        myapikey = ncreds.read().rstrip('\n')
    print(myapikey)
    # read in our nasa api key
    # append to our url
    # make an API request
    apod = requests.get(NASAURL+myapikey)
    # parse out json
    apod = apod.json()
    # print out date
    print(apod.get("date"))
    # print out explination
    print(apod.get("explanation"))
    # print out URL
    print(apod.get("hdurl"))

if __name__ == "__main__":
    main()
