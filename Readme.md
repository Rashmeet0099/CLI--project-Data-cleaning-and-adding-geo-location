#Readme.md

# 📍 GeoEnrich CLI Tool

A powerful and lightweight Python CLI tool to enrich address data in a CSV file with geolocation (latitude and longitude) coordinates using the [OpenCage Geocoding API](https://opencagedata.com/).

---

## 🚀 Features

- ✅ Validate and clean address data from CSV files
- 🌐 Automatically fetch latitude and longitude for residential and postal addresses
- 📦 Save enriched data into a new CSV file
- 🧪 Built-in testing with `pytest`
- 🔐 Secure API key management using `.env` file

---

## 📁 Project Structure

```
GeoEnrich-CLI/
│
├── cli.py                # Main script to process input/output
├── geo.py                # Handles API requests and geolocation logic
├── validator.py          # Validates address fields in CSV
├── test_cli.py           # Unit tests using pytest
├── .env                  # Contains your API key (DO NOT COMMIT)
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore file (includes .env)
├── input/
│   └── sample.csv.csv    # Sample input CSV
├── output/
│   └── enriched_output.csv # Output after enrichment
```

---

## ⚙️ Installation

### 🐍 Requirements:
- Python 3.8+
- [OpenCage API Key](https://opencagedata.com/api)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/GeoEnrich-CLI.git
cd GeoEnrich-CLI
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Setup Environment Variables

Create a `.env` file in the root directory and add your OpenCage API key:

```env
OPEN_KEY=your_opencage_api_key_here
```

> 🔗 You can get a free key from [OpenCageData](https://opencagedata.com/)

Add `.env` to `.gitignore` to keep your API key safe:

```bash
echo .env >> .gitignore
```

---

## 📌 Usage

### Run the tool:
```bash
python cli.py input.csv output.csv
```

### Example:
```bash
python cli.py sample.csv.csv enriched_output.csv
```

- `input.csv` — your input file with address data (must have at least 16 columns)
- `output.csv` — the output file with additional lat/lng fields

---

## 🧪 Running Tests

We use `pytest` to test validation and geolocation logic.

```bash
pytest test_cli.py
```

---

## 🧠 How It Works

1. **Validation** – Ensures each row contains the required fields.
2. **Geolocation** – Calls the OpenCage API to get:
   - Residential address coordinates
   - Postal address coordinates
3. **Enrichment** – Appends lat/lng to appropriate columns.
4. **Output** – Writes to CSV with added `res_lat`, `res_lng`, `post_lat`, `post_lng`.

---

## 💡 Sample Input Format (First 16 Columns)

| Email | First Name | Last Name | Res Address | Res City | Res State | Res Postcode | Res Lat | Res Lng | ... | Post Address | Post City | Post State | Post Postcode | Post Lat | Post Lng |
|-------|------------|-----------|-------------|----------|-----------|---------------|----------|----------|-----|---------------|------------|-------------|----------------|-----------|-----------|

> 🚫 If a row has fewer than 16 columns or missing critical fields, it will be skipped.

---

## 📌 Reference Links

- 🌍 [OpenCage Geocoding API](https://opencagedata.com/)
- 📘 [Python `dotenv`](https://pypi.org/project/python-dotenv/)
- 🧪 [pytest Documentation](https://docs.pytest.org/en/stable/)
- 🐍 [csv module](https://docs.python.org/3/library/csv.html)

---

## 🔐 Security Tips

- Never commit your `.env` file or API keys to public repositories.
- Use `.gitignore` to exclude sensitive files.
- Consider using environment-specific `.env.production`, `.env.dev`, etc.

---

## 🙌 Contributions

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

---

## 📄 License

MIT License — feel free to use, modify, and distribute with credit.

---

## ✨ Author

Made with ❤️ by [Rashmeet Singh](https://github.com/rashmeet-singh)
