import random
from db import *
from gender import *
class Names:
    def name_select(self):
        with open('names_surnames/names_surnames.txt',"r") as names_file:
            string_extractor = names_file.readlines()
        self.male_name = string_extractor[random.randint(1,201)]
        self.female_name=string_extractor[random.randint(201,401)]
        self.surname=string_extractor[random.randint(401,601)]
        if gender.gender_random == 0:
            with conn.cursor() as curs:
                    curs.execute("INSERT INTO saves.names (character_name,character_surname) VALUES (%s, %s)",(self.male_name,self.surname))
                    conn.commit()
                    curs.close()
        else:
             with conn.cursor() as curs:
                    curs.execute("INSERT INTO saves.names (character_name,character_surname) VALUES (%s, %s)",(self.female_name,self.surname))
                    conn.commit()
                    curs.close()
names = Names()