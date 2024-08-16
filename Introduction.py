# introduction.py
import streamlit as st
from styles import overall_css

def Introduction():
    # Apply CSS styles
    st.markdown(overall_css, unsafe_allow_html=True)
    
    
    # Introduction content
    st.markdown("<p>This is the GemanAI chatbot screen.</p>", unsafe_allow_html=True)
    
    # Section for detailed explanation and analysis
    st.markdown("<h2>Project Overview</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        In the bustling world of online food delivery, platforms like Zomato have become integral to connecting hungry customers with a plethora of dining options. Beyond facilitating online orders, Zomato offers a wealth of information about restaurants, reservations, and more, making it a resource for both food enthusiasts and restaurant owners.
        </p>
        <p>
        As someone who frequently availed food delivery services in India, the sight of numerous delivery personnel crowding around apartment complexes sparked my curiosity. It led me to ponder a series of questions: What would be the ideal city for opening a restaurant in India? Which cuisine is most popular? What food items are trending, and what price range attracts the most customers? Through extensive analysis, I aimed to uncover insights that could not only satisfy my curiosity but also offer valuable information for anyone considering entering the restaurant business.
        </p>
        """, unsafe_allow_html=True
    )

    st.markdown("<h2>Aims and Objectives</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        In this project, my aim is to provide comprehensive insights for aspiring restaurant owners in India. I will achieve this through:
        </p>
        <ul>
            <li><strong>City Analysis:</strong> Unveil the best city to open a restaurant</li>
            <li><strong>Cuisine Analysis:</strong> Discover the most-loved cuisines in the market</li>
            <li><strong>Dining Type Analysis:</strong> Understand the dining preferences of potential customers</li>
            <li><strong>Best Selling Items Analysis:</strong> Discover dishes with high customer appeal</li>
            <li><strong>Price Range Analysis:</strong> Determine the sweet spot for pricing dishes</li>
            <li><strong>Competitor Analysis:</strong> Gain insights into the local restaurant landscape</li>
        </ul>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h2>Steps of the Project</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        - <strong>Data Preprocessing:</strong> Clean and organize the dataset, address missing values and refine data quality
        </p>
        <p>
        - <strong>Exploratory Data Analysis (EDA) + Feature Engineering:</strong> Explore the dataset through EDA to uncover patterns, trends, and insights. Simultaneously perform feature engineering to derive new variables relevant to the project objectives.
        </p>
        <p>
        - <strong>Drawing Insights:</strong> Extract meaningful insights to address the aims and objectives
        </p>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h2>Technology Used</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        - <strong>Python:</strong> Serves as the primary programming language, providing versatility and efficiency in data analysis.
        </p>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h2>Dataset</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        I sought a restaurant dataset for analysis and chose Zomato due to its industry prominence in India. As Zomato doesn’t publicly release data, I used Kaggle to find publicly available datasets. Most of them did not fit my requirements, as they either had small data sizes or fewer features. The “Zomato Restaurants Dataset for Metropolitan Areas” from Kaggle fits my requirements perfectly. The dataset, comprising 123,657 rows and 12 columns, provides insights on food, dining, delivery, prices, and more across 13 Indian cities.
        </p>
        <p>
        The dataset includes:
        </p>
        <ul>
            <li><strong>Restaurant Name:</strong> Name of the restaurant</li>
            <li><strong>Dining Rating:</strong> Rating given by customers for the dining experience at the restaurant</li>
            <li><strong>Delivery Rating:</strong> Rating given by customers for the delivery service provided by the restaurant</li>
            <li><strong>Dining Votes:</strong> Number of votes or reviews received for the dining experience</li>
            <li><strong>Delivery Votes:</strong> Number of votes or reviews received for the delivery service</li>
            <li><strong>Cuisine:</strong> Type of cuisine or culinary style offered by the restaurant</li>
            <li><strong>Place Name:</strong> Name of the metropolitan area</li>
            <li><strong>City:</strong> Name of the metropolitan city where the restaurant is located</li>
            <li><strong>Item Name:</strong> Name of a specific dish or item offered by the restaurant</li>
            <li><strong>Best Seller:</strong> Indicates whether the item is a best-selling dish or not</li>
            <li><strong>Votes:</strong> Number of votes or reviews received for the specific item</li>
            <li><strong>Prices:</strong> Prices associated with each item offered by the restaurant</li>
        </ul>
        <p>
        One limitation of this dataset is that it does not contain data from all over India and is limited to 13 major cities alone. No ethical concerns are associated with using this dataset as it is publicly available on Kaggle.
        </p>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h2>Pre-requisites</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        - <strong>Pandas:</strong> A powerful data manipulation library in Python that provides data structures for efficiently storing large datasets and tools for working with them.
        </p>
        <p>
        - <strong>NumPy:</strong> A fundamental package for scientific computing in Python, providing support for large, multi-dimensional arrays and matrices, along with mathematical functions to operate on these arrays.
        </p>
        <p>
        - <strong>Matplotlib:</strong> A comprehensive data visualization library in Python that produces static visualizations.
        </p>
        <p>
        - <strong>Seaborn:</strong> A data visualization library based on Matplotlib that provides a high-level interface for creating informative and attractive statistical graphics.
        </p>
        <p>
        - <strong>Plotly Express:</strong> A high-level interface for creating interactive and expressive visualizations, allowing for the creation of dynamic and engaging charts with ease.
        </p>
        <p>
        - <strong>Fuzzywuzzy:</strong> A library for string matching and comparison, offering functions like fuzzy string matching to measure the similarity between strings.
        </p>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h2>Read Data</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        I loaded the dataset and examined the initial five rows along with their respective dataframe information to gain a feel of the data.
        </p>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h2>Data Preprocessing</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        - <strong>Change Column Names:</strong> Converted all column names to lowercase and used underscores to separate words.
        </p>
        <p>
        - <strong>Check Null Values:</strong> Replaced nulls in "dining_rating" and "delivery_rating" with 0. Encoded "BESTSELLER" as 1 and other values as 0 in "best_seller" column.
        </p>
        <p>
        - <strong>Check Duplicate Values:</strong> Checked and removed duplicate rows.
        </p>
        <p>
        - <strong>Check Irregularities in Columns:</strong> Used fuzzywuzzy for similar restaurant names and verified them.
        </p>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h2>Exploratory Data Analysis (EDA) + Feature Engineering</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        - <strong>City Analysis:</strong> Identified the ideal city for opening a restaurant.
        </p>
        <p>
        - <strong>Cuisine Analysis:</strong> Discovered the most-loved cuisines in the market.
        </p>
        <p>
        - <strong>Dining Type Analysis:</strong> Understood dining preferences of potential customers.
        </p>
        <p>
        - <strong>Best Selling Items Analysis:</strong> Discovered dishes with high customer appeal.
        </p>
        <p>
        - <strong>Price Range Analysis:</strong> Determined the optimal pricing strategy.
        </p>
        <p>
        - <strong>Competitor Analysis:</strong> Gained insights into the local restaurant landscape.
        </p>
        """, unsafe_allow_html=True
    )
    st.markdown("<h2>Drawing Insights</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        - <strong>Best City for Restaurant:</strong> The analysis revealed that <strong>[City Name]</strong> is the most promising city for opening a restaurant based on various factors like customer preferences, competition, and market trends.
        </p>
        <p>
        - <strong>Top Cuisines:</strong> The most popular cuisines identified are <strong>[Cuisine 1]</strong>, <strong>[Cuisine 2]</strong>, and <strong>[Cuisine 3]</strong>, with high customer ratings and demand.
        </p>
        <p>
        - <strong>Dining Preferences:</strong> Customers show a strong preference for <strong>[Dining Type]</strong> dining experiences, indicating a trend towards <strong>[Specific Trend]</strong>.
        </p>
        <p>
        - <strong>Best Selling Items:</strong> The top-selling dishes are <strong>[Dish 1]</strong>, <strong>[Dish 2]</strong>, and <strong>[Dish 3]</strong>, known for their popularity and high sales volume.
        </p>
        <p>
        - <strong>Optimal Pricing:</strong> The best price range for attracting customers is between <strong>[Price Range]</strong>, balancing affordability and profitability.
        </p>
        <p>
        - <strong>Competitor Landscape:</strong> The analysis of competitors highlighted key players in the market and areas where new entrants can gain a competitive edge.
        </p>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h2>Conclusion</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        This project provides a comprehensive analysis for aspiring restaurant owners in India. By understanding city preferences, popular cuisines, dining trends, best-selling items, and pricing strategies, one can make informed decisions about entering the restaurant industry. The insights gained from this analysis can serve as a valuable guide for opening and managing a successful restaurant.
        </p>
        <p>
        For further details or questions regarding this analysis, please feel free to contact me.
        </p>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h2>Contact Information</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p>
        - <strong>Email:</strong> [Your Email Address]
        </p>
        <p>
        - <strong>LinkedIn:</strong> [Your LinkedIn Profile]
        </p>
        <p>
        - <strong>Phone:</strong> [Your Phone Number]
        </p>
        """, unsafe_allow_html=True
    )
