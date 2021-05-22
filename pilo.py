```
from cowin_api import CoWinAPI
from pushbullet import Pushbullet
import json

district_id = ''  #<-district id
#date = '03-05-2021'  # Optional. Takes today's date by default
#min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit
API_KEy="o.rlk;tpfokwpeok-PUSHBULLET API KEY --t6C"
cowin = CoWinAPI()
av = cowin.get_availability_by_district(district_id)

mynearestblock=["Ulhasnagar Municipal Corporation","Ambernath"] #Type your block name


flag="False"
i=0
j=0
place=[]
pb=Pushbullet(API_KEy)
print(len(av['centers']))
while i<len(av['centers']):
        
        
        if av['centers'][i]['block_name'] in mynearestblock:
                #print(av['centers'][i]['block_name'])
                #print(av['centers'][i]['name'])
                j=0
                for j in av['centers'][i]['sessions']:
                        if (j['available_capacity']>0):
                                flag="True"
                                print(place)
                                
                                place.append(av['centers'][i]['name'])
                                
                                
                                
                        
               
                        
                
        i=i+1
if flag=="True":
        s="\n"
        place=s.join(place)
        push=pb.push_note('Vaccine booking are available!',place)
else:
        push=pb.push_note('Tried not found.', 'I will try again')
                                



```
