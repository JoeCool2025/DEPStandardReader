from standards_reader import StandardsDict
from standards_reader import header
from CASN import NameDict
from CASN import ReverseNameDict
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
        print(f"{contaminant} not found in current standards database.\n")

def check_contaminant_name(contaminant):
    while True:
        if contaminant.lower() == 'exit':
            return None
        elif contaminant.lower() in NameDict:
            return contaminant.lower()
        elif contaminant in ReverseNameDict:
            for name in ReverseNameDict[contaminant]:
                return name
        else:
            print(f"Contaminant '{contaminant}' not found. Please check the contaminant name or CASN, or update our CASN dictionary\n")
            contaminant = input("Enter the contaminant name or CASN (or type 'exit' to quit): ")

while run_condition:
    contaminant_0 = input("Enter the contaminant name or CASN (or type 'exit' to quit): ")
    if contaminant_0.lower() == 'exit':
        run_condition = False
        print("Exiting the program.")
        break
    else:
        contaminant_name = check_contaminant_name(contaminant_0)
        if contaminant_name == None:
            print("Exiting the program.")
            break
        else:
            contaminant = NameDict[contaminant_name]

    while True:
        try:
            concentration = float(input(f"Enter the concentration for {contaminant_name}: "))
            break
        except ValueError:
            print("Invalid concentration. Please enter a numeric value.\n")
            continue

    RS_Search(contaminant, concentration)