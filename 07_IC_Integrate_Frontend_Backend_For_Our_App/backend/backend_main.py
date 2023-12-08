# # ==========
# # 9. Implement the backend for plots
# # ==========

# from fastapi import FastAPI
# import uvicorn
# import pandas as pd

# app = FastAPI() 

# @app.get("/") 
# async def root(): 
#     return {"message": "Hello World"} 

# @app.post("/plot")
# def process_data(data: dict):
#     df = pd.DataFrame.from_dict(data)
    
#     df1 = df.groupby(["House_Type"])["Sale_Price"].mean().reset_index()
#     json1 = pd.DataFrame.to_dict(df1)

#     df2 = df.groupby(["Property_Shape"])["Sale_Price"].mean().reset_index()
#     json2 = pd.DataFrame.to_dict(df2)

#     # df1.to_csv("df1.csv") # This is just for TESTING PURPOSE
#     # df2.to_csv("df2.csv") # This is just for TESTING PURPOSE
    
#     return {"first": json1, "second": json2}

# if __name__ == "__main__":
#     uvicorn.run("backend_main:app", host = "127.0.0.1", port = 8000, reload = True)


# ==========
# 10. Integrate prediction
# ==========

from fastapi import FastAPI
import uvicorn
import pandas as pd
import joblib
import numpy as np

app = FastAPI() 

@app.get("/") 
async def root(): 
    return {"message": "Hello World"} 

@app.post("/plot")
def process_data(data: dict):
    df = pd.DataFrame.from_dict(data)
    
    df1 = df.groupby(["House_Type"])["Sale_Price"].mean().reset_index()
    json1 = pd.DataFrame.to_dict(df1)

    df2 = df.groupby(["Property_Shape"])["Sale_Price"].mean().reset_index()
    json2 = pd.DataFrame.to_dict(df2)

    # df1.to_csv("df1.csv") # This is just for TESTING PURPOSE
    # df2.to_csv("df2.csv") # This is just for TESTING PURPOSE
    
    return {"first": json1, "second": json2}


def data_preprocessing(df, modelsDict):

    # print("=====================================data_preprocessing starts=====================================")

    df["Sale_Price"] = np.nan

    # df.to_csv("data_preprocessing.csv") # This is just for TESTING PURPOSE
    
    df[modelsDict["contVars"]] = pd.DataFrame(modelsDict["imputeContModel"].transform(df[modelsDict["contVars"]]), columns = modelsDict["contVars"])

    # print("=====================================data_preprocessing contVars=====================================")
    
    df[modelsDict["categVars"]] = pd.DataFrame(modelsDict["imputeCategModel"].transform(df[modelsDict["categVars"]]), columns = modelsDict["categVars"])
    
    df[modelsDict["labelEncCategVars"]].replace(modelsDict["kitchenQualityMapping"], inplace = True)
    df[modelsDict["labelEncCategVars"]] = pd.DataFrame(modelsDict["labelEncModel"].transform(df[modelsDict["labelEncCategVars"]]), columns = [modelsDict["labelEncCategVars"]])
    
    testOneHotEncDf = pd.DataFrame(modelsDict["oneHotEncModel"].transform(df[modelsDict["oneHotEncCategVars"]]).toarray(), 
                                   columns = list(modelsDict["oneHotEncModel"].get_feature_names_out()))
    df = pd.concat([df.drop(modelsDict["oneHotEncCategVars"], axis = 1), testOneHotEncDf], axis = 1)
    
    print(df.columns)
    
    df.drop(["Sale_Price"], axis = 1, inplace = True) # Need to drop "Sale_Price" as RF model (in the next step/ function) does NOT have this input column in the model
                                                                 
    return df


def load_models():

    # print("=====================================load_models start=====================================")

    modelsDict = {}
    
    modelsDict["contVars"] = joblib.load('../model/contVars.joblib')

    # print("=====================================load_models contVars=====================================")

    modelsDict["categVars"] = joblib.load('../model/categVars.joblib')
    modelsDict["labelEncCategVars"] = joblib.load('../model/labelEncCategVars.joblib')
    modelsDict["oneHotEncCategVars"] = joblib.load('../model/oneHotEncCategVars.joblib')
    modelsDict["imputeContModel"] = joblib.load('../model/imputeContModel.joblib')
    modelsDict["imputeCategModel"] = joblib.load('../model/imputeCategModel.joblib')
    modelsDict["kitchenQualityMapping"] = joblib.load('../model/kitchenQualityMapping.joblib')
    modelsDict["labelEncModel"] = joblib.load('../model/labelEncModel.joblib')
    modelsDict["oneHotEncModel"] = joblib.load('../model/oneHotEncModel.joblib')
    modelsDict["rfModel"] = joblib.load('../model/rfModel.joblib')

    # print("=====================================load_models end=====================================")

    # pd.DataFrame(modelsDict).to_csv("modelsDictDf.csv") # This is just for TESTING PURPOSE

    return modelsDict

def predict_house_price(df, rfModel):
   
    df["testPrediction"] = rfModel.predict(df)
    
    return df

@app.post("/prediction")
def process_data(data: dict):

    # df = pd.DataFrame.from_dict(data) # This will give an error as its a SINGLE/ SCALAR row
    df = pd.DataFrame(data, index=[0])
    # df.to_csv("predictionDf.csv") # This is just for TESTING PURPOSE 

    # print("=====================================load_model starts=====================================")

    # 1. Load all models
    modelsDict = load_models()

    # print("=====================================data_preprocessing starts=====================================")
    

    # 2. Pre-process the data coming from frontend using data_preprocessing
    df = data_preprocessing(df, modelsDict)

    # print("====================================predict_house_price starts======================================")

    # 3. Predict using predict_house_price
    predictedDf = predict_house_price(df, modelsDict["rfModel"])

    # 4. Return prediction to frontend
    predictionJson = pd.DataFrame.to_dict(predictedDf)

    # print("=====================================prediction ends=====================================")

    return predictionJson

if __name__ == "__main__":
    uvicorn.run("backend_main:app", host = "127.0.0.1", port = 8000, reload = True)
    