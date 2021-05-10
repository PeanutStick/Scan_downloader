import requests
import os
manga = "/solo_leveling/" # The name of the manga
nbchap = 150 # Number of chapitre
chapitre = 1 # Initialise the var
i=1

while chapitre <= 150: 
    page = f'{i:03}' # to get 3 digit because of the URL ex(i=22 so we request 022.jpg )
    url = "https://www.scan-fr.cc/uploads/manga/solo-leveling/chapters/"+str(chapitre)+"/"+str(page)+".jpg"
    r = requests.get(url)
    filename = manga[1:]+str(chapitre)+'_'+page+'.jpg' #the path
    with open(filename, 'wb') as outfile: # To save it
        outfile.write(r.content)
    size = os.path.getsize(filename) # Get the size of the file
    i=i+1
    if size < 5000: # If the size is too smal it's because there is no image
        os.remove(filename) # I remove the empty file
        chapitre=chapitre+1 # Next chap
        i=1 # Page 1
    
    
