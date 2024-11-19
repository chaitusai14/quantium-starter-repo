
# **Soul Foods Sales Data Visualizer**

This project is a web application that visualizes sales data for "Pink Morsel" products. The application is built using Python and the Dash framework, with a focus on interactivity and user-friendly design. It includes scripts for data processing, visualization, and automated testing.

---

## **Table of Contents**

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Testing](#testing)
- [Improvements and Future Work](#improvements-and-future-work)
- [Contributing](#contributing)

---

## **Overview**

This project processes and visualizes sales data for a fictional product, "Pink Morsel." It aims to provide insights into sales trends, highlighting key events like price increases and highest sales dates. Users can filter data by region and view interactive line charts.

---

## **Features**

1. **Data Processing**:
   - Cleans and formats raw sales data.
   - Filters for "Pink Morsel" products only.
   - Calculates total sales (`price * quantity`) and selects relevant columns.

2. **Interactive Dashboard**:
   - Built using Dash.
   - Displays sales trends with interactive region filters.
   - Highlights key events with annotations.

3. **Automated Testing**:
   - Tests ensure the presence of critical UI elements (header, chart, and region picker).
   - Utilizes Selenium WebDriver for browser-based testing.

4. **Automation**:
   - A Bash script automates the testing process and provides feedback on test results.

---

## **Installation**

### Prerequisites
- Python 3.8 or higher
- Node.js (optional for advanced Dash configurations)
- Virtual environment tools (`venv` or `virtualenv`)
- Google Chrome browser (for testing)
- ChromeDriver (managed by `webdriver_manager`)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/chaitusai14/quantium-starter-repo.git
   cd soul-foods-visualizer
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the ChromeDriver for testing:
   ```bash
   pip install webdriver-manager
   ```

---

## **Usage**

1. **Data Processing**:
   Run the data munging script to process raw sales data:
   ```bash
   python data_munging.py
   ```

2. **Run the Dashboard**:
   Start the Dash application:
   ```bash
   python dash_visual.py
   ```
   Open your browser and navigate to `http://127.0.0.1:8050` to view the app.

3. **Automated Testing**:
   Run the tests with the provided Bash script:
   ```bash
   bash bash_script.sh
   ```

---

## **File Descriptions**

1. **`data_munging.py`**:
   - Processes raw sales data from multiple CSV files.
   - Filters, cleans, and formats data for visualization.

2. **`dash_visual.py`**:
   - Implements the Dash application.
   - Provides an interactive line chart of sales data.

3. **`test_app.py`**:
   - Contains automated tests for the Dash application.
   - Tests the presence of UI elements and functionality.

4. **`bash_script.sh`**:
   - Automates the testing process using `pytest`.

5. **Raw Data Files**:
   - `daily_sales_data_0.csv`
   - `daily_sales_data_1.csv`
   - `daily_sales_data_2.csv`

6. **Formatted Data**:
   - `formatted_sales_data.csv`: Processed data for visualization.

---

## **Testing**

Automated tests are written using `pytest` and `dash.testing`. To execute the tests, run:

```bash
bash bash_script.sh
```

Tests include:
- **Header Test**: Verifies the header text.
- **Chart Test**: Confirms the presence of the sales line chart.
- **Filter Test**: Checks the region picker functionality.

---

## **Improvements and Future Work**

1. **Continuous Integration (CI) Integration**:
   - Plan to integrate the test suite with a CI/CD pipeline using GitHub Actions.
   - This will ensure automated testing on every code change, maintaining high code quality and reducing the risk of errors.

2. **Additional Visualizations**:
   - Expand the app's functionality by including additional charts, such as:
     - Regional sales comparisons using bar charts.
     - Profitability trends over time.

3. **Enhanced Testing**:
   - Extend the test suite to cover:
     - Annotation functionality (e.g., tooltips for significant events like price increases).
     - Validation of interactive elements (e.g., region filters and graph updates).
   - Include performance testing to measure load times and app responsiveness.

4. **Dynamic Data Input**:
   - Implement a feature that allows users to upload their datasets directly through the app, making it versatile for various use cases.

5. **Deployment**:
   - Deploy the application on a cloud platform (e.g., Heroku, AWS, or Azure) to make it accessible online for broader use.

6. **User Experience Enhancements**:
   - Improve the UI by adding customizable themes and tooltips for better data interpretation.
   - Optimize responsiveness for mobile and tablet devices.

7. **Documentation and Code Samples**:
   - Provide detailed usage documentation and example datasets for users to test the application.

---

## **Contributing**

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your branch.
4. Submit a pull request.

---

