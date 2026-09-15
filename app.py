import streamlit as st

st.set_page_config(page_title="Мектептің Онлайн Мұражайы", layout="wide")
st.title("🏛 Мектептің «Онлайн тарихи мұражай» веб-порталы")
st.write("Мектебіміздің тарихы мен жетістіктерінің сапалы базасы")

museum_data = [
    {
        "title": "Мектептің алғашқы ғимараты (1970 жыл)",
        "desc": "Мектебіміздің ең алғаш ашылған кезіндегийн тарихи суреті.",
        "img": "https://unsplash.com"
    },
    {
        "title": "Алтын медаль иегерлері мен марапаттар",
        "desc": "Мектеп мақтаныштары — олимпиада жеңімпаздарының бұрышы.",
        "img": "https://unsplash.com"
    }
]

st.sidebar.header("Мұражай бөлімдері")
section = st.sidebar.radio("Көру үшін таңдаңыз:", ["Басты бет", "Жәдігерлер қоры", "Байланыс"])

if section == "Басты бет":
    st.subheader("Қош келдіңіздер!")
    st.write("Бұл портал мектеп тарихын цифрландыру мақсатында жасалған.")
elif section == "Жәдігерлер қоры":
    st.subheader("🏛 Виртуалды жәдігерлер көрмесі")
    cols = st.columns(2)
    for i, item in enumerate(museum_data):
        with cols[i]:
            st.image(item["img"], use_container_width=True)
            st.markdown(f"### {item['title']}")
            st.write(item["desc"])
elif section == "Байланыс":
    st.subheader("📞 Кері байланыс")
    st.text_input("Аты-жөніңіз:")
    st.text_area("Ұсынысыңыз:")
    if st.button("Жіберу"):
        st.success("Мәлімет қабылданды!")
