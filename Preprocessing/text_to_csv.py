import csv

txt_file = r"Circle2Accelerometer.txt"
csv_file = r"Circle2Accelerometer.csv"

in_txt = csv.reader(open(txt_file, "rb"), delimiter='\t')
out_csv = csv.writer(open(csv_file, 'wb'))

out_csv.writerows(in_txt)


