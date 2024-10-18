import streamlit as st

# Set page title
st.set_page_config(page_title="House Price Prediction Project", page_icon=":House:")

# Main page title with animation
st.markdown(
    """
    <style>
        .title {
            animation: fadeIn 2s;
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
    </style>
    <h1 class="title">House Price Prediction using ML</h1>
    """,
    unsafe_allow_html=True
)

# Project details
st.markdown(
    """
    <style>
        .project-details {
            animation: slideInLeft 2s;
        }
        @keyframes slideInLeft {
            from {
                transform: translateX(-50px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
    </style>
    <div class="project-details">
        <h2>Description of the Project:</h2>
        <ul>
            <li><strong>Language:</strong> The project was implemented using Python, a popular programming language for machine learning and data analysis tasks.</li>
            <li><strong>Libraries:</strong>
                <ul>
                    <li>Pandas: For data manipulation and preprocessing.</li>
                    <li>NumPy: For numerical computations.</li>
                    <li>Scikit-learn: For implementing machine learning algorithms.</li>
                    <li>Matplotlib and Seaborn: For data visualization.</li>
                    <li>Streamlit: For building a web application (if applicable).</li>
                </ul>
            </li>
            <li><strong>Dataset:</strong> The project utilized house price datasets from Mumbai and Bangalore.</li>
            <li><strong>Pickle Files:</strong> Pickle files were used to store trained machine learning models for later use.</li>
        </ul>
        <h2>Working:</h2>
        <ol>
            <li><strong>Data Collection:</strong> The project team collected housing dataset containing various features such as area, number of bedrooms, location, etc.</li>
            <li><strong>Data Preprocessing:</strong> The collected data was cleaned, missing values were handled, and features were preprocessed for further analysis.</li>
            <li><strong>Feature Engineering:</strong> Additional features were created or modified to improve the performance of the machine learning models.</li>
            <li><strong>Model Selection:</strong> Different regression algorithms such as Linear Regression, Decision Trees, Random Forest, etc., were explored and evaluated to select the best-performing model.</li>
            <li><strong>Model Training:</strong> The selected model was trained on the preprocessed data to learn the patterns and relationships between the features and the target variable (house prices).</li>
            <li><strong>Model Evaluation:</strong> The trained model was evaluated using appropriate metrics such as Mean Absolute Error, Mean Squared Error, etc., to assess its performance.</li>
            <li><strong>Deployment (if applicable):</strong> The final trained model was deployed, either as a standalone application or a web service using Flask, allowing users to input new data and get predictions on house prices.</li>
        </ol>
        <p>Overall, the project demonstrated the application of machine learning techniques in predicting house prices, which can be useful for real estate agents, homeowners, and investors in making informed decisions.</p>
    </div>
    """,
    unsafe_allow_html=True
)
