import csv

PATH_TO_CSV = './testcsv.csv'
print("csv file need to be sorted by filename. Otherwise, it will create a single mask for multiple labels")

with open(PATH_TO_CSV, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'{row["label_hierarchy"].split(">", 1)[0]}\t{row["filename"]}\t{row["points"]}\t{row["attributes"]}')
        line_count += 1
    print(f'Processed {line_count} lines.')


#def add_mask(x,y,radius):

