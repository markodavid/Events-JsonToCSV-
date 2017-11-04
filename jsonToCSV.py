import json
import codecs

with open('events.json') as json_data:
    data = json.load(json_data)
    fo = codecs.open('nuevoEvento.txt', encoding='utf-8',mode="wb")
    fo.write("event" + "," + "programStage" + "," + "program" + "," + "orgUnit" + "," + "eventDate" +"," + "voucher" + "," + "cui" + "edad" + ","+ "comoSeEntero" + "," +
             "utilizacionMetodo" + "," + "presentaSintomas" + "razonUso" + "metodoProvisto" + "ocasion" + "tipoProducto" + "servicioProvisto" + "descontinuacion" +"\n")

    for r in data["events"]:
        fo.write(r["event"]+","+r["programStage"] + "," + r["program"]+ "," + r["orgUnit"]+ "," + r["eventDate"])
        value1 = ""
        value2 = ""
        value3 = ""
        value4 = ""
        value5 = ""
        value6 = ""
        value7 = ""
        value8 = ""
        value9 = ""
        tipoProducto = ""
        servicioProvisto = ""
        descontinuacion = ""
        for s in r["dataValues"]:
            if s["dataElement"] == "chRv6qKPFv1":
                value1 = s["value"]
            elif s["dataElement"] == "jpVO6drF8g1":
                value2 = s["value"]
            elif s["dataElement"] == "XTCbwhUhbzG":
                value3 = s["value"]
            elif s["dataElement"] == "SVHK6Lo921J":
                value4 = s["value"]
            elif s["dataElement"] == "sMwOBd5kpXS":
                value5 =s["value"]
            elif s["dataElement"] == "BlKXR08FXOd":
                value6 = s["value"]
            elif s["dataElement"] == "UiM5jqgvpwE":
                value7 = s["value"]
            elif s["dataElement"] == "JylO6HVyb8y":
                value8 = s["value"]
            elif s["dataElement"] == "Fs4mWm7ASTK":
                value9 =s["value"]
            elif s["dataElement"] == "HYK44c6fc2H":
                tipoProducto = s["value"]
            elif s["dataElement"] == "tZmmKfo75aP":
                servicioProvisto =s["value"]
            elif s["dataElement"] == "Ie3vjYD5ups":
                descontinuacion = s["value"]

        fo.write("," + value1  + "," + value2 + "," + value3 + "," + value4 + "," + value5 + "," + value6 + "," + value7 + "," + value8 + "," + value9 + "," + tipoProducto + "," + servicioProvisto + "," + descontinuacion  + " \n")
        value1 = ""
        value2 = ""
        value3 = ""
        value4 = ""
        value5 = ""
        value6 = ""
        value7 = ""
        value8 = ""
        value9 = ""
        tipoProducto = ""
        servicioProvisto = ""
        descontinuacion = ""

    fo.close()
