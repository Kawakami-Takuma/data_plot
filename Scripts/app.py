import streamlit as st
import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sns

def main():
    uploded_file = st.file_uploader("csvファイルをアップロードしてください", type = "csv")
    if uploded_file is not None:
        df = pd.read_csv(uploded_file)
        st.write(df)

if __name__ == "__main__":
    main()
