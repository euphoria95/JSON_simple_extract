import json
import sys

def load_json(input_file):
    try:
        with open(input_file, 'r') as file:
            data = file.read()
            # Rozdziela dane na oddzielne fragmenty JSON i parsuje każdy z nich
            json_objects = [json.loads(obj) for obj in data.split('\n') if obj.strip()]
            return json_objects
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
def extract_data(data, keys):
    extracted = {key: data.get(key) for key in keys}
    return extracted
    
def main(input_file, output_file):
    json_objects = load_json(input_file)

    # Zbieranie dostępnych kluczy z wszystkich obiektów JSON
    all_keys = set()
    for obj in json_objects:
        all_keys.update(obj.keys())
    
    print("Dostępne klucze:", ", ".join(all_keys))

    # Pobierz klucze od użytkownika
    keys = input("Wpisz klucze do ekstrakcji, oddzielone przecinkami: ").split(',')

    # Ekstrakcja danych z każdego obiektu JSON
    extracted_data = [extract_data(obj, keys) for obj in json_objects]

    # Zapis do pliku wyjściowego
    with open(output_file, 'w') as file:
        json.dump(extracted_data, file, indent=4)

    print("Dane zostały zapisane do", output_file)

# Reszta skryptu pozostaje taka sama


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Użycie: python3 skrypt.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    main(input_file, output_file)
