# 🌍 Largest Economies Data Extraction Project

## 📌 Overview

This project extracts data on the **top 10 largest economies in the world (by nominal GDP)** from an archived Wikipedia page using Python.
The data is cleaned, processed, and saved into a CSV file for further analysis.

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas

---

## 📊 Features

* Extracts tables directly from a webpage
* Cleans and processes GDP data
* Converts GDP from **Million USD → Billion USD**
* Rounds values for readability
* Saves output to a CSV file

---

## 📁 Output

The final dataset is saved as:

```
Largest_economies.csv
```

It contains:

* Country names
* GDP values in Billion USD

---

## 🚀 How to Run

1. Install required libraries:

```
pip install pandas numpy lxml
```

2. Run the Python script:

```
python Practice_project.py
```

3. Check the output file in the same directory.

---

## 📌 Project Structure

```
python_problems/
│── Practice_project.py
│── Largest_economies.csv
│── README.md
```

---

## 💡 Notes

* The project uses an **archived Wikipedia page** to ensure consistent data.
* Table selection is handled carefully to avoid parsing issues.
* Data cleaning includes handling commas and missing values.

---

## 👨‍💻 Author

Created as part of a **data analysis practice project**.

---

## 📈 Future Improvements

* Add data visualization (bar charts)
* Automate table detection
* Export results to Excel or dashboards

---
