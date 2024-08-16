import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from styles import overall_css

def data_reading_and_exploration():
    # Apply CSS styles
    st.markdown(overall_css, unsafe_allow_html=True)
    
    # Heading for the section
    st.markdown("<h1>Data Reading and Exploration</h1>", unsafe_allow_html=True)
    
    # Reading the data
    st.markdown("<h2>Reading the Zomato Dataset</h2>", unsafe_allow_html=True)
    data = pd.read_csv('zomato.csv', encoding='latin-1')
    
    st.markdown(
        """
        <p>The dataset contains various attributes related to restaurants, such as:</p>
        <ul>
            <li><strong>Restaurant ID:</strong> A unique identifier assigned to each restaurant in the dataset.</li>
            <li><strong>Restaurant Name:</strong> The name of the restaurant.</li>
            <li><strong>Country Code:</strong> A numeric code representing the country where the restaurant is located.</li>
            <li><strong>City:</strong> The city where the restaurant is located.</li>
            <li><strong>Address:</strong> The complete address of the restaurant.</li>
            <li><strong>Locality:</strong> A specific area or neighborhood within the city where the restaurant is situated.</li>
            <li><strong>Locality Verbose:</strong> A more detailed description of the locality, often including landmarks or additional context.</li>
            <li><strong>Longitude:</strong> The geographical longitude coordinate of the restaurant's location.</li>
            <li><strong>Latitude:</strong> The geographical latitude coordinate of the restaurant's location.</li>
            <li><strong>Cuisines:</strong> The types of cuisines offered by the restaurant, such as North Indian, Mughlai, Italian, etc.</li>
            <li><strong>Average Cost for two:</strong> The average cost of a meal for two people at the restaurant.</li>
            <li><strong>Currency:</strong> The currency in which prices are listed, such as Indian Rupees (Rs.) or South African Rand (R).</li>
            <li><strong>Has Table booking:</strong> Indicates whether the restaurant offers table booking services.</li>
            <li><strong>Has Online delivery:</strong> Indicates whether the restaurant provides online delivery services.</li>
            <li><strong>Is delivering now:</strong> Indicates whether the restaurant is currently delivering food.</li>
            <li><strong>Switch to order menu:</strong> A flag indicating if there is an option to switch to an order menu.</li>
            <li><strong>Price range:</strong> A numeric value representing the price range category of the restaurant.</li>
            <li><strong>Aggregate rating:</strong> The average rating of the restaurant based on customer reviews.</li>
            <li><strong>Rating color:</strong> The color code associated with the aggregate rating.</li>
            <li><strong>Rating text:</strong> A textual representation of the rating.</li>
            <li><strong>Votes:</strong> The total number of votes or reviews the restaurant has received from customers.</li>
        </ul>
        """, unsafe_allow_html=True
    )
    
    # Display first few rows
    st.markdown("<h2>First 3 Rows of the Dataset</h2>", unsafe_allow_html=True)
    st.write(data.head(3))
    
    # Display last few rows
    st.markdown("<h2>Last 3 Rows of the Dataset</h2>", unsafe_allow_html=True)
    st.write(data.tail(3))
    
    # Display random sample rows
    st.markdown("<h2>Random Sample of 3 Rows from the Dataset</h2>", unsafe_allow_html=True)
    st.write(data.sample(3))
    
    return data

def feature_transformation(data):
    # Heading for the section
    st.markdown("<h1>Feature Engineering</h1>", unsafe_allow_html=True)
    st.markdown("<h2>1. Feature Transformation</h2>", unsafe_allow_html=True)
    
    # Load country code data
    df_country = pd.read_excel('Country-Code.xlsx')
    st.markdown("<h3>Country Code Data</h3>", unsafe_allow_html=True)
    st.write(df_country.head())
    
    # Merge data with country code
    data = pd.merge(data, df_country, on='Country Code', how='left')
    st.markdown("<h3>Data After Merging with Country Code</h3>", unsafe_allow_html=True)
    st.write(data.head(2))
    
    # Extract information from Locality
    data[['Mall', 'Area', 'City from Locality']] = data['Locality'].str.split(', ', expand=True, n=2)
    st.markdown("<h3>Data After Extracting Locality Information</h3>", unsafe_allow_html=True)
    st.write(data.head(2))
    
    # Drop unnecessary columns
    data.drop(columns=['Restaurant ID', 'Address', 'Locality Verbose','Switch to order menu', 'Locality', 'City from Locality', 'Country Code', 'Rating color'], inplace=True)
    st.markdown("<h3>Data After Dropping Unnecessary Columns</h3>", unsafe_allow_html=True)
    st.write(data.head(2))

    # Display data types before conversion
    st.markdown("<h2>Data Types Before Conversion</h2>", unsafe_allow_html=True)
    st.write(data.dtypes)
    
    # Convert object columns to categorical if they represent categorical data
    categorical_columns = ['Restaurant Name', 'City', 'Cuisines', 'Currency', 
                           'Has Table booking', 'Has Online delivery', 'Is delivering now', 
                           'Rating text', 'Area', 'Country', 'Price range']
    data[categorical_columns] = data[categorical_columns].astype('category')
    
    # Display the data types of the columns after conversion
    st.markdown("<h2>Data Types After Conversion</h2>", unsafe_allow_html=True)
    st.write(data.dtypes)
    
    # Count numerical and categorical columns
    num_numerical = data.select_dtypes(include=['number']).shape[1]
    num_categorical = data.select_dtypes(include=['category', 'object']).shape[1]
    
    # Display the counts
    st.markdown("<h2>Numerical and Categorical Columns Count</h2>", unsafe_allow_html=True)
    st.write(f"Numerical Columns: {num_numerical}")
    st.write(f"Categorical Columns: {num_categorical}")
    
    return data

def data_cleaning(data):
    # Heading for the section
    st.markdown("<h1>Data Cleaning</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Handling Null Values</h2>", unsafe_allow_html=True)
    
    # Display initial shape of the data
    st.markdown("<h3>Initial Shape of the Data</h3>", unsafe_allow_html=True)
    st.write(data.shape)
    
    # Display count of null values in each column
    st.markdown("<h3>Count of Null Values in Each Column</h3>", unsafe_allow_html=True)
    st.write(data.isnull().sum())
    
    # Drop the 'Area' column
    data.drop(columns=['Area'], inplace=True)
    st.markdown("<h3>Data After Dropping 'Area' Column</h3>", unsafe_allow_html=True)
    st.write(data.head(2))
    
    # Drop rows with any null values
    data.dropna(inplace=True)
    
    # Display count of null values in each column after dropping
    st.markdown("<h3>Count of Null Values After Dropping Rows with Null Values</h3>", unsafe_allow_html=True)
    st.write(data.isnull().sum())
    st.image("null.png", caption="Null Values Heatmap")
    
    # Display final shape of the data
    st.markdown("<h3>Final Shape of the Data</h3>", unsafe_allow_html=True)
    st.write(data.shape)
    
    return data


# Primary data analysis function
def primary_data_analysis(data):
    st.markdown("<h1>Exploratory Data Analysis (EDA)</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Primary Analysis of Data</h2>", unsafe_allow_html=True)
    
    # Display the first few rows of the dataset
    st.markdown("<h3>First Few Rows of the Dataset</h3>", unsafe_allow_html=True)
    st.write(data.head(2))
    
    # Check the size of the dataset
    data_shape = data.shape
    st.markdown(f"<h3>The dataset contains {data_shape[0]} rows and {data_shape[1]} columns.</h3>", unsafe_allow_html=True)
    
    # Attribute Information
    st.markdown("<h3>Attribute Information</h3>", unsafe_allow_html=True)
    # buffer = io.StringIO()
    # data.info(buf=buffer)
    # info_str = buffer.getvalue()
    # st.text(info_str)
    
    # Check for missing values
    st.markdown("<h3>Missing Values</h3>", unsafe_allow_html=True)
    missing_values = data.isnull().sum()
    st.write(missing_values[missing_values > 0])
    
    # Check for duplicate rows
    duplicate_rows = data.duplicated().sum()
    st.markdown(f"<h3>There are {duplicate_rows} duplicate rows in the dataset.</h3>", unsafe_allow_html=True)
    
    # Check the data types of each column
    st.markdown("<h3>Data Types of Each Column</h3>", unsafe_allow_html=True)
    st.write(data.dtypes)
    
    # Get the data types of each column
    data_types = data.dtypes
    
    # Count the number of numerical and categorical columns
    num_numerical = data_types[data_types.apply(lambda x: pd.api.types.is_numeric_dtype(x))].count()
    num_categorical = data_types[data_types.apply(lambda x: pd.api.types.is_categorical_dtype(x) or pd.api.types.is_object_dtype(x))].count()
    
    st.markdown(f"<h3>Number of numerical columns: {num_numerical}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3>Number of categorical columns: {num_categorical}</h3>", unsafe_allow_html=True)
    
    # Get numerical and categorical column names
    numerical_columns = data.select_dtypes(include=['number']).columns.tolist()
    categorical_columns = data.select_dtypes(include=['category', 'object']).columns.tolist()
    
    # Print the column names
    st.markdown("<h3>Numerical Columns</h3>", unsafe_allow_html=True)
    st.write(numerical_columns)
    
    st.markdown("<h3>Categorical Columns</h3>", unsafe_allow_html=True)
    st.write(categorical_columns)
    
    # Print the count of unique categories for each categorical column
    st.markdown("<h3>Count of Unique Categories for Each Categorical Column</h3>", unsafe_allow_html=True)
    for column in categorical_columns:
        st.write(f"{column}: {data[column].nunique()} unique categories")
    
    # Define the function to apply top N categories and replace others with 'Other'
    def replace_with_other(data, column_name, top_n=10):
        top_categories = data[column_name].value_counts().nlargest(top_n).index
        data[column_name] = data[column_name].apply(lambda x: x if x in top_categories else 'Other')
    
    # Apply the function to each column and save the result in a new DataFrame
    data_clean = data.copy()  # Create a copy of the original DataFrame
    columns = ['Restaurant Name', 'City', 'Cuisines', 'Mall']
    for col in columns:
        replace_with_other(data_clean, col)
    
    # Print the count of unique categories for each categorical column
    st.markdown("<h3>Count of Unique Categories for Each Categorical Column After Transformation</h3>", unsafe_allow_html=True)
    for column in categorical_columns:
        st.write(f"{column}: {data_clean[column].nunique()} unique categories")
    
    st.markdown("<h2>Observations</h2>", unsafe_allow_html=True)
    st.markdown("""
    **Data Completeness**: The dataset consists of 9551 unique restaurant entries with no duplicate rows. It has 9 missing values in the Cuisines column, which may affect the completeness of cuisine-related analysis.

    **Categorical Information:** Key categorical features include Country Code, City, and service-related attributes such as Has Table booking and Has Online delivery, providing insights into restaurant locations and service offerings.

    **Numerical Metrics:** Includes Longitude and Latitude for spatial analysis, Average Cost for two for pricing insights, and Aggregate rating for assessing restaurant quality based on customer reviews.

    **Service Availability:** The dataset highlights whether restaurants offer features like table booking, online delivery, or are currently delivering, which can be used to evaluate the availability and popularity of these services.
    
    **Pricing and Currency:** Details local currencies and pricing ranges, facilitating financial analysis and comparison of restaurant costs across different regions and currencies.
    """, unsafe_allow_html=True)

# Mathematical data analysis function
def mathematical_data_analysis(data):
    st.markdown("<h1>Mathematical Analysis of Data</h1>", unsafe_allow_html=True)

    # Get a statistical summary of the dataset
    st.markdown("<h2>Statistical Summary</h2>", unsafe_allow_html=True)
    st.write(data.describe())

    # Select only numeric columns
    numeric_data = data.select_dtypes(include=[np.number])

    # Compute the variance of the numeric columns
    variance = numeric_data.var()
    st.markdown("<h2>Variance of Numeric Columns</h2>", unsafe_allow_html=True)
    st.write(variance)

    # Compute the covariance matrix of the numeric columns
    covariance_matrix = numeric_data.cov()
    st.markdown("<h2>Covariance Matrix of Numeric Columns</h2>", unsafe_allow_html=True)
    st.write(covariance_matrix)
    st.image("cov.png", caption="Covariance of Data")

    # Pearson Correlation Coefficient
    pearson_corr = numeric_data.corr(method='pearson')
    st.markdown("<h2>Pearson Correlation Coefficient</h2>", unsafe_allow_html=True)
    st.write(pearson_corr)
    st.image("heatmap0.png", caption="Pearson Correlation Coefficient")

    # Spearman Rank Correlation Coefficient
    spearman_corr = numeric_data.corr(method='spearman')
    st.markdown("<h2>Spearman Rank Correlation Coefficient</h2>", unsafe_allow_html=True)
    st.write(spearman_corr)
    st.image("heatmap1.png", caption="Spearman Rank Correlation Coefficient")

    # Kendall Rank Correlation Coefficient
    kendall_corr = numeric_data.corr(method='kendall')
    st.markdown("<h2>Kendall Rank Correlation Coefficient</h2>", unsafe_allow_html=True)
    st.write(kendall_corr)
    st.image("heatmap2.png", caption="Kendall Rank Correlation Coefficient")

    st.markdown("<h2>Mathematical Observations</h2>", unsafe_allow_html=True)
    st.image("dist1.png")
    st.image("dist2.png")
    st.image("dist3.png")
    st.image("dist4.png")
    st.image("dist5.png")
    st.image("bar.png")
    st.markdown("""
    **Distribution Characteristics:** The numerical columns exhibit a wide range of values with high variance, indicating substantial variability in Average Cost for two, Votes, and Restaurant ID.

    **Correlation Insights:** There is a moderate negative correlation between Aggregate rating and Restaurant ID, and a moderate positive correlation between Aggregate rating and Votes. Average Cost for two shows weak correlations with other variables.

    **Covariance Analysis:** The covariance matrix reveals significant variability in Average Cost for two and Votes, with negative covariance between Restaurant ID and other features, suggesting complex relationships.

    **Non-Normal Distribution:** Numerical features are not normally distributed, as indicated by varying means and standard deviations, impacting the applicability of standard statistical tests.

    **Ranking Correlations:** Pearson and Spearman correlations suggest weak to moderate relationships among numerical columns, with stronger relationships observed in rankings for Aggregate rating and Votes.
    """, unsafe_allow_html=True)


def Exploration():
    st.title('Zomato Data Cleaning and Feature Transformation')
    # Call the functions to execute
    data = data_reading_and_exploration()
    data = feature_transformation(data)
    # Data cleaning
    data = data_cleaning(data)
    
    # Display the final cleaned data
    st.markdown("<h1>Cleaned Data</h1>", unsafe_allow_html=True)
    st.write(data.head())

    # Primary data analysis
    primary_data_analysis(data)

    # Mathematical data analysis
    mathematical_data_analysis(data)

    st.header('Categorical Columns')
    st.header('Count Plots')
    st.image("count1.png")
    st.image("count2.png")
    st.image("count3.png")
    st.image("count4.png")
    st.image("count5.png")
    st.image("count6.png")

    st.header('Pi Charts')
    st.image("pi1.png")
    st.image("pi2.png")
    st.image("pi3.png")
    st.image("pi4.png")

    st.header('MultiVariate Analysis')
    st.image("multi1.png")
    st.image("multi2.png")
    st.image("multi3.png")
    st.image("best1.png")
    st.image("best2.png")
    st.image("best3.png")