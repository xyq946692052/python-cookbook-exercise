prices = {
    'AMER': 45.23,
    'SANS': 56.02,
    'APPLE': 10.99,
    'ZHP': 56.20,
    'GOOG': 40.54,
    'KOLU': 20.89
}

ndt = {key:value for key, value in prices.items() if value>20}
print(ndt)

tech_names = {'ZHP', 'KOLU', 'AMER'}
tdt = {key:value for key, value in prices.items() if key in tech_names}
print(tdt)
