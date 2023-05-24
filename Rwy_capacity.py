import streamlit as st
import pandas as pd
selected_aeronefs = []
def load_aeronef():
    df = pd.read_csv("aeronef.csv")
    return df["Type"].tolist()

def main():
    aeronef_df = load_aeronef()
    

    st.title("AÉRONEF")
    st.markdown("<font color='red'><b>Veuillez choisir un aéronef</b></font>", unsafe_allow_html=True)

    aeroname = st.selectbox("Type d'aéronef", aeronef_df)
    proportions = st.slider("Proportion (%)", 0, 100, 0)

    valid_button = st.button("Valider")
    p=sum([proportion for _, proportion in selected_aeronefs])
    if valid_button and proportions > 0:
        selected_aeronefs.append((aeroname, proportions))
        if p <100:
            st.success("Ajouter un autre aéronef")
        else :
             st.success("Trafic constitué")
    st.write("Tableau des aéronefs choisis :")
    aeronef_table = pd.DataFrame(selected_aeronefs, columns=["Aéronef", "Proportion"])
    st.table(aeronef_table)
    print( selected_aeronefs)
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

    st.write(f"Longueur : {plong} m")
    st.write(f"Largeur : {plarg} m")
    st.write(f"LApp : {plapp} NM")
    st.write(f"QFU : {qfu}")
    st.write(f"NbExit : {nbexit}")
    st.write(f"LOI : {loi}")

if __name__ == "__main__":
    main()
