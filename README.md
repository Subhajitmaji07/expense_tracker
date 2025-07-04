# Expense Tracker

## Overview

The Expense Tracker is a web application built using Streamlit that allows users to track their expenses. Users can add expenses, upload a CSV file to load existing expenses, and visualize their spending by category using bar charts.

## Features

- **Add Expense**: Users can input the date, category, amount, and description of an expense.
- **Load Expenses**: Users can upload a CSV file to load previously recorded expenses.
- **Save Expenses**: Users can save their current expenses to a CSV file.
- **Visualize Expenses**: Users can view a bar chart of their expenses categorized by type.

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   
   ```
2. Install the required packages:

   ```
   pip install streamlit pandas matplotlib seaborn
   
   ```
3. Run the application:

   ```
   streamlit run Expense_tracker.py
   
   ```

## Usage

1. **Add Expense**: 
   - Navigate to the sidebar and fill in the details for the expense (date, category, amount, and description).
   - Click the "Add" button to save the expense.
2. **Load Expenses**: 
   - Click the "Load Expenses" button to upload a CSV file containing previously recorded expenses.
3. **Save Expenses**: 
   - Click the "Save Expenses" button to save the current expenses to a CSV file named ```
     expense_data.csv
     ```

     .
4. **Visualize Expenses**: 
   - Click the "Visualize Expenses" button to generate a bar chart showing expenses by category.

## Code Structure

- **Expense_tracker.py**: The main application file containing the Streamlit code.
- **session_state**: Utilizes Streamlit's session state to manage the expense data throughout the user's session.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## Acknowledgments

- Thanks to the Streamlit community for their support and resources.
- Special thanks to the developers of Pandas, Matplotlib, and Seaborn for their powerful libraries that make data manipulation and visualization easy.
