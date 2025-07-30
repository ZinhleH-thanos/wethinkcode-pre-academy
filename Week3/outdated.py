months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if '/' in date:
            m, d, y = map(int, date.split('/'))
            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y}-{m:02}-{d:02}")
                break
        elif ',' in date:
            month, rest = date.split(' ', 1)
            if month in months:
                d, y = rest.split(',')
                m = months.index(month) + 1
                if 1 <= int(d) <= 31:
                    print(f"{y.strip()}-{m:02}-{int(d):02}")
                    break
    except (ValueError, AttributeError):
        pass
