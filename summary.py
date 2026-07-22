from rs_search import RS_Search

def SummaryAnalysis (num_sites, num_analytes, standards, name):
    data_dict = {}

    for y in range(0, num_analytes + 1):
        for x in range(0, num_sites + 1):
            if y == 0 and x == 0:
                data_dict["Analyte"] = []
            elif y == 0 and x != 0:
                data_dict["Analyte"].append(input(f"Enter site ID #{x}: "))
            elif x == 0:
                analyte = input(f"Enter analyte #{y}: ")
                data_dict[analyte] = []
            else:
                concentration = input(f"Enter concentration for {analyte}, {data_dict["Analyte"][x - 1]}: ")
                try:
                    data_dict[analyte].append(int(concentration))
                except ValueError:
                    try:
                        data_dict[analyte].append(float(concentration))
                    except ValueError:
                        data_dict[analyte].append(concentration)
                        continue

    for entry in data_dict:
        print(f"{entry}: {data_dict[entry]}")
        if entry.lower() in name:
            for conc in data_dict[entry]:
                if type(conc) != str:
                    RS_Search(name[entry.lower()], conc)

    
    pass
            