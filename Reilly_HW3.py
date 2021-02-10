# Author:  Michael Reilly

# Purpose of Program: Analyze Youtube data based on a search term given by user, for 10 total entries

# Takes in a search term from command line, and then checks on Youtube for the videos relating to that search term.
# The basis of the youtube_search function come from youtube_data.py given to us, this is just it modified.
# The end results of the search are written to csvfile, which gets read by the function youtube_search_term_csv.
# 

# To run from terminal window:   python3 Reilly_HW3.py search_term num_terms

from googleapiclient.discovery import build      # use build function to create a service object
import argparse
import csv
import operator


# put your API key into the API_KEY field below, in quotes
API_KEY = "AIzaSyB_hD_A2lCAc77NL0U6UfyZhJ_I5ghODfM"

API_NAME = "youtube"
API_VERSION = "v3"       # this should be the latest version

#  function youtube_search retrieves the YouTube records

def youtube_search(s_term, s_max):
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)

    search_data = youtube.search().list(q=s_term, part="id,snippet", maxResults=s_max).execute()
    # Just a print for readability
    print("\nTerm: ", s_term)
    print("Number of Videos: ", s_max)

    # create the necessary CSV file output to be passed to youtube_search_term_csv
    csvFile=open('youtube_data.csv', 'w')
    # csvWriter is responsibly for writing the contents of the search to the CSV file.
    csvWriter=csv.writer(csvFile)
    csvWriter.writerow(["TITLE","ID","VIEWS","LIKES","DISLIKES","COMMENTS"])
    # a print used in order to ensure the program has gotten to this point successfully
    print("\nCSV file created correctly.")
    
    # search for videos matching search_args.search;
    
    for search_instance in search_data.get("items", []):
        if search_instance["id"]["kind"] == "youtube#video":
        
            videoId = search_instance["id"]["videoId"]  
            title = search_instance["snippet"]["title"] 
            video_data = youtube.videos().list(id=videoId,part="statistics").execute()
            for video_instance in video_data.get("items",[]):
                viewCount = video_instance["statistics"]["viewCount"]
                if 'likeCount' not in video_instance["statistics"]:
                    likeCount = 0
                else:
                    likeCount = video_instance["statistics"]["likeCount"]
                # follows likeCount from youtube_data.py by finding all the dislikes on the video
                if 'dislikeCount' not in video_instance["statistics"]:
                    dislikeCount = 0
                else:
                    dislikeCount = video_instance["statistics"]["dislikeCount"]
                # same as before but with comments
                if 'commentCount' not in video_instance["statistics"]:
                    commentCount = 0
                else:
                    commentCount = video_instance["statistics"]["commentCount"]

            csvWriter.writerow([title,videoId,viewCount,likeCount,dislikeCount,commentCount])
    print("CSV file successfully written to.")

# This function necessary prints out and displays the contents of the youtube_search function to the user
def youtube_search_term_csv(csv_file):

    # lists needed for the titles and rows
    fields=[]
    rows=[]
    
    # reading a csv file
    with open(csv_file) as file:
        # creates reader object
        reader=csv.reader(file, delimiter=',')
        # gets field names
        fields=next(reader)
        # sorts results by views from least to most
        sortedlist=sorted(reader, key=lambda x: int(x[2]))
        # reverses the list so sorted by most to least views
        sortedlist.reverse()
        # gets the data row by row
        for row in sortedlist:
            rows.append(row)
    
    # prints out all field names for readability
    print(', '.join(field for field in fields))
    print("\n")
    print(" Data Analysis of YouTube Search Data. ")
    print("\n")
    print(" Videos Sorted from Most to Least Views. ")
    print("\n")

    # for results larger than 5, as we only want 5 outputs printed out max.
    count=0
    # goes through every row, then every column in the row and prints out it's contents.
    for row in rows:
        for col in row:
            print("%10s"%col),
        print('\n')
        count+=1
        # after incrementing count, check if count is 5 or more so that output will no longer be printed out.
        if(count>=5):
            break

# main routine
if __name__ == "__main__":   
    # argparse will parse the arguments passed in through command line
    parser=argparse.ArgumentParser(description="Youtube Search by term given in command line for a set number of results")
    # The first argument we are looking for, search term
    parser.add_argument("search", default="string")
    # The second argument we are looking for, number of terms
    parser.add_argument("num_term", default="5")
    # parse_args on parser to get a usable version of the results
    search_term=parser.parse_args()    
    youtube_search(search_term.search, search_term.num_term)
    # function to read and print the results of the csv file
    youtube_search_term_csv('youtube_data.csv')
