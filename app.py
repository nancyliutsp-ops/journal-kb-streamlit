import os
import streamlit as st
import pandas as pd

st.set_page_config(page_title="期刊知识库", layout="wide")
st.title("📚 期刊知识库（Streamlit）")

PATH = "data/journals.xlsx"

st.write("### ✅ 启动自检")
st.write("当前工作目录：", os.getcwd())
st.write("文件是否存在：", os.path.exists(PATH))
if os.path.exists(PATH):
    st.write("文件大小（字节）：", os.path.getsize(PATH))
    st.write("data/ 目录文件：", os.listdir("data"))

st.divider()

@st.cache_data
def load_data():
    # 1) 强制指定引擎，避免 pandas 自动判断出错
    return pd.read_excel(PATH, engine="openpyxl")

try:
    df = load_data()
    st.success(f"已加载 {len(df)} 条期刊数据")
    st.dataframe(df, use_container_width=True)
except Exception as e:
    # 2) 把真实错误显示出来（你自己看，不是公开给别人也没问题；若担心可后续再关）
    st.error("读取 Excel 失败，下面是完整错误信息：")
    st.exception(e)

    st.info(
        "常见原因：\n"
        "1) 文件不是标准 .xlsx（比如 csv 改后缀、WPS 导出异常）\n"
        "2) Excel 被加密/有密码\n"
        "3) 文件损坏\n"
        "4) 依赖版本/引擎问题（openpyxl）"
    )
