name:str = "Ojo Boluwatife"
ID:str = "ST001"
level:str = "100LV"
score:float = 85
is_registered:bool = True

def display_profile(name:str, ID:str, level:str, score:float, is_registered:bool) -> None:
    print(f"Student Profile\n"
          f"name: {name}\n"
          f"ID: {ID}\n"
          f"level: {level}\n"
          f"score: {score}\n"
          f"is_registered: {is_registered}")

display_profile(name, ID, level, score, is_registered)