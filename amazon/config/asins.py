import csv
reviews_base_url = 'https://www.amazon.com/product-reviews/{}'
products_base_url = 'https://www.amazon.com/dp/{}'


def get_asin_list() -> list:
    asin_list = []
    with open('/home/milo/7-scrapy/amazon/amazon/config/asin.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue  # header
            if row[0]:
                asin_list.append(row[0])
        return asin_list


print(get_asin_list())
asin_list = get_asin_list()
