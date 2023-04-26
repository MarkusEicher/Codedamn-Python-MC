report = ""
total = 0
with open('file_io/sales.txt') as file:
    for line in file.readlines():
        day, sale = line.split(" - ")
        report += f"{day}: {sale}"

        total += int(sale)

report += f'\n{"-"*10}\n'
report += f"{'Total'}: {total}"

with open('file_io/report.txt', 'w') as file:
    file.write(report)