import json


def extract_company_data(data):
    result = []

    if "children" in data:
        for child in data["children"]:
            company_info = (child["title"], child["id"])
            result.append(company_info)

            if "children" in child:
                result.extend(extract_company_data(child))

    return tuple(result)


# Загрузка данных из файла
with open('new_test_hw.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Пример использования
result = extract_company_data(json_data)
print(result)
