import requests

URL = "https://date.nager.at/api/v3/PublicHolidays/2026/KR"

# 응답
response = requests.get(URL)
holidays = response.json()

# 가장 많이 등장하는 공휴일 TOP3
count = {}

for holiday in holidays:
    name = holiday["localName"]
    count[name] = count.get(name, 0) + 1

# print(count)
top3 = sorted(count.items(), key=lambda x: x[1], reverse=True)[:3]

print("=== TOP 3 ===")
for i, (name, c) in enumerate(top3, 1):
    print(f"{i}. {name} ({c}회)")

