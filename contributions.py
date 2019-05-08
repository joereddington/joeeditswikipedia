import json,urllib.request

start_of_stream_time="12:00"

def difference(start,end):
    hour=int(end[0:2])-int(start[0:2])
    min=int(end[3:5])-int(start[3:5])

    return "{}:{}".format(hour,min)


# from [200~https://stackoverflow.com/a/35587027/170243[201~ 
# bug solved by [200~https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org[201~n
data = urllib.request.urlopen("https://en.wikipedia.org/w/api.php?action=query&format=json&list=usercontribs&ucuser=joereddington&uclimit=200").read()
output = json.loads(data)

for x in output['query']['usercontribs']:
    timestamp=x['timestamp'][11:16]
    title=x['title']
    print("{}, {}".format(difference(start_of_stream_time,timestamp),title))

#print (output)




