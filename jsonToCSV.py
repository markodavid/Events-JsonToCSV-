import json
import codecs

with open('events.json') as json_data:
    data = json.load(json_data)
    fo = codecs.open('nuevoEvento.txt', encoding='utf-8',mode="wb")
    fo.write("event" + "," + "programStage" + "," + "program" + "," + "orgUnit" + "," + "eventDate" +"," + "edad" + "," + "cui" + "Recomendo" + "\n")
    for r in data["events"]:
        fo.write(r["event"]+","+r["programStage"] + "," + r["program"]+ "," + r["orgUnit"]+ "," + r["eventDate"])
        for s in r["dataValues"]:
            if s["dataElement"]=="XTCbwhUhbzG":
                value1=s["value"]
            else:
                if s["dataElement"]=="jpVO6drF8g1":
                    value2=s["value"]
                else:
                    if s["dataElement"] == "SVHK6Lo921J":
                        value3 = s["value"]


        fo.write("," + value1  +"," + value2 + "," + value3 + "\n")
        value1=""
        value2=""
        value3=""

    fo.close()
