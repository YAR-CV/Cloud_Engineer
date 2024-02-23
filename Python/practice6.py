
gradenotes = {
    "Yary" : 10.9,
    "Alexandra" : 15.6,
    "Angela" : 16.2
    }
del gradenotes["Yary"]
for name, grade in gradenotes.items():
    print("La calificación de %s es %d" % (name, grade))

