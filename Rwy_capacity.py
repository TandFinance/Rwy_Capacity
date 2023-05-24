import streamlit as st

def main():
    st.title("ENTREE")
    st.sidebar.title("Paramètres")

    st.sidebar.header("Piste")
    plong = st.sidebar.selectbox("Longueur", list(range(500, 5001)))
    plarg = st.sidebar.selectbox("Largeur", list(range(20, 101)))
    plapp = st.sidebar.text_input("LApp", "4.8")
    qfu = st.sidebar.selectbox("QFU", list(range(37)))
    nbexit = st.sidebar.selectbox("NbExit", list(range(1, 21)))

    st.sidebar.header("Aéronef")
    list_aeronef = st.sidebar.selectbox("Type", ["EA33/M"])
    melange = st.sidebar.slider("Proportion", 0, 100)

    st.sidebar.header("LOI")
    loi = st.sidebar.selectbox("LOI", ["Normal", "Uniforme", "KDE", "Autre"])

    st.sidebar.header("Simulation")
    simul_button = st.sidebar.button("Lancer la Simulation")

    if simul_button:
        st.write("Simulation en cours...")

    st.write(f"Longueur : {plong}")
    st.write(f"Largeur : {plarg}")
    st.write(f"LApp : {plapp}")
    st.write(f"QFU : {qfu}")
    st.write(f"NbExit : {nbexit}")

    st.write(f"Type : {list_aeronef}")
    st.write(f"Proportion : {melange}%")

    st.write(f"LOI : {loi}")

if __name__ == "__main__":
    main()
