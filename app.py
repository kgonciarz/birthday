import streamlit as st
import random
import time

st.set_page_config(page_title="Oficjalna Strona Legendy", page_icon="👑")

# Styl Real Madrid vibes
st.markdown("""
    <style>
    .big-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #111;
    }
    .center {
        text-align: center;
    }
    .boom {
        font-size: 35px;
        font-weight: bold;
        color: #6A0DAD;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">⚽ Oficjalna Strona Legendy ⚽</div>', unsafe_allow_html=True)
st.markdown('<div class="center">Sponsorowane przez rodzinę i Candy 🐶</div>', unsafe_allow_html=True)
st.markdown("---")

st.subheader("🧐 Pytanie weryfikacyjne")

answer = st.radio("Czy masz na imię Rafał?", ["Nie", "Tak"])

if answer == "Tak":
    st.markdown("---")
    
    # Dramaturgia 😎
    with st.spinner("Sprawdzanie w bazie legend..."):
        time.sleep(2)

    st.balloons()

    st.markdown('<div class="boom">💥 DOSTĘP PRZYZNANY 💥</div>', unsafe_allow_html=True)

    st.markdown("""
    # 🎉 WSZYSTKIEGO NAJLEPSZEGO RAFAŁ! 🎉
    
    Jedyny zawodnik, którego nie wykupi nawet Real Madryt.  
    Galáctico Rodziny.  
    Człowiek, legenda, ojciec.
    """)

    st.markdown("## 📊 Statystyki sezonu 2026")

    col1, col2, col3 = st.columns(3)

    col1.metric("🔥 Poziom legendy", "101")
    col2.metric("🐶 Głasków Candy dziennie", "127")
    col3.metric("⚽ Znajomość Realu", "100")

    st.markdown("---")
    st.markdown("## 💙 Największe miłości")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ⚽ Real Madryt")
        st.write("Miłość silniejsza niż jakikolwiek transfer.")
        st.write("Liga Mistrzów? Oczywiście oglądane wszystkie.")

    with col2:
        st.markdown("### 🐶 Candy")
        st.write("Jedyna istota, która cieszy się bardziej niż kibice po finale.")
        st.write("Oficjalny najlepszy przyjaciel legendy.")

    st.markdown("---")

    wishes = [
        "Oby Real zdobył więcej trofeów niż masz świeczek na torcie!",
        "Oby Candy patrzyła na Ciebie zawsze tak, jak Ty patrzysz na Real!",
        "Zdrowia, radości i samych zwycięskich sezonów!",
        "Niech Twoje życie będzie tak piękne jak finał Ligi Mistrzów!"
    ]

    if st.button("🎁 Wygeneruj specjalne życzenia"):
        st.success(random.choice(wishes))

    st.markdown("---")
    st.markdown("### 👑 Status: LEGENDA RODZINY")

else:
    st.warning("❌ Ta strona jest dostępna tylko dla jednej osoby.")
    st.info("Jeśli nie masz na imię Rafał... wróć z prawdziwą legendą 😉")