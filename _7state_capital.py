# Question_num_2 = Create a dictionary of any 7 Indian states and their capitals.Write this into a JSON file.

import json

data = {

    "Maharashtra":"Mumbai",
    "Kerala":"Thiruvananthapuram",
    "Tamilnadu":"Chennai",
    "Telangana":"Hyderabad", 
    "Rajsthan":"Jaipur",
    "WestBengal":"Kolkata",
    "Goa":"Panaji",
    
}

with open("C:\\Users\\HP\\Desktop\\DS301222\\_6_assignment_no_6\\state_capital.json","w") as file:

    json.dump(data,file)










