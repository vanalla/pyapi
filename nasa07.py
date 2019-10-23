""" NASA NEO  """
import requests
import argparse

def main():
    """ Run the code """
    # def our url
    neourl = "https://api.nasa.gov/neo/rest/v1/feed?"
    #startdate = 'start_date=2019-10-15'
    startdate = 'start_date=' + args.start
    enddate   = '&end_date=END_DATE'
    mak = '&api_key='

    with open("/home/student/nasa.creds", 'r') as creds :
        myapikey = creds.read().rstrip('\n')
    myapikey = mak + myapikey

    # prompt user for start date
    # prompt user for end date
    # make our API requests
    neow = requests.get(neourl + startdate  + myapikey)
    # parse our json
    print(neow.json())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', help="provide a start date for us to search on YYYY-MM-DD")
    args = parser.parse_args()
    main()

