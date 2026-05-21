# newproject1

A small Python project with an interactive Streamlit dashboard and a simple utility script.

## Overview

| File | Description |
|------|-------------|
| `test.py` | Interactive dashboard built with Streamlit over synthetic sample data |
| `secound.py` | Minimal script that prints a greeting |

## Requirements

- Python 3.8+
- Dependencies: `streamlit`, `pandas`, `numpy`

Install dependencies:

```bash
pip install streamlit pandas numpy
```

## Usage

### Streamlit dashboard

```bash
streamlit run test.py
```

Opens a Hebrew-language demo dashboard with:

- Sidebar filters for category (multiselect) and date range
- Filtered data table
- Bar chart: average value per category
- Line chart: value over time

### Hello script

```bash
python secound.py
```

Expected output: `hello moty`

## Project structure

```
newproject1/
├── test.py       # Streamlit dashboard
├── secound.py    # Simple greeting script
└── README.md     # Project documentation
```

## Dashboard details (`test.py`)

- Generates 200 rows of synthetic data (categories A/B/C, numeric values, dates from 2023)
- Filters data by selected categories and date range
- Displays filtered results and two charts

## License

Personal / learning project — adjust as needed.
