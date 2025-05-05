import statistics


def scraped_run(scraped_prices_dict, debug=False):
    scraped_prices_dict_copy = scraped_prices_dict
    car_list = scraped_prices_dict_copy.keys()
    for car in car_list:
        part_list = scraped_prices_dict_copy[car].keys()
        for part in part_list:
            if debug:
                print(f'scraped_prices_dict[car][part]: {scraped_prices_dict[car][part]}')
            numbers = scraped_prices_dict[car][part]
            scraped_prices_dict[car][part] = {}
            # scraped_prices_dict[car][part]['data'] = numbers
            scraped_prices_dict[car][part]['max'] = max(numbers)
            scraped_prices_dict[car][part]['min'] = min(numbers)
            scraped_prices_dict[car][part]['mean'] = statistics.mean(numbers)
            scraped_prices_dict[car][part]['median'] = statistics.median(numbers)
    return scraped_prices_dict

def compare_run(scraped_prices_dict, parts_dict, debug=False):
    scraped_prices_dict_copy = scraped_prices_dict
    car_list = scraped_prices_dict_copy.keys()
    for car in car_list:
        part_list = scraped_prices_dict_copy[car].keys()
        for part in part_list:
            buy_price = parts_dict[part]
            if debug:
                print(buy_price)
            scraped_prices_dict[car][part]['buy'] = buy_price
            median = scraped_prices_dict[car][part]['median']
            dif = median - buy_price
            scraped_prices_dict[car][part]['dif'] = dif
    return scraped_prices_dict

def analysis_debug(scraped_prices_dict, parts_dict):
    print(scraped_run(scraped_prices_dict))
    print(compare_run(scraped_prices_dict, parts_dict, debug=True))

if __name__ == '__main__':
    analysis_debug({'1998 jeep wrangler ': {'fuel injector': [154, 159, 149, 259, 99, 26, 28, 94, 165, 159, 149, 249, 149, 199, 175, 145, 559, 31, 45, 56, 24, 249, 76, 149, 29, 40, 75, 32, 64, 48, 57, 159, 149, 139, 75, 46, 51, 28, 140, 28, 62, 65, 160, 32, 37, 79, 105, 263, 4, 62, 65, 106, 424, 85, 89, 56, 26, 53, 35, 39, 65, 60, 75, 78, 125, 566, 65, 35, 38, 28, 109, 274, 5, 14, 38, 29, 23, 40, 50, 61, 122, 11, 6, 51, 35, 37, 103, 38, 24, 49, 149, 166, 50, 61], 'window wiper': [20, 52, 44, 541, 513, 39, 22, 57, 12, 12, 13, 20, 44, 533, 22, 22, 20, 22, 13, 13, 14, 64, 13, 37, 33, 39, 22, 65, 71, 15, 13, 19, 13, 6, 6, 6, 7, 3, 7, 11, 38, 12, 39, 36, 13, 19, 39, 39, 22, 29, 32, 20, 52, 35, 12, 13, 33, 42, 12, 38, 15, 65, 69, 15, 9, 7, 9, 3, 13, 11, 12, 13, 10, 31, 34, 21, 22, 4, 3, 10, 18, 9, 13, 13, 22, 32, 22, 34, 37, 15, 18, 3, 999, 26, 28]}, '2001 ford explorer ': {'fuel injector': [112, 179, 51, 99, 541, 63, 51, 35, 37, 37, 179, 99, 5147, 42, 159, 544, 36, 40, 80, 5105, 38, 38, 78, 45, 42, 49, 150, 10, 147, 125, 19, 2, 126, 109, 540, 50, 44, 52, 30, 52, 63, 54, 0, 31, 58, 12, 2, 29, 44, 42, 47, 159, 552, 38, 46, 46, 55, 37, 41, 8, 47, 51, 179, 207, 80, 129, 26, 31, 199, 179, 44, 74, 10, 41, 45, 6, 9, 79, 13, 149, 38, 14, 219, 20, 49, 35, 44, 52, 59], 'window wiper': [29, 28, 29, 6, 7, 11, 8, 5, 14, 17, 29, 6, 55, 512, 11, 6, 7, 11, 55, 57, 5, 16, 34, 28, 22, 24, 39, 5, 5, 17, 12, 10, 8, 5, 11, 3, 39, 6, 5, 6, 55, 11, 7, 6, 7, 15, 17, 5, 59, 20, 51007, 5, 7, 11, 6, 6, 4, 37, 49, 20, 5, 40, 5, 5, 5, 5, 4, 13, 14, 5, 5, 5, 9, 12, 1513, 14, 6, 39, 6, 7]}}, {'fuel injector': 7, 'window wiper': 5})