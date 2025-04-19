documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):
    for doc in documents:
        name = []
        if doc_number == doc['number']:
            name.append(doc['name'])
            return  (f'{"".join(name)}')
    return ("Документ не найден")

def get_directory(doc_number):
    for shelfs, numbers in directories.items():
        if doc_number in numbers:
            return shelfs
    return("Полки с таким документом не найдено")

def add_data(document_type, number, name, shelf_number):
    new_doc = {'type': document_type, 'number': number, 'name': name}
    documents.append(new_doc)
    if shelf_number in directories:
        directories[shelf_number].append(number)
    else:
        directories[shelf_number] = [number]
    return f'Данные добавлены на имя {name}'

if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    print(add_data('international passport', '311 020203', 'Александр Пушкин', 3))
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))