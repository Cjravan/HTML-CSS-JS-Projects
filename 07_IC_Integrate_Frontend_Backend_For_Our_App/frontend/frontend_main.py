# # ==========
# # 9. Implement (or shift) plotting operations in the backend (as a small exercise)
# # ==========

# import streamlit as st
# import pandas as pd
# import plotly.express as px

# import requests

# st. set_page_config(layout="wide")

# # Added new: Cut pasted from inside display_plots() functions
# def display_data_summary(df):

#     st.write(df.describe())
#     tempDf = df.select_dtypes(include=["object"])
#     categVars = st.expander("Categorical Variables")
#     for col in tempDf.columns:
#         categVars.write(col)
#         categVars.write(tempDf[col].unique())
    
#     return None

# # Modified to match the new logic
# def display_plots(df1, df2):

#     # Plot pie chart
#     # groupByDf1 = df.groupby(["House_Type"])["Sale_Price"].mean() # To be computed at the backend
#     fig = px.pie(df1, values = "Sale_Price", names = df1["House_Type"])
#     st.plotly_chart(fig)

#     # Plot bar chart
#     # groupByDf2 = df.groupby(["Property_Shape"])["Sale_Price"].mean() # To be computed at the backend
#     fig2 = px.bar(df2, x = df2["Property_Shape"], y = "Sale_Price")
#     st.plotly_chart(fig2)

#     return None

# def impute_missing_values(df):
#     cols = list(df.columns)

#     for col in cols:
#         if df[col].dtype == "object":
#             df[col].fillna(df[col].mode()[0], inplace = True)
#         else:
#             df[col].fillna(df[col].median(), inplace = True)
#     return df

# def prediction_data():

#     Road_Type = st.selectbox("Road_Type", ["Paved", "Gravel"])
#     Property_Shape = st.selectbox("Property_Shape", ["Reg", "IR1", "IR2", "IR3"])	
#     House_Type = st.selectbox("House_Type", ["1Fam", "2fmCon", "Duplex", "TwnhsE", "Twnhs"])	
#     House_Condition	= st.slider("House_Condition", 1, 9, 5, 1) # 5 is the median, so lets keep that as the default when its rendered on UI
#     Construction_Year = st.slider("Construction_Year", 1872, 2010, 1973, 5)
#     Remodel_Year = st.selectbox("Remodel_Year", [year for year in range(1950, 2011, 1)])
#     BsmtFinSF1	= st.number_input("BsmtFinSF1 (0 to 5700)", 0.0, 5700.0)
#     Total_Basement_Area	= st.number_input("Total_Basement_Area (0 to 5700)", 0.0, 6100.0)
#     Air_Conditioning = st.radio("Air_Conditioning", ["Y", "N"])
#     First_Floor_Area = st.number_input("First_Floor_Area (330 to 4700)", 330.0, 4700.0)	
#     Second_Floor_Area = st.number_input("Second_Floor_Area (330 to 4700)", 330.0, 4700.0)	
#     LowQualFinSF = st.number_input("LowQualFinSF (0 to 575)", 0.0, 575.0)	
#     Underground_Full_Bathroom = st.slider("Underground_Full_Bathroom", 0, 3, 2, 1)	
#     Full_Bathroom_Above_Grade = st.slider("Full_Bathroom_Above_Grade", 0, 3, 2, 1)		
#     Bedroom_Above_Grade = st.slider("Bedroom_Above_Grade", 0, 8, 2, 1)		
#     Kitchen_Quality	= st.selectbox("Kitchen_Quality", ["Gd", "TA", "Ex", "Fa"])
#     Rooms_Above_Grade = st.slider("Rooms_Above_Grade", 0, 3, 2, 1)	
#     Fireplaces = st.slider("Fireplaces", 0, 3, 2, 1)		
#     Garage = st.selectbox("Garage", ["Attchd", "Detchd", "BuiltIn", "CarPort", "Basment", "2TFes", "2Types"])
#     Garage_Built_Year = st.selectbox("Garage_Built_Year", [year for year in range(1900, 2011, 1)])	
#     Garage_Area	= st.number_input("Garage_Area (0 to 1150)", 0.0, 1150.0)
#     Pool_Area = st.number_input("Pool_Area (0 to 750)", 0.0, 750.0)
#     Miscellaneous_Value	= st.number_input("Miscellaneous_Value (0 to 15000)", 0.0, 15000.0)
#     Year_Sold = st.selectbox("Year_Sold", [year for year in range(2006, 2011, 1)])

#     predictionData = \
#     {
#         "Road_Type": Road_Type,
#         "Property_Shape": Property_Shape,
#         "House_Type": House_Type,
#         "House_Condition": House_Condition,
#         "Construction_Year": Construction_Year,
#         "Remodel_Year": Remodel_Year,
#         "BsmtFinSF1": BsmtFinSF1,
#         "Total_Basement_Area": Total_Basement_Area,
#         "Air_Conditioning": Air_Conditioning,
#         "First_Floor_Area": First_Floor_Area,
#         "Second_Floor_Area": Second_Floor_Area,
#         "LowQualFinSF": LowQualFinSF,
#         "Underground_Full_Bathroom": Underground_Full_Bathroom,
#         "Full_Bathroom_Above_Grade": Full_Bathroom_Above_Grade,
#         "Bedroom_Above_Grade": Bedroom_Above_Grade,
#         "Kitchen_Quality": Kitchen_Quality,
#         "Rooms_Above_Grade": Rooms_Above_Grade,
#         "Fireplaces": Fireplaces,
#         "Garage": Garage,
#         "Garage_Built_Year": Garage_Built_Year,
#         "Garage_Area": Garage_Area,
#         "Pool_Area": Pool_Area,
#         "Miscellaneous_Value": Miscellaneous_Value,
#         "Year_Sold": Year_Sold
#     }

#     return predictionData

# def read_data_and_page_setup():

#     dataFile = st.file_uploader("Upload CSV", type = ["csv"])
#     fileReadFlag = False
#     df = None

#     if dataFile is not None:
#         fileReadFlag = True
#         df = pd.read_csv(dataFile)
#         df = impute_missing_values(df)

#     sidebarMenu = ["Home", "Prediction"] # Prediction will be coded later
#     userChoice = st.sidebar.radio("Welcome to our App :)", sidebarMenu)

#     return df, userChoice, fileReadFlag

# def main():
    
#     df, userChoice, fileReadFlag = read_data_and_page_setup()

#     baseURL = "http://127.0.0.1:8000"

#     if fileReadFlag == True:

#         if userChoice == "Home":
#             # df.dropna(inplace = True)
#             df = impute_missing_values(df)
#             display_data_summary(df)
            
#             ### Send plot operations to backend (as an exercise) and get a groupby df in return from backend
#             dfInJson = pd.DataFrame.to_dict(df)
#             # st.write(dfInJson)
            
#             response = requests.post(baseURL + "/plot", json = dfInJson)
#             st.write(response.json())
#             # df = pd.DataFrame(response.json())
#             # st.write(df)
#             df1 = pd.DataFrame(response.json()["first"])
#             st.write(df1)
#             df2 = pd.DataFrame(response.json()["second"])
#             st.write(df2)
#             ###
            
#             display_plots(df1, df2)


#         elif userChoice == "Prediction":
#             predictionData = prediction_data()
        
    
#     st.write("You have reached the end of the page :)")

# # To execute a streamlit application, you need to type in the command prompt: streamlit run main.py
# if __name__ == '__main__':
#     main()


# # ==========
# # 10. Integrate prediction
# # ==========

# import streamlit as st
# import pandas as pd
# import plotly.express as px

# import requests

# st. set_page_config(layout="wide")

# # Added new: Cut pasted from inside display_plots() functions
# def display_data_summary(df):

#     st.write(df.describe())
#     tempDf = df.select_dtypes(include=["object"])
#     categVars = st.expander("Categorical Variables")
#     for col in tempDf.columns:
#         categVars.write(col)
#         categVars.write(tempDf[col].unique())
    
#     return None

# # Modified to match the new logic
# def display_plots(df1, df2):

#     # Plot pie chart
#     # groupByDf1 = df.groupby(["House_Type"])["Sale_Price"].mean() # To be computed at the backend
#     fig = px.pie(df1, values = "Sale_Price", names = df1["House_Type"])
#     st.plotly_chart(fig)

#     # Plot bar chart
#     # groupByDf2 = df.groupby(["Property_Shape"])["Sale_Price"].mean() # To be computed at the backend
#     fig2 = px.bar(df2, x = df2["Property_Shape"], y = "Sale_Price")
#     st.plotly_chart(fig2)

#     return None

# def impute_missing_values(df):
#     cols = list(df.columns)

#     for col in cols:
#         if df[col].dtype == "object":
#             df[col].fillna(df[col].mode()[0], inplace = True)
#         else:
#             df[col].fillna(df[col].median(), inplace = True)
#     return df

# def prediction_data():

#     Road_Type = st.selectbox("Road_Type", ["Paved", "Gravel"])
#     Property_Shape = st.selectbox("Property_Shape", ["Reg", "IR1", "IR2", "IR3"])	
#     House_Type = st.selectbox("House_Type", ["1Fam", "2fmCon", "Duplex", "TwnhsE", "Twnhs"])	
#     House_Condition	= st.slider("House_Condition", 1, 9, 5, 1) # 5 is the median, so lets keep that as the default when its rendered on UI
#     Construction_Year = st.slider("Construction_Year", 1872, 2010, 1973, 5)
#     Remodel_Year = st.selectbox("Remodel_Year", [year for year in range(1950, 2011, 1)])
#     BsmtFinSF1	= st.number_input("BsmtFinSF1 (0 to 5700)", 0.0, 5700.0)
#     Total_Basement_Area	= st.number_input("Total_Basement_Area (0 to 5700)", 0.0, 6100.0)
#     Air_Conditioning = st.radio("Air_Conditioning", ["Y", "N"])
#     First_Floor_Area = st.number_input("First_Floor_Area (330 to 4700)", 330.0, 4700.0)	
#     Second_Floor_Area = st.number_input("Second_Floor_Area (330 to 4700)", 330.0, 4700.0)	
#     LowQualFinSF = st.number_input("LowQualFinSF (0 to 575)", 0.0, 575.0)	
#     Underground_Full_Bathroom = st.slider("Underground_Full_Bathroom", 0, 3, 2, 1)	
#     Full_Bathroom_Above_Grade = st.slider("Full_Bathroom_Above_Grade", 0, 3, 2, 1)		
#     Bedroom_Above_Grade = st.slider("Bedroom_Above_Grade", 0, 8, 2, 1)		
#     Kitchen_Quality	= st.selectbox("Kitchen_Quality", ["Gd", "TA", "Ex", "Fa"])
#     Rooms_Above_Grade = st.slider("Rooms_Above_Grade", 0, 3, 2, 1)	
#     Fireplaces = st.slider("Fireplaces", 0, 3, 2, 1)		
#     Garage = st.selectbox("Garage", ["Attchd", "Detchd", "BuiltIn", "CarPort", "Basment", "2TFes", "2Types"])
#     Garage_Built_Year = st.selectbox("Garage_Built_Year", [year for year in range(1900, 2011, 1)])	
#     Garage_Area	= st.number_input("Garage_Area (0 to 1150)", 0.0, 1150.0)
#     Pool_Area = st.number_input("Pool_Area (0 to 750)", 0.0, 750.0)
#     Miscellaneous_Value	= st.number_input("Miscellaneous_Value (0 to 15000)", 0.0, 15000.0)
#     Year_Sold = st.selectbox("Year_Sold", [year for year in range(2006, 2011, 1)])

#     # # if garage area increases by x units, then ffa should decrease 0.8x
#     # First_Floor_Area = First_Floor_Area - 0.8*First_Floor_Area

#     predictionData = \
#     {
#         "Road_Type": Road_Type,
#         "Property_Shape": Property_Shape,
#         "House_Type": House_Type,
#         "House_Condition": House_Condition,
#         "Construction_Year": Construction_Year,
#         "Remodel_Year": Remodel_Year,
#         "BsmtFinSF1": BsmtFinSF1,
#         "Total_Basement_Area": Total_Basement_Area,
#         "Air_Conditioning": Air_Conditioning,
#         "First_Floor_Area": First_Floor_Area,
#         "Second_Floor_Area": Second_Floor_Area,
#         "LowQualFinSF": LowQualFinSF,
#         "Underground_Full_Bathroom": Underground_Full_Bathroom,
#         "Full_Bathroom_Above_Grade": Full_Bathroom_Above_Grade,
#         "Bedroom_Above_Grade": Bedroom_Above_Grade,
#         "Kitchen_Quality": Kitchen_Quality,
#         "Rooms_Above_Grade": Rooms_Above_Grade,
#         "Fireplaces": Fireplaces,
#         "Garage": Garage,
#         "Garage_Built_Year": Garage_Built_Year,
#         "Garage_Area": Garage_Area,
#         "Pool_Area": Pool_Area,
#         "Miscellaneous_Value": Miscellaneous_Value,
#         "Year_Sold": Year_Sold
#     }

#     return predictionData

# def read_data_and_page_setup():

#     dataFile = st.file_uploader("Upload CSV", type = ["csv"])
#     fileReadFlag = False
#     df = None

#     if dataFile is not None:
#         fileReadFlag = True
#         df = pd.read_csv(dataFile)
#         df = impute_missing_values(df)

#     sidebarMenu = ["Home", "Prediction"] # Prediction will be coded later
#     userChoice = st.sidebar.radio("Welcome to our App :)", sidebarMenu)

#     return df, userChoice, fileReadFlag

# def main():
    
#     df, userChoice, fileReadFlag = read_data_and_page_setup()

#     baseURL = "http://127.0.0.1:8000"

#     if fileReadFlag == True:

#         if userChoice == "Home":
#             # df.dropna(inplace = True)
#             df = impute_missing_values(df)
#             display_data_summary(df)
            
#             ### Send plot operations to backend (as an exercise) and get a groupby df in return from backend
#             dfInJson = pd.DataFrame.to_dict(df)
#             # st.write(dfInJson)
            
#             response = requests.post(baseURL + "/plot", json = dfInJson)
#             st.write(response.json())
#             # df = pd.DataFrame(response.json())
#             # st.write(df)
#             df1 = pd.DataFrame(response.json()["first"])
#             st.write(df1)
#             df2 = pd.DataFrame(response.json()["second"])
#             st.write(df2)
#             ###
            
#             display_plots(df1, df2)


#         elif userChoice == "Prediction":
#             predictionJson = prediction_data()

#             # st.write(predictionJson)
#             # tempDf = pd.DataFrame(predictionJson, index=[0])
#             # st.write(tempDf)

#             if st.button("Predict"): # You can read it as "If Predict button is clicked on the UI, execute the below block"
#                 response = requests.post(baseURL + "/prediction", json = predictionJson)
#                 # st.write(response.json())
#                 testPredictionValue = response.json()["testPrediction"]["0"]
#                 st.success("The Predicted Price of the House is: $" + str(testPredictionValue))
        
    
#     st.write("You have reached the end of the page :)")

# # To execute a streamlit application, you need to type in the command prompt: streamlit run main.py
# if __name__ == '__main__':
#     main()

# ==========
# 11. Lets refine the UI a little bit
# 1. We do NOT need CSV uploader for "Prediction" page. Lets remove it and keep it only for "Home" page.
# 2. On "Prediction" page, lets spread the fields horizontally (using st.columns()), so that the user does NOT have to scroll so much vertically. 24 columns in total. 
# 3. Lets remove all the "input/ ouput JSONs" displayed on the UI. Remove st.write() from most places, except where necessary (like data summarization)
# 4. On "Home" page, lets put both the plots side by side 
# ==========

import streamlit as st
import pandas as pd
import plotly.express as px

# Added new
import requests

st.set_page_config(layout="wide")

def display_data_summary(df):

    st.write(df.describe())
    tempDf = df.select_dtypes(include=["object"])
    categVars = st.expander("Categorical Variables")
    for col in tempDf.columns:
        categVars.write(col)
        categVars.write(tempDf[col].unique())
    
    return None
            
# Modified to match the new logic
def display_plots(df1, df2):

    col1, col2 = st.columns(2)

    with col1:
        # Plot pie chart
        # groupByDf1 = df.groupby(["House_Type"])["Sale_Price"].mean()
        fig = px.pie(df1, values = "Sale_Price", names = df1["House_Type"])
        st.plotly_chart(fig)

    with col2:
        # Plot bar chart
        # groupByDf2 = df.groupby(["Property_Shape"])["Sale_Price"].mean()
        fig2 = px.bar(df2, x = df2["Property_Shape"], y = "Sale_Price")
        st.plotly_chart(fig2)

    return None

def impute_missing_values(df):
    cols = list(df.columns)

    for col in cols:
        if df[col].dtype == "object":
            df[col].fillna(df[col].mode()[0], inplace = True)
        else:
            df[col].fillna(df[col].median(), inplace = True)
    return df

def prediction_data():

    col1, col2, col3 = st.columns(3)

    with col1:

        # First 8 cols here
        Road_Type = st.selectbox("Road_Type", ["Paved", "Gravel"])
        Property_Shape = st.selectbox("Property_Shape", ["Reg", "IR1", "IR2", "IR3"])	
        House_Type = st.selectbox("House_Type", ["1Fam", "2fmCon", "Duplex", "TwnhsE", "Twnhs"])	
        House_Condition	= st.slider("House_Condition", 1, 9, 5, 1) # 5 is the median, so lets keep that as the default when its rendered on UI
        Construction_Year = st.slider("Construction_Year", 1872, 2010, 1973, 5)
        Remodel_Year = st.selectbox("Remodel_Year", [year for year in range(1950, 2011, 1)])
        BsmtFinSF1	= st.number_input("BsmtFinSF1 (0 to 5700)", 0.0, 5700.0)
        Total_Basement_Area	= st.number_input("Total_Basement_Area (0 to 5700)", 0.0, 6100.0)
    
    with col2:
        Air_Conditioning = st.radio("Air_Conditioning", ["Y", "N"])
        First_Floor_Area = st.number_input("First_Floor_Area (330 to 4700)", 330.0, 4700.0)	
        Second_Floor_Area = st.number_input("Second_Floor_Area (330 to 4700)", 330.0, 4700.0)	
        LowQualFinSF = st.number_input("LowQualFinSF (0 to 575)", 0.0, 575.0)	
        Underground_Full_Bathroom = st.slider("Underground_Full_Bathroom", 0, 3, 2, 1)	
        Full_Bathroom_Above_Grade = st.slider("Full_Bathroom_Above_Grade", 0, 3, 2, 1)		
        Bedroom_Above_Grade = st.slider("Bedroom_Above_Grade", 0, 8, 2, 1)		
        Kitchen_Quality	= st.selectbox("Kitchen_Quality", ["Gd", "TA", "Ex", "Fa"])
    
    with col3:
        Rooms_Above_Grade = st.slider("Rooms_Above_Grade", 0, 3, 2, 1)	
        Fireplaces = st.slider("Fireplaces", 0, 3, 2, 1)		
        Garage = st.selectbox("Garage", ["Attchd", "Detchd", "BuiltIn", "CarPort", "Basment", "2TFes", "2Types"])
        Garage_Built_Year = st.selectbox("Garage_Built_Year", [year for year in range(1900, 2011, 1)])	
        Garage_Area	= st.number_input("Garage_Area (0 to 1150)", 0.0, 1150.0)
        Pool_Area = st.number_input("Pool_Area (0 to 750)", 0.0, 750.0)
        Miscellaneous_Value	= st.number_input("Miscellaneous_Value (0 to 15000)", 0.0, 15000.0)
        Year_Sold = st.selectbox("Year_Sold", [year for year in range(2006, 2011, 1)])

    predictionJson = \
    {
        "Road_Type": Road_Type,
        "Property_Shape": Property_Shape,
        "House_Type": House_Type,
        "House_Condition": House_Condition,
        "Construction_Year": Construction_Year,
        "Remodel_Year": Remodel_Year,
        "BsmtFinSF1": BsmtFinSF1,
        "Total_Basement_Area": Total_Basement_Area,
        "Air_Conditioning": Air_Conditioning,
        "First_Floor_Area": First_Floor_Area,
        "Second_Floor_Area": Second_Floor_Area,
        "LowQualFinSF": LowQualFinSF,
        "Underground_Full_Bathroom": Underground_Full_Bathroom,
        "Full_Bathroom_Above_Grade": Full_Bathroom_Above_Grade,
        "Bedroom_Above_Grade": Bedroom_Above_Grade,
        "Kitchen_Quality": Kitchen_Quality,
        "Rooms_Above_Grade": Rooms_Above_Grade,
        "Fireplaces": Fireplaces,
        "Garage": Garage,
        "Garage_Built_Year": Garage_Built_Year,
        "Garage_Area": Garage_Area,
        "Pool_Area": Pool_Area,
        "Miscellaneous_Value": Miscellaneous_Value,
        "Year_Sold": Year_Sold
    }

    return predictionJson

def read_data():

    dataFile = st.file_uploader("Upload CSV", type = ["csv"])
    # fileReadFlag = False
    df = None

    if dataFile is not None:
        # fileReadFlag = True
        df = pd.read_csv(dataFile)
        df = impute_missing_values(df)

    return df, dataFile


def page_setup():

    sidebarMenu = ["Home", "Prediction"] # Prediction will be coded later
    userChoice = st.sidebar.radio("Welcome to our App :)", sidebarMenu)

    return userChoice

def main():

    userChoice = page_setup()    

    baseURL = "http://127.0.0.1:8000"

    if userChoice == "Home":

        df, dataFile = read_data()

        if dataFile is not None:

            display_data_summary(df)

            dfInJson = pd.DataFrame.to_dict(df)
            # st.write(dfInJson)
            
            response = requests.post(baseURL + "/plot", json = dfInJson)
            # st.write(response.json())
            # df = pd.DataFrame(response.json())
            # st.write(df)
            df1 = pd.DataFrame(response.json()["first"])
            # st.write(df1)
            df2 = pd.DataFrame(response.json()["second"])
            # st.write(df2)
            display_plots(df1, df2)

    elif userChoice == "Prediction":
        predictionJson = prediction_data()
        # # st.write(predictionJson)
        # tempDf = pd.DataFrame(predictionJson, index=[0])
        # # st.write(tempDf)

        if st.button("Predict"):
            response = requests.post(baseURL + "/prediction", json = predictionJson)
            # st.write(response.json())
            testPredictionValue = response.json()["testPrediction"]["0"]
            st.success("The Predicted Price of the House is: $" + str(testPredictionValue))
    

st.write("You have reached the end of the page :)")

# To execute a streamlit application, you need to type in the command prompt: streamlit run main.py
if __name__ == '__main__':
    main()