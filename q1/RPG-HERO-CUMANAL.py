# ============================================================
#  RPG Hero — complete the class below.
#  The class name and method names are already set for you;
#  just fill in the bodies marked with TODO.
# ============================================================
class Hero:
    def __init__(self, name, hp):
        # TODO: store `name` and `hp` as INSTANCE attributes
        self.name = name
        self.hp = hp
        

    def take_damage(self, amount):
        # TODO: subtract `amount` from this hero's hp
        self.hp = self.hp - amount
        


# ------------------------------------------------------------
#  Step 3 — Instantiate two heroes and try them out.
#  Uncomment and complete the lines below once your class works.
# ------------------------------------------------------------
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(f"Arthur: {arthur.hp}")     
print(f"Morgana: {morgana.hp}")    


# this is pisay

