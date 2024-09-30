import bikes

print("Test 1:", bikes.distance_of_user("ocuber"))
print("Test 2:", bikes.speed_of_user("ocuber"))
print("Test 3:", bikes.duration_in_each_city("2021-06-01"))
print("Test 4:", bikes.users_in_city("laeserii"))
print("Test 5:", bikes.trips_on_each_day("laeserii"))
print("Test 6:", bikes.most_popular_start("laeserii"))


# Test 1: 54320
# Test 2: 16.21
# Test 3: [('anddesen', 59354), ('anpoan', 59296), ('baphoetron', 58655), ('beriifo', 59749), ('laeserii', 59470), ('maller', 60947), ('miboo', 57403), ('nonraemo', 59829), ('selatan', 57488), ('triamal', 59925)]
# Test 4: 43246
# Test 5: [('2021-06-01', 3403), ('2021-06-02', 3406), ('2021-06-03', 3216), ('2021-06-04', 3360), ('2021-06-05', 3416), ('2021-06-06', 3243), ('2021-06-07', 3336), ('2021-06-08', 3335), ('2021-06-09', 3429), 
# ('2021-06-10', 3297), ('2021-06-11', 3351), ('2021-06-12', 3316), ('2021-06-13', 3362), ('2021-06-14', 3370), ('2021-06-15', 3298), ('2021-06-16', 3405), ('2021-06-17', 3164), ('2021-06-18', 3324), ('2021-06-19', 3356), ('2021-06-20', 3280), 
# ('2021-06-21', 3293), ('2021-06-22', 3332), ('2021-06-23', 3303), ('2021-06-24', 3403), ('2021-06-25', 3308), ('2021-06-26', 3317), ('2021-06-27', 3338), ('2021-06-28', 3441), ('2021-06-29', 3262), ('2021-06-30', 3357)]
# Test 6: ('riirande', 1077)


"""
Arvostelu

Seuraava moduuli main.py testaa moduuliasi bikes.py arvostelua varten.
Huomaa, että funktioita kutsutaan tässä eri tavalla kuin yllä olevassa esimerkissä.

--------------------------------------------------------------------------------------
import bikes

print("Test 1:", bikes.distance_of_user("eba"))
print("Test 2:", bikes.speed_of_user("eba"))
print("Test 3:", bikes.duration_in_each_city("2021-06-15"))
print("Test 4:", bikes.users_in_city("anddesen"))
print("Test 5:", bikes.trips_on_each_day("anddesen"))
print("Test 6:", bikes.most_popular_start("anddesen"))
"""