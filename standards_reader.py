import csv
StandardsDict = {}

while True:
    filename = input("Enter the CSV name (e.g., njdep.csv): ")

    if not filename.endswith('.csv'):
        # Check if file type is a CSV file
        print("That doesn't look like a CSV file. Please enter a valid CSV file name (e.g., njdep.csv).\n")
        continue

    try:
        with open(filename, newline='', encoding='utf-8-sig') as csvfile:
            StandardsReader = csv.reader(csvfile, dialect='excel')
            header = next(StandardsReader)
            print(f"Header: {header}\n") # Remove header row from CSV
            for row in StandardsReader:
                # Create a dictionary with the key as the CASN and the value as a list of standards
                StandardsDict[row[0]] = []
                for i in range(1, len(row)):
                    try:
                        # if standard is an integer, convert it to an int and append to the list
                        int(row[i])
                        StandardsDict[row[0]].append(int(row[i]))
                    except ValueError:
                        try:
                            # if standard is a decimal, convert it to a float and append to the list
                            float(row[i])
                            StandardsDict[row[0]].append(float(row[i]))
                        except ValueError:
                            # if standard is text, append it to the list as is
                            StandardsDict[row[0]].append(row[i])
                            continue
        break
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the file name and make sure it is in the proper folder and then try again.")
