import csv

def process_csv(input_file, output_file):
  with open(input_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = []
    for row in reader:
      if row['product'] == 'pink morsel':
        price = float(row['price'].replace('$', ''))
        sales = price * float(row['quantity'])
        processed_row = {
          'sales': sales,
          'date': row['date'],
          'region': row['region']
        }
        data.append(processed_row)

  with open(output_file, 'w', newline='') as outfile:
    fieldnames = ['sales', 'date', 'region']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

input_files = ['data\daily_sales_data_0.csv', 'data\daily_sales_data_1.csv', 'data\daily_sales_data_2.csv']
output_file = 'output.csv'

for file in input_files:
  process_csv(file, output_file)