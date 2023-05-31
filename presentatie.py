def presenteer(dictionairy, totaal):
    for key, value in dictionairy.items():
        print(f"{key} : {value} euro")
    print("=====================")
    print(f"totaal : {totaal} euro")

mijn_dict = {'vis' : 10, 'vlees' : 25, 'overig' : 15}
totaal = 50


