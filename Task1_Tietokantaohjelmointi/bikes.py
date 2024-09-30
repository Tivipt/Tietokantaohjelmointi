import sqlite3

db = sqlite3.connect("bikes.db")
db.isolation_level = None

# ilmoittaa käyttäjän ajaman yhteismatkan.
def distance_of_user(user):
    kayttaja = user[4:]
    matka = db.execute( '''
                        SELECT SUM(T.distance)
                        FROM Trips T, Users U
                        WHERE T.user_id = U.id AND T.user_id = ?
                        ''', [kayttaja]).fetchone()
    return matka[0]

# ilmoittaa käyttäjän keskinopeuden (km/h) kaikilla matkoilla kahden desimaalin tarkkuudella.
def speed_of_user(user):
    return 5

# ilmoittaa jokaisesta kaupungista, kauanko pyörillä ajettiin annettuna päivänä.
def duration_in_each_city(day):
    return 5

# ilmoittaa, montako eri käyttäjää pyörillä on ollut annetussa kaupungissa.
def users_in_city(city):
    return 5

# ilmoittaa jokaisesta päivästä, montako matkaa kyseisenä päivänä on ajettu.
def trips_on_each_day(city):
    return 5

# ilmoittaa kaupungin suosituimman aloitusaseman matkalle sekä matkojen määrän.
def most_popular_start(city):
    return 5


"""
Tehtäväsi on laatia Pythonilla moduuli bikes.py, joka tarjoaa seuraavat funktiot:

distance_of_user(user)
ilmoittaa käyttäjän ajaman yhteismatkan.

speed_of_user(user)
ilmoittaa käyttäjän keskinopeuden (km/h) kaikilla matkoilla kahden desimaalin tarkkuudella.

duration_in_each_city(day)
ilmoittaa jokaisesta kaupungista, kauanko pyörillä ajettiin annettuna päivänä.

users_in_city(city)
ilmoittaa, montako eri käyttäjää pyörillä on ollut annetussa kaupungissa.

trips_on_each_day(city)
ilmoittaa jokaisesta päivästä, montako matkaa kyseisenä päivänä on ajettu.

most_popular_start(city)
ilmoittaa kaupungin suosituimman aloitusaseman matkalle sekä matkojen määrän 
(jos vaihtoehtoja on useita, valitaan niistä aakkosjärjestyksessä viimeisin).
"""
