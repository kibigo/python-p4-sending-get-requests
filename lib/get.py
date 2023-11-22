# import requests
# import json

# url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

# response = requests.get(url)

# json_content = json.loads(response.text)

# print(json.dumps(json_content, indent=4))

import requests
import json

class GetPrograms:

    def get_programs():
        
        URL = "https://data.cityofnewyork.us/resource/uvks-tn5n.json"

        response = requests.get(URL)

        return response.content
    
    def program_school(self):

        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list
        

# programs = GetPrograms.get_programs()
# print(programs)

programs = GetPrograms.get_programs()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print (school)