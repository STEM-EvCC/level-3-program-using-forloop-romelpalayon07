mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

#prints out how many missions there are
countOfMission = 0
for missions in mission_success:
    countOfMission =+ 1

print("Total number of missions: " + str(countOfMission))