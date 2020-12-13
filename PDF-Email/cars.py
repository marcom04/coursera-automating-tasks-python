#!/usr/bin/env python3
import sys
import json
import reports
import emails

if __name__ == "__main__":
    with open('car_sales.json') as f:
        data = json.load(f)

    #print(data)

    # Find the car with most sales
    from operator import itemgetter

    most_sales = sorted(data, key=itemgetter('total_sales'), reverse=True)
    car_make = most_sales[0]["car"]["car_make"]
    car_model = most_sales[0]["car"]["car_model"]
    total_sales = most_sales[0]["total_sales"]
    most_sales_phrase = f"The {car_make} {car_model} had the most sales: {total_sales}"

    # create dict "year":count
    sales_by_year = {}
    for car in data:
        year = car["car"]["car_year"]
        if year not in sales_by_year:
            sales_by_year[year] = 0
        sales_by_year[year] += 1

    sales_by_year = sorted(sales_by_year.items(), key=lambda item: item[1], reverse=True)

    by_years_phrase = f"The most popular year was {sales_by_year[0][0]} with {sales_by_year[0][1]} sales."

    table_data = []
    for car in data:
        car_name = f"{car['car']['car_make']} {car['car']['car_model']} ({car['car']['car_year']})"
        table_data.append([car["id"], car_name, car["price"], car["total_sales"]])
    table_data = sorted(table_data, key=lambda x: x[3], reverse=True)
    table_data.insert(0, ['ID', 'Car', 'Price', 'Total Sales'])

    title = "Sales summary for last month"
    add_info = most_sales_phrase + "<br/>" + by_years_phrase
    reports.generate("/tmp/cars.pdf", title, add_info, table_data)

    sender = "automation@example.com"
    receiver = "user@example.com"
    subject = title
    body = most_sales_phrase + "\n" + by_years_phrase
    message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
    emails.send(message)