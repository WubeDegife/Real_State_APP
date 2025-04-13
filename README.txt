Sacramento Real Estate Explorer
================================

Overview:
---------
This Streamlit app allows users to explore real estate transactions in Sacramento. The app provides:
  - Interactive property listings with filters (city, street name, price range, square footage).
  - Visualizations including price distribution, average price by city, and price per square foot over time.
  - An interactive map (using Plotly Express) displaying property locations.
  - Export options to download filtered data (CSV) and chart images (PNG/PDF).

Installation:
-------------
1. Clone or download this repository to your local machine.
2. Ensure you have Python (version 3.7 or later) installed.
3. (Optional) Set up a virtual environment:
   - For example, using venv:
     > python -m venv env
     > source env/bin/activate        (Linux/Mac)
     > env\Scripts\activate           (Windows)
4. Install the required Python packages:
   > pip install -r requirements.txt
5. Place the file "Sacramentorealestatetransactions.csv" in the same directory as the main application script (e.g., app.py).

Usage:
------
To launch the app locally:
  > streamlit run app.py

Inside the app you can:
  - Use the sidebar to filter listings based on city, street name, price, and square footage.
  - Navigate between tabs:
     * Listings: See detailed property listings.
     * Visualizations: View charts (price histogram, average price bar chart, price per sqft scatter plot) and export charts.
     * Export: Download filtered data as CSV.
     * Map: Explore an interactive map of property listings.
  - Interact with the charts and map just like other visualizations in the app.

File Structure:
---------------
- app.py                     : Main Streamlit application file.
- Sacramentorealestatetransactions.csv : CSV file containing real estate transactions.
- requirements.txt           : List of required Python packages.
- README.txt (or README.md)  : This documentation file.

Future Enhancements:
--------------------
- Expand filtering options and add more detailed search capabilities.
- Introduce additional visualizations or data analyses.
- Improve user interface and responsiveness.

Contact:
--------
For questions or issues, please reach out to [your-email@example.com].
