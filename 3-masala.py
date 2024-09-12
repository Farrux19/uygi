import os; os.system("cls")
import json

matn = [
    {
        "title": "BAA dirhami",
        "code": "AED",
        "cb_price": "3454.05",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Avstraliya dollari",
        "code": "AUD",
        "cb_price": "8458.23",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Kanada dollari",
        "code": "CAD",
        "cb_price": "9349.78",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Shveytsariya franki",
        "code": "CHF",
        "cb_price": "14966.04",
        "nbu_buy_price": "14750.00",
        "nbu_cell_price": "15450.00",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Xitoy yuani",
        "code": "CNY",
        "cb_price": "1782.12",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Daniya kronasi",
        "code": "DKK",
        "cb_price": "1876.76",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Misr funti",
        "code": "EGP",
        "cb_price": "262.30",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Yevro",
        "code": "EUR",
        "cb_price": "14004.86",
        "nbu_buy_price": "13800.00",
        "nbu_cell_price": "14040.00",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Angliya funt sterlingi",
        "code": "GBP",
        "cb_price": "16617.05",
        "nbu_buy_price": "16400.00",
        "nbu_cell_price": "17050.00",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Islandiya kronasi",
        "code": "ISK",
        "cb_price": "91.95",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Yaponiya iyenasi",
        "code": "JPY",
        "cb_price": "88.62",
        "nbu_buy_price": "70.00",
        "nbu_cell_price": "90.00",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Koreya respublikasi voni",
        "code": "KRW",
        "cb_price": "9.46",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Quvayt dinori",
        "code": "KWD",
        "cb_price": "41527.69",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Qozog‘iston tengesi",
        "code": "KZT",
        "cb_price": "26.56",
        "nbu_buy_price": "15.00",
        "nbu_cell_price": "30.00",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Livan funti",
        "code": "LBP",
        "cb_price": "0.14",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Malayziya ringgiti",
        "code": "MYR",
        "cb_price": "2921.52",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Norvegiya kronasi",
        "code": "NOK",
        "cb_price": "1174.70",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Polsha zlotiysi",
        "code": "PLN",
        "cb_price": "3269.18",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Rossiya rubli",
        "code": "RUB",
        "cb_price": "139.09",
        "nbu_buy_price": "125.00",
        "nbu_cell_price": "145.00",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Shvetsiya kronasi",
        "code": "SEK",
        "cb_price": "1223.37",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",

        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Singapur dollari",
        "code": "SGD",
        "cb_price": "9721.62",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Turkiya lirasi",
        "code": "TRY",
        "cb_price": "372.50",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "Ukraina grivnasi",
        "code": "UAH",
        "cb_price": "307.96",
        "nbu_buy_price": "null",
        "nbu_cell_price": "null",
        "date": "11.09.2024 11:00:01"
    },
    {
        "title": "AQSh dollari",
        "code": "USD",
        "cb_price": "12686.71",
        "nbu_buy_price": "12670.00",
        "nbu_cell_price": "12730.00",
        "date": "11.09.2024 11:00:01"
    }
]

davlat = sorted(matn,key=lambda a: a["title"])

f1 = open("NBU2.json","w")
json.dump(davlat, f1, indent=4)

print("faylga yozildi")