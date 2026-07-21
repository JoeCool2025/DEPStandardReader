from standards_reader import StandardsDict
from standards_reader import header
from CASN import NameDict
run_condition = True

def RS_Search(contaminant, concentration):
    print()
    SSL = False
    if contaminant in StandardsDict:
        for limit in StandardsDict[contaminant]:
            if type(limit) != str and concentration >= limit:
                print(f"Exceedance detected for {contaminant}:")
                print(header[1:])
                print(f"{StandardsDict[contaminant]}\n")
                return
            elif limit == 'Site Specific':
                print(f"Exceedance possible, site-specific limit for {contaminant}: {StandardsDict[contaminant]}\n")
                SSL = True
        if not SSL:
            print(f"No exceedance detected for {contaminant}\n")
    else:
        print(f"{contaminant} not found. Please check the contaminant CASN and try again.\n")

while run_condition:
    contaminant = input("Enter the contaminant name or CASN (or type 'exit' to quit): ")
    if contaminant.lower() == 'exit':
        run_condition = False
        print("Exiting the program.")
        break

    try:
        concentration = float(input(f"Enter the concentration for {contaminant}: "))
    except ValueError:
        print("Invalid concentration. Please enter a numeric value.\n")
        continue

    if contaminant.lower() in NameDict:
        contaminant = NameDict[contaminant.lower()]

    RS_Search(contaminant, concentration)