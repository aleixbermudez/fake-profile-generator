# 🧪 Fake Profile Generator

A Python CLI tool that generates **realistic fake user profiles** for testing, development, or demo purposes. Each profile includes personal details (name, email, phone, address, job, birthday) and even a **fake AI-generated profile photo**.

This project is perfect for developers, designers, educators, and QA engineers who need mock data without exposing any real personal information.

---

## ✨ Features

- ✅ Generate any number of fake user profiles
- 🌍 Multi-language support using locale (e.g. `en_US`, `es_ES`, etc.) (Coming soon)
- 🖼️ Automatically downloads a realistic fake profile picture
- 💾 Exports profiles as `.json` (CSV support Coming soon)
- 📁 Creates a folder structure to organize output data
- ⚡ Fast and easy to use from the terminal

---

## 🧰 Technologies Used

- [`Faker`](https://faker.readthedocs.io/) – Generate fake user data
- [`Requests`](https://docs.python-requests.org/) – Download profile pictures
- Python Standard Library (`argparse`, `os`, `json`, `datetime`, etc)

---

## 📦 Installation

Clone this repository and install the dependencies:

```bash
git clone https://github.com/yourusername/fake-profile-generator.git
cd fake-profile-generator
pip install -r requirements.txt
```

Make sure you’re using Python 3.7 or higher.

---

## ⚙️ Usage

You can run the generator from the command line:

```bash
python main.py --n 5
```

### Available Arguments

| Flag         | Description                                             | Default   |
|--------------|---------------------------------------------------------|-----------|
| `--num`      | Number of profiles to generate                          | `1`       |
| `--locale`   | Faker locale to use (`en_US`, `es_ES`, etc.) (Soon)     | `es_ES`   |
| `--output`   | Output format: `json` or `csv` (Soon)                   | `json`    |

---

## 📁 Output Structure

Once you run the tool, a `/profiles/` directory is created automatically:

```
fake-profile-generator/
├── main.py
├── generator.py
├── profiles/
│   ├── data.json
│   └── photos/
│       ├── profile_name.jpg
│       └── profile_name.jpg
```
## 🖼️ About the Profile Photos

For every generated profile, the script fetches a realistic, AI-generated face from:

https://thispersondoesnotexist.com

---

These images are not of real people. This ensures ethical usage of data while keeping the profiles visually realistic.

---

## 🧪 Example Output

Here’s an example of a single generated profile:

```json
{
  "name": "Lucía Fernández",
  "email": "lucia.fernandez91@example.com",
  "phone_number": "+34 612 345 678",
  "address": "Calle Mayor 123, Madrid, España",
  "date_of_birth": "1991-08-14",
  "job": "UX Designer",
  "photo": "photos/profile_001.jpg"
}
```

---

## 🤝 Contributing

Contributions are welcome! If you have an idea for a feature, improvement, or fix, feel free to fork the repo and open a pull request.

---

## 🧑‍💻 Author

Made with ❤️ and curiosity by [Aleix](https://github.com/aleixbermudez)  
If you find this useful, feel free to ⭐️ the repo!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Use it freely, modify it, and build cool stuff!
