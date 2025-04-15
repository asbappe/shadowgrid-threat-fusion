def map_risks(threats):
    for threat in threats:
        threat["Impact"] = "High" if threat["Score"] > 8 else "Moderate"
    return threats
