import webbrowser

# opens in read mode saves as object in file
file = open("webpages.txt", "r")

# gibt inhalt von object file aus
for line in file:

    # schneidet umbruch ab
    line = line.strip("\n")
    print(line)
    webbrowser.open_new_tab(line)
