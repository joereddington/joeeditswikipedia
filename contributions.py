import json
import urllib

start_of_stream_time="09:52"

def difference(start,end):
#    print "Changinge start {} end {}".format(start,end)
    hour=int(end[0:2])-int(start[0:2])
    min=int(end[3:5])-int(start[3:5])
    if min <0:
        min = 60+ min 
        hour=hour-1
    difference= "{}:{:02d}".format(hour,min)
      
    return difference


# from [200~https://stackoverflow.com/a/35587027/170243[201~ 
# bug solved by [200~https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org[201~n
data = urllib.urlopen("https://en.wikipedia.org/w/api.php?action=query&format=json&list=usercontribs&ucuser=joereddington&uclimit=400").read()
output = json.loads(data)

for x in reversed(output['query']['usercontribs']):
    timestamp=x['timestamp'][11:16]
  #  print timestamp, x['comment']
    title=x['title']
    try: 
            print("{}, {}, Comment: \"{}\"".format(difference(start_of_stream_time,timestamp),title,x['comment']))
    except:
            print "odd"    
#print (output)




