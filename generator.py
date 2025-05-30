import os
import json
import argparse
import datetime
import requests
from faker import Faker

# Parser for command line arguments
parser = argparse.ArgumentParser(
    prog="Fake Profile Generator",
    description="Generate fake profiles with images"
)

parser.add_argument('--n', '--number', type=int, default=10, help='Amount of generated profiles')
parser.add_argument('--l', '--locale', type=str, default="es_ES", help='Language of fake profiles')

args = parser.parse_args()

# Change languane if needed
fake = Faker(args.l)

# Directories for photos and JSON
photos_dir = 'profiles/photos'
json_path = 'profiles/data.json'
os.makedirs(photos_dir, exist_ok=True)

# Function for custom serialization
def default_serializer(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    return str(obj)

# Data dictionary
data = []

for _ in range(args.n):
    fake_user = {
        'name': fake.name(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'address': fake.address(),
        'date_of_birth': fake.date_of_birth().isoformat(),
        'job': fake.job()
    }

    # Get fake image
    try:
        response = requests.get('https://thispersondoesnotexist.com/', timeout=10)
        if response.status_code == 200:
            filename = os.path.join(photos_dir, f"{fake_user['name'].replace(' ', '_')}.jpg")
            with open(filename, "wb") as fp:
                fp.write(response.content)

            fake_user["filename"] = filename
            data.append(fake_user)

    except Exception as e:
        print(f"Error al descargar imagen: {e}")

        

# Save JSON data
os.makedirs("profiles", exist_ok=True)
with open(json_path, "w", encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False, default=default_serializer)

# Exit message
print(f"{args.n} perfiles generados correctamente.")
