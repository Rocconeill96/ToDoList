languages = ['English', 'German', 'Spanish']

for lang in languages:
    with open(f"coding_exercises/{lang}.txt", "w") as file:
        file.write(lang)
        file.close()
        

