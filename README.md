This Python script is designed to process, clean, and visualize data from an IPL 2025 auction player dataset stored in a CSV file. It includes the following components:

File Cleaning:
Reads the CSV file using pandas.
Provides an overview of the data, including a preview (head), column information (info), and missing values.
Identifies and removes duplicate rows, resetting the index afterward.
Replaces placeholder values (-) in the "Team" column with "TBD" for clarity.

Data Analysis:
Groups data by key columns (Type, Team, Sold) and counts the occurrences in each group.
Uses pandas to summarize the dataset (describe) and check data types (dtypes).

Visualization:
Generates a bar chart for players based on their "Sold" status, highlighting player distribution across price ranges.
Adds value annotations above each bar for better readability.
Employs a dark-themed background and custom styles, such as rotated x-axis labels, white bar edges, and a shadowed legend.

Error Handling:
Catches file-related issues (FileNotFoundError) and logs meaningful error messages.
Handles issues like missing columns (KeyError) or uninitialized data (AttributeError) during visualization.

Execution:
The script first cleans the dataset by invoking clean_file.
It then visualizes key insights through analyze_visualize_file, showing a bar chart.
This program is modular, making it easy to extend or reuse for similar data-processing tasks. It also emphasizes robustness through error handling and meaningful logging.
