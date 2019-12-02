with open("haiku.txt", "r+") as file:
    file.seek(0)
    file.write('Apparently it overwrites everything...\n')


# with open("lol.txt", "w") as laugh:
#     laugh.write("hahahahahahahahahahahahahahahaha\n" * 100)