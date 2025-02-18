import pandas as pd
from prophet import Prophet

def predict_sales(data):
    df = pd.DataFrame(data)
    df.rename(columns={"date": "ds", "sales": "y"}, inplace=True)

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    return forecast[["ds", "yhat"]].tail(30).to_dict(orient="records")
