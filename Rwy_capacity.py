import streamlit as st
import pandas as pd

def load_aeronef():
    df = pd.read_csv("aeronef.csv")
    return df["Type"].tolist()

def main():
    st.title("ENTREE")
    st.sidebar.title("Paramètres")

    st.sidebar.header("Piste")
    plong = st.sidebar.selectbox("Longueur (m)", list(range(500, 5001)), index=2500)
    plarg = st.sidebar.selectbox("Largeur (m)", list(range(20, 101)), index=25)
    plapp = st.sidebar.slider("LApp (NM)", 2.0, 10.0, 4.8, 0.1)
    qfu = st.sidebar.selectbox("QFU", list(range(37)))
    nbexit = st.sidebar.selectbox("NbExit", list(range(1, 21)))

    st.sidebar.header("Aéronef")
    aeronef_df = load_aeronef()
    list_aeronef = st.sidebar.selectbox("Type", aeronef_df, 0)
    melange = st.sidebar.slider("Proportion (%)", 0, 100, 0)

    st.sidebar.header("LOI")
    loi = st.sidebar.selectbox("LOI", ["Normal", "Uniforme", "KDE", "Autre"])

    st.sidebar.header("Simulation")
    simul_button = st.sidebar.button("Lancer la Simulation", key="simulation_button")

    if simul_button:
        st.write("Simulation en cours...")

    st.write(f"Longueur : {plong} m")
    st.write(f"Largeur : {plarg} m")
    st.write(f"LApp : {plapp} NM")
    st.write(f"QFU : {qfu}")
    st.write(f"NbExit : {nbexit}")

    st.write(f"Type : {list_aeronef}")
    st.write(f"Proportion : {melange}%")

    st.write(f"LOI : {loi}")

    if melange == 0:
        st.warning("Veuillez choisir un aéronef")
    elif melange == 100:
        st.success("Trafic constitué")
    else:
        remaining_proportion = 100 - melange
        st.warning(f"Choisir un autre : proportion restante : {remaining_proportion}%")

if __name__ == "__main__":
    main()
