import re
import player
from operator import itemgetter

def add(line,dictionary):
        pattern = "(?P<name>\w+\s\w+)\sbatted\s(?P<bats>\d)\stimes\swith\s(?P<hits>\d)\shits";
        result= re.match(pattern,line)
        if result:
            name=result.group('name')
            bats=int(result.group('bats'))
            hits=int(result.group('hits'))
            if(dictionary.has_key(name)==False):
                dictionary[name]=player.Player(name)
            dictionary[name].bats+=bats
            dictionary[name].hits+=hits
            
f=open("record.txt")
dictionary={}
for line in f:
    add(line,dictionary)
f.close()
for name, player in dictionary.items():
    dictionary[name].set_batting_average()
   # print "name: %s bats: %d hits: %d average: %.3f" % (name, player.bats, player.hits, player.bat_average)
batting = sorted(dictionary.items(), key=lambda x:x[1].bat_average, reverse=True)
for item in batting:
    print "name: %s : %.3f" % (item[0],item[1].bat_average)