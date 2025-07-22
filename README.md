# 🌍 IP Address Info Tool

A simple Python CLI tool that uses the `ipapi` package to fetch location and ISP information about IP addresses using the [ipapi.co](https://ipapi.co) API.

---

## 🔧 Features

- Lookup details for **any IP address**
- Automatically detect and locate **your own IP** (if none is provided)
- Command-line interface using `argparse`
- Web interface for easy IP lookups
- Displays:
  - City, region, country
  - Coordinates (latitude & longitude)
  - Timezone, postal code, country code
  - ISP/organization and EU status

---

## 📦 Installation

### 1. Clone the repository:
```bash
git clone https://github.com/Kamseyz/ip-locator.git
cd ip-locator
```

### 2. Create and activate virtual environment:

**For Linux/Mac:**
```bash
python -m venv myenv
source myenv/bin/activate
```

**For Windows:**
```bash
python -m venv myenv
myenv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Web Interface
To use the web interface, start the server:
```bash
python manage.py runserver
```
Then open your browser and navigate to the displayed URL (usually `http://127.0.0.1:8000/`).

### Command Line Interface (CLI)

#### Get your own IP information:
```bash
cd ip_locator
python my_ip.py
```

#### Get information for a specific IP address:
```bash
python my_ip.py --ip <IP_ADDRESS>
```

**Example:**
```bash
python my_ip.py --ip 8.8.8.8
```

### Sample Output:
```
IP Address: 8.8.8.8
City: Mountain View
Region: California
Country: United States
Latitude: 37.42301
Longitude: -122.083352
Timezone: America/Los_Angeles
Postal Code: 94043
Country Code: US
ISP: Google LLC
Organization: Google LLC
ASN: AS15169
EU: False
```

---

## 📁 Project Structure

```
ip-locator/
├── Ip_locator/
│   ├── my_ip.py          
│   └── ...
├── requirements.txt       
├── manage.py             
└── README.md           
```

---

## 🔗 API Information

This tool uses the [ipapi.co](https://ipapi.co) API service to retrieve IP geolocation data. The free tier allows for limited requests per day.

---

