from db import *
import random
class Skills:
    def get_skills(self):
        with conn.cursor() as curs:
            cursor = conn.cursor()
            # Получаем список всех скиллов
            cursor.execute('SELECT * FROM character_characteristics.skills_list')
            all_users = cursor.fetchall()
            print(all_users)
            cursor.close() 
            conn.close() 
    def add_skills(self):
            self.fighting_value = random.randint(0,10)
            self.shooting_value = random.randint(0,10)
            self.building_value = random.randint(0,10)
            self.crafting_items_value = random.randint(0,10)
            self.electronics_value = random.randint(0,10)
            self.programming_value = random.randint(0,10)
            self.research_value = random.randint(0,10)
            self.agronomy_value = random.randint(0,10)
            self.mining_value = random.randint(0,10)
            self.cooking_value = random.randint(0,10)
            with conn.cursor() as curs:
                curs.execute("INSERT INTO saves.skill_values (fighting_value,shooting_value,building_value,crafting_items_value,electronics_value,programming_value,research_value,agronomy_value,mining_value,cooking_value) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(self.fighting_value,self.shooting_value,self.building_value,self.crafting_items_value,self.electronics_value,self.programming_value,self.research_value,self.agronomy_value,self.mining_value,self.cooking_value))
                conn.commit()
                curs.close()
skills = Skills()