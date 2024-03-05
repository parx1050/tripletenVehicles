# tripletenVehicles

Hello! Welcome to my Sprint 4 Project: A Sample Application

This application can be run with Streamlit on a local server or with Render: https://tripletenvehicles.onrender.com

The following details the heirarchy of the project:
├── README.md
├── app.py
├── vehicles_us.csv
└── notebooks
    └── EDA.ipynb
└── .streamlit
    └── config.toml
└── .conda
    └── ...
├── .gitignore

The README.md is this current file, which details everything in the project.
The app.py file contains the Python code used to run the application. You can run the application from your system console with the "$ streamlit app.py run" command.
The EDA.ipynb file is a Jupyter Notebooks file that performs basic EDA analysis on the dataset, plotting histograms and displaying info for the data.
The vehicles_us.csv file contains the dataset for this project, detailing about 51,000 different data points for vehicles, and columns for:
    - price
    - model_year
    - model
    - condition
    - cylinders
    - fuel
    - odometer
    - transmission
    - type
    - paint_color
    - is_4wd
    - date_posted
    - days_listed
All other files are background functions for the execution of the project.

The project itself provides three options for users to interact with the dataset:
    - The user can look through the whole dataset formatted as a Pandas DataFrame, and apply any combination of the four following filters to the dataset:
        - Vehicles That Cost At Least $100,000 Only
        - Vehicles Released in 2014 Only
        - Vehicles Listed for More Than 100 Days Only
        - Manual Transmission Only
    - The user can display a histogram for any of the columns in the dataset DataFrame (except for "is_4wd" or "date_posted").
    - The user can display a scatterplot comparing vehicle prices with the type of vehicle, plotted over the different model year releases. 
        The user is able to click on the different types of vehicles to filter what is displayed on the scatterplot.
