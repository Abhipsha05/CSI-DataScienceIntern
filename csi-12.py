import csv

# Open the CSV file to read
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Print all email addresses
    for line in csv_reader:
        print(line['email'])
    
    # Reset the file pointer to the beginning of the file
    csv_file.seek(0)
    
    # Reinitialize the CSV reader to read the file again
    csv_reader = csv.DictReader(csv_file)

    # Open a new CSV file to write
    with open('new_names2.csv', 'w') as new_file2:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file2, fieldnames=fieldnames, delimiter='\t')
        
        # Write the header
        csv_writer.writeheader()
        
        # Write rows from the original CSV file to the new CSV file
        for line in csv_reader:
            csv_writer.writerow(line)
    
    
    #csv_reader = csv.reader(csv_file)
    #for line in csv_reader:
        #print(line)
        #print(line[1])
        
    
    #with open('new_names.csv','w') as new_file:
        #csv_writer = csv.writer(new_file, delimiter = '\t')#separate with tab
        
        #for line in csv_reader:
            #csv_writer.writerow(line)
       
      