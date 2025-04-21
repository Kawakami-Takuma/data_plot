import streamlit as st
import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sns

option = ["ヒストグラム", "散布図", "箱ひげ図"]

def main():
    uploded_file = st.file_uploader("csvファイルをアップロードしてください", type = "csv")
    if uploded_file is not None:
        df = pd.read_csv(uploded_file)
        st.write(df)
        
        
        graph = st.selectbox("プロットするグラフを選んでください", options = option)
        if graph == option[0]: # ヒストグラム
            plot_hist(df)

def plot_hist(df): # とりあえず１つだけ
    # ToDo 複数選択可能にしたい
    data = st.selectbox("データを選択してください", options = df.columns)
    plot_button = st.button("実行")
    if plot_button is True:
        st.write(pt.hist(data, bins=20)) # ヒストグラムプロットできず




if __name__ == "__main__":
    main()
