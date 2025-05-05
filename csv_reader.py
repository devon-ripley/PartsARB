import csv

def parts_file_read(path):
    #read csv files
    parts_price_dict = {}
    parts_list = []
    print(f'loading {path}')
    with open(path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            parts_price_dict[row['part']] = int(row['price'])
            parts_list.append(row['part'])
    return parts_price_dict, parts_list

def cars_file_read(path):
    cars_list = []
    print(f'loading {path}')
    with open(path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            car = row['year'] + ' ' + row['make'] + ' ' + row['model'] + ' '
            cars_list.append(car)
    return cars_list

def save_results(path, results_dict):
    with open(path, "w", newline="") as file:
        w = csv.DictWriter(file, results_dict.keys())
        w.writeheader()
        w.writerow(results_dict)

