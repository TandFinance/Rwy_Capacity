import streamlit as st
import pandas as pd

def load_aeronef():
    df = pd.read_csv("aeronef.csv")
    return df["Type"].tolist()

def main():
    aeronef_df = load_aeronef()

    st.title("AÉRONEF")
    st.header("Choix de l'aéronef")
    list_aeronef = st.selectbox("Type", aeronef_df, 0)

    proportion = 0
    valid_button = st.button("Valider", key="valid_button")
    if valid_button:
        proportion = st.slider("Proportion (%)", 0, 100 - proportion, 0)
        st.success("Trafic constitué")

    st.sidebar.title("Paramètres")

    st.sidebar.header("Piste")
    plong = st.sidebar.selectbox("Longueur (m)", list(range(500, 5001)), index=2500)
    plarg = st.sidebar.selectbox("Largeur (m)", list(range(20, 101)), index=25)
    plapp = st.sidebar.slider("LApp (NM)", 2.0, 10.0, 4.8, 0.1)
    qfu = st.sidebar.selectbox("QFU", list(range(37)))
    nbexit = st.sidebar.selectbox("NbExit", list(range(1, 21)))

    st.sidebar.header("LOI")
    loi = st.sidebar.selectbox("LOI", ["Normal", "Uniforme", "KDE", "Autre"])

    st.sidebar.header("Simulation")
    simul_button = st.sidebar.button("Lancer la Simulation", key="simulation_button")

    if simul_button:
        st.write("Simulation en cours...")

    aeronef_table = pd.DataFrame({
        "Aéronef": [list_aeronef],
        "Proportion": [proportion]
    })

    st.write("**Veuillez choisir un aéronef**", unsafe_allow_html=True)

    if valid_button:
        st.write("Tableau des aéronefs choisis :")
        st.table(aeronef_table)

    st.write(f"Longueur : {plong} m")
    st.write(f"Largeur : {plarg} m")
    st.write(f"LApp : {plapp} NM")
    st.write(f"QFU : {qfu}")
    st.write(f"NbExit : {nbexit}")
    st.write(f"LOI : {loi}")

if __name__ == "__main__":
    main()
