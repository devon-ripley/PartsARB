import analysis
import csv_reader
import scraper

def buy_data(csv_list):
    pass

def sell_data(num_pages, car_list_csv, part_list_csv, results_path):

    #load csv's
    parts_price_dict, parts_list = csv_reader.parts_file_read(part_list_csv)
    cars_list = csv_reader.cars_file_read(car_list_csv)
    print("CSV's loaded")

    # scraper
    print('Starting scraper')
    scrape_results = scraper.run(num_pages=num_pages, parts=parts_list, cars=cars_list)
    print(f'Scrape Results: {scrape_results}')

    #prelim analysis
    analysis_results = analysis.scraped_run(scrape_results)
    analysis_results = analysis.compare_run(analysis_results, parts_price_dict)
    print(f'Analysis Results: {analysis_results}')

    #save results
    csv_reader.save_results(results_path, analysis_results)

    # more advanced under here


def main():
    # settings
    part_list_csv = 'part_list_picknpull.csv'
    car_list_csv = 'car_list.csv'
    results_path = 'results.csv'
    num_pages = 1

    buy_data(part_list_csv)
    sell_data(num_pages, car_list_csv, part_list_csv, results_path)

if __name__ == '__main__':
    main()