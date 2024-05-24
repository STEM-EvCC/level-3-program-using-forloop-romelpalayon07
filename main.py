mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

#prints out how many missions there are
countOfMission = 0
for missions in mission_success:
    countOfMission = countOfMission + 1
print()
print("Total number of missions: " + str(countOfMission))

#prints out how many of the missions were successful
successfulMissionsCount = 0
for successfulMission in mission_success:
    if successfulMission == True:
        successfulMissionsCount += 1

print("Number of successful missions: " + str(successfulMissionsCount))

#prints out the success rate
successRate = (successfulMissionsCount/countOfMission)*100

print(f"Success rate: {successRate:.2f}%")

#prints out which of the missions were launched before 2000
print("Missions launched before the year 2000:")
for missionName, missionsBefore2000 in zip (mission_names, mission_years):
    if missionsBefore2000 < 2000:
        print("- " + missionName)
print()