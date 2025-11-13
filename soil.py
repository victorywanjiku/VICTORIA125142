soil_ph=float(input("enter soil ph(0-14):"))
if 0<=soil_ph<=14:
    print("invalid ph value:must be within the range")
    if soil_ph<5.5:
        soil_type="acidic"
        AI="ideal for most crops such as maize,beans and vegetables"
        if 5.6<soil_ph<7.5:
            soil_type="neutral"
        AI="ideal for most crops such as maize,beans and vegetables"
        if soil_ph>7.5:
             soil_type="alkaline"
        AI="add oraginic matter or suplhur,suitable for barley and cabbage"
print("soil ph:",soil_ph)
print("soil type:",soil_type)
print("advice:",AI)