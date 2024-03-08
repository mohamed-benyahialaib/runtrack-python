def time_to_text(minute):
    if int(minute)==minute:
        print(minute)
    else : print("le nombre de minute n'est pas entier")
    if minute >= 60: hour = int(minute/60)
    minuterestante= minute-int(hour)*60
    print(hour, "heures et", minuterestante, "minutes")

time_to_text(140)
time_to_text(360)
time_to_text(545)