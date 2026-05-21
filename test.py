import streamlit as st
import pandas as pd
import numpy as np
print('my name is hadar')


# יצירת נתונים לדוגמה
np.random.seed(42)
df = pd.DataFrame({
    "קטגוריה": np.random.choice(["A", "B", "C"], 200),
    "ערך": np.random.randn(200)*10 + 50,
    "תאריך": pd.date_range("2023-01-01", periods=200)
})

st.title("דאשבורד אינטראקטיבי לדוגמה")
st.write("דאשבורד זה מדגים אינטראקטיביות פשוטה על גבי נתונים סינתטיים.")

# פילטר על קטגוריה
selected_cat = st.sidebar.multiselect(
    "בחר קטגוריה",
    options=df["קטגוריה"].unique(),
    default=df["קטגוריה"].unique()
)

# מסנן טווח תאריכים
start_date, end_date = st.sidebar.date_input(
    "בחר טווח תאריכים",
    value=[df["תאריך"].min(), df["תאריך"].max()],
    min_value=df["תאריך"].min(),
    max_value=df["תאריך"].max()
)

# סינון הדאטהפריים
filtered_df = df[
    df["קטגוריה"].isin(selected_cat) &
    (df["תאריך"] >= pd.to_datetime(start_date)) &
    (df["תאריך"] <= pd.to_datetime(end_date))
]

st.subheader("נתונים מסוננים")
st.dataframe(filtered_df)

# גרף ממוצע ערך פר קטגוריה
st.subheader("ממוצע ערך לפי קטגוריה")
avg_per_cat = filtered_df.groupby("קטגוריה")["ערך"].mean()
st.bar_chart(avg_per_cat)

# גרף ערך לאורך זמן
st.subheader("ערך לאורך זמן")
st.line_chart(filtered_df.set_index("תאריך")["ערך"])