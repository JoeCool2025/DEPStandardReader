from standards_reader import StandardsDict
from standards_reader import header

def RS_Search(contaminant, concentration):
    print()
    SSL = False
    if contaminant in StandardsDict:
        for limit in StandardsDict[contaminant]:
            if type(limit) != str and concentration >= limit: # check if limit is a number and if concentration exceeds the limit
                print(f"Exceedance detected for {contaminant}:")
                print(header[1:])
                print(f"{StandardsDict[contaminant]}\n")
                return
            elif limit == 'Site Specific': # specific catch for site-specific limits
                print(f"Exceedance possible, site-specific limit for {contaminant}: {StandardsDict[contaminant]}\n")
                SSL = True
        if not SSL:
            print(f"No exceedance detected for {contaminant}\n")
    else:
        print(f"{contaminant} not found in current standards database.\n")