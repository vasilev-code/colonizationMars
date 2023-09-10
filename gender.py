import random
from db import *
class Gender:
    def gender_mixer(self):
        self.gender_random = random.randint(0,1)
        if self.gender_random == 0:
            with conn.cursor() as curs:
                curs.execute("INSERT INTO saves.genders (gender_name) VALUES (%s)",[self.gender_random])
                conn.commit()
                curs.close()
        else:
              with conn.cursor() as curs:
                    curs.execute("INSERT INTO saves.genders (gender_name) VALUES (%s)",[self.gender_random])
                    conn.commit()
                    curs.close()
gender = Gender()