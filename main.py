def gen_plates():
    area_codes = []
    random_last = []
    first_area_codes = 'ABCDEFGHKLMNOPRSVWY'
    second_area_codes = 'ABCDEFGHKLMNOPRSTVWXY'
    for i in first_area_codes:
        for j in second_area_codes:
            area_codes.append(i + j)
    last_letters = 'ABCDEFGHJKLMNOPRSTUVWXYZ'
    second_last_letters = 'ABCDEFGHJKLMNOPRSTUVWXYZ'
    third_last_letters = 'ABCDEFGHJKLMNOPRSTUVWXYZ'
    for i in last_letters:
        for j in second_last_letters:
            for k in third_last_letters:
                random_last.append(i + j + k)
    years = ['51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
    with open ('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in area_codes:
            for j in years:
                for k in random_last:
                    writer.writerow([i + j + k])

gen_plates()

