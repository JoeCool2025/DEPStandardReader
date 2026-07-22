from standards_reader import StandardsDict
from standards_reader import header
from CASN import NameDict
from CASN import ReverseNameDict
from summary import SummaryAnalysis
from rs_search import RS_Search
run_condition = True

while True:
    mode = input("To search a database - type 'search'\nTo perform a table analysis - type 'summary'\n\n")
    if mode.lower() == "search":
        break
    elif mode.lower() == "summary":
        break
    else:
        print("Invalid Mode\n")

def check_contaminant_name(contaminant):
    while True:
        if contaminant is None:
            return None
        cand = contaminant.strip()
        if cand.lower() == 'exit':  # exit condition
            return None
        # check if input is a recognized contaminant name (case-insensitive)
        if cand.lower() in NameDict:
            return cand.lower()
        # check if input is a recognized CASN (exact match after stripping)
        if cand in ReverseNameDict:
            # return the first associated contaminant name in lowercase
            return ReverseNameDict[cand][0].lower()
        print(f"Contaminant '{contaminant}' not recognized. Please check the contaminant name or CASN, or update our CASN dictionary\n")
        contaminant = input("Enter the contaminant name or CASN (or type 'exit' to quit): ")


if mode.lower() == "search":
    while True:
        contaminant_0 = input("Enter the contaminant name or CASN (or type 'exit' to quit): ")
        if contaminant_0.lower() == 'exit': # end condition
            run_condition = False
            print("Exiting the program.")
            break
        else:
            contaminant_name = check_contaminant_name(contaminant_0)
            if contaminant_name == None:
                run_condition = False
                print("Exiting the program.")
                break
            else:
                contaminant = NameDict[contaminant_name] # grabs CASN for CSV search

        while True:
            try:
                concentration = float(input(f"Enter the concentration for {contaminant_name}: "))
                break
            except ValueError:
                print("Invalid concentration. Please enter a numeric value.\n")
                continue

        # call the search function and handle return values explicitly
        result = RS_Search(contaminant, concentration)
        if result == 1:
            print(f"{contaminant_name} ({contaminant}) not found in current standards database.\n")
        elif result == 0:
            print(f"No exceedance detected for {contaminant_name}\n")
        if not run_condition:
            break
else:
    while True:
        try:
            num_sites = int(input("Enter the number of sites being evaluated and summarized: "))
            break
        except ValueError:
            print("Please input an integer.")

    while True:
        try:
            num_analytes = int(input("Enter the number of analytes being evaluated and summarized: "))
            break
        except ValueError:
            print("Please input an integer.")
    print()
    SummaryAnalysis(num_sites, num_analytes, StandardsDict, NameDict)
    

