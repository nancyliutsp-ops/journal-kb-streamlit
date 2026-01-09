import streamlit as st
import pandas as pd

st.set_page_config(page_title="期刊知识库", layout="wide")

st.title("📚 期刊知识库（Streamlit）")

# ===== 1. 读取后台 Excel =====
@st.cache_data
def load_data():
    return pd.read_excel("data/journals.xlsx")

df = load_data()

st.success(f"已加载 {len(df)} 条期刊数据")

# ===== 2. 筛选 =====
with st.sidebar:
    st.header("筛选条件")

    if "REGION" in df.columns:
        region = st.multiselect("地区", sorted(df["REGION"].dropna().unique()))
    else:
        region = []

    if "PUBLISHER" in df.columns:
        publisher = st.multiselect("出版商", sorted(df["PUBLISHER"].dropna().unique()))
    else:
        publisher = []

    if "Category" in df.columns:
        subject = st.multiselect("学科", sorted(df["Category"].dropna().unique()))
    else:
        subject = []

df_show = df.copy()

if region:
    df_show = df_show[df_show["REGION"].isin(region)]
if publisher:
    df_show = df_show[df_show["PUBLISHER"].isin(publisher)]
if subject:
    df_show = df_show[df_show["Category"].isin(subject)]

# ===== 3. 展示表格 =====
st.dataframe(df_show, use_container_width=True)

# ===== 4. 统计 =====
st.subheader("📊 统计")

c1, c2, c3 = st.columns(3)

with c1:
    if "REGION" in df_show.columns:
        st.write("按地区")
        st.bar_chart(df_show["REGION"].value_counts())

with c2:
    if "PUBLISHER" in df_show.columns:
        st.write("按出版商")
        st.bar_chart(df_show["PUBLISHER"].value_counts().head(10))

with c3:
    if "Category" in df_show.columns:
        st.write("按学科")
        st.bar_chart(df_show["Category"].value_counts().head(10))
