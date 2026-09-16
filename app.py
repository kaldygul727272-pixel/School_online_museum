import streamlit as st
import pandas as pd
import os

# 1. Сайттың баптаулары мен тақырыбы
st.set_page_config(page_title="Шымкент қ. Кешкі мектеп мұражайы", layout="wide")
st.title("🏛 Шымкент қаласы білім басқармасының «Кешкі мектеп» КММ")
st.subheader("«Онлайн тарихи мұражай» веб-порталы")
st.write("Мектебіміздің тарихы, басшылығы, ұстаздар құрамы мен оқушылар базасы")

# Ресми мәліметтер панелі
with st.expander("📋 Мектептің мемлекеттік тіркеу туралы ресми мәліметтері"):
    st.write("**Бизнес-сәйкестендіру нөмірі (БСН):** 260540027150")
    st.write("**Орналасқан жері:** Қазақстан, Шымкент қаласы, Қаратау ауданы, Қайтпас шағын ауданы, Мұхамедқұл Исламқұлов көшесі, 156 ғимарат, пошта индексі 160009")

# 2. Мәліметтер базасы
teachers_data = [
    {"Аты-жөні": "Амантай Толқынай", "Телефон нөмірі": "8 (778) 888-11-15"},
    {"Аты-жөні": "Айтбекова Сәуле", "Телефон нөмірі": "8 (771) 252-52-24"},
    {"Аты-жөні": "Сәбденова Гүлнар", "Телефон нөмірі": "8 (771) 252-52-24"},
    {"Аты-жөні": "Балкыбекова Хадиша", "Телефон нөмірі": "+7 (771) 616-77-74"},
    {"Аты-жөні": "Досымбекова Гульвира", "Телефон нөмірі": "8 (778) 445-93-80"},
]

students_data = [
    {"№": 1, "Аты-жөні": "Асанәлі Мұратұлы", "Сыныбы": "10А", "Жетістігі": "Мектеп мақтанышы, спорт жеңімпазы"},
    {"№": 2, "Аты-жөні": "Аружан Серікқызы", "Сыныбы": "11Б", "Жетістігі": "Алтын белгіге үміткер, олимпиада жүлдегері"},
    {"№": 3, "Аты-жөні": "Нұрсұлтан Әлиев", "Сыныбы": "11А", "Жетістігі": "Қоғамдық жұмыс белсендісі"},
]

# 3. Сайттың интерфейсі (Сайдбар мәзірі)
st.sidebar.header("Мұражай бөлімдері")
section = st.sidebar.radio("Көру үшін таңдаңыз:", [
    "Басты бет", 
    "Басшылық", 
    "Ұстаздар құрамы", 
    "Іс-шаралар фотодеректері", 
    "Оқушылар базасы", 
    "Кері байланыс"
])

if section == "Басты бет":
    st.subheader("✨ Мұражайға қош келдіңіздер!")
    st.write("Бұл портал Шымкент қаласының «Кешкі мектебінің» тарихын, жетістіктерін цифрландыру мақсатында жасалған.")
    
    if os.path.exists("school.jpg"):
        st.image("school.jpg", caption="«Кешкі мектеп» КММ ғимараты", width=600)
    elif os.path.exists("school.png.jpg"):
        st.image("school.png.jpg", caption="«Кешкі мектеп» КММ ғимараты", width=600)
    else:
        st.warning("Мектеп суреті жүктелуде...")
    
elif section == "Басшылық":
    st.subheader("👤 Мектеп басшылығы")
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("direktor.png.jpeg"):
            st.image("direktor.png.jpeg", caption="Мектеп басшысы", width=200)
        else:
            st.warning("Директор суреті жүктелуде...")
    with col2:
        st.markdown("### **Қайранбеков Мейрамхан Дәрменбекович**")
        st.write("**Лауазымы:** Заңды тұлғаның уәкілетті органымен тағайындалған м.а. басқарушы.")
        st.write("**Тіркелген күні:** 02.07.2026 жылғы ресми анықтама негізінде.")
        st.info("«Біздің мақсатымыз — әрбір оқушыға сапалы білім нәрін сеуіп, мектебіміздің тарихын болашақ ұрпаққа цифрлы форматта аманаттау.»")

elif section == "Ұстаздар құрамы":
    st.subheader("👩‍🏫 Мектептің мақтанышы — Ұстаздар")
    st.write("Мектепте қызмет атқаратын тәжірибелі мұғалімдер тізімі мен байланыс нөмірлері:")
    
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        if os.path.exists("amantay.png.jpeg"):
            st.image("amantay.png.jpeg", caption="Амантай Толқынай", width=160)
    with t_col2:
        if os.path.exists("aitbekova.png.jpeg"):
            st.image("aitbekova.png.jpeg", caption="Айтбекова Сәуле", width=160)
            
    st.write("") 
    df_teachers = pd.DataFrame(teachers_data)
    st.table(df_teachers)

elif section == "Іс-шаралар фотодеректері":
    st.subheader("📸 Мектеп өмірінен фотодеректер мен маңызды іс-шаралар")
    st.write("Мектебімізде өткен маңызды мәдени, тарихи және қоғамдық іс-шаралардың фотогалереясы:")
    
    # 5 жаңа суретті бағандарға бөліп әдемі орналастыру
    col_a, col_b = st.columns(2)
    with col_a:
        if os.path.exists("school1.jpeg"):
            st.image("school1.jpeg", caption="Мектеп өмірінен көрініс (1)", use_container_width=True)
        if os.path.exists("school3.jpeg"):
            st.image("school3.jpeg", caption="Мектеп өмірінен көрініс (3)", use_container_width=True)
        if os.path.exists("school5.jpeg"):
            st.image("school5.jpeg", caption="Мектеп өмірінен көрініс (5)", use_container_width=True)
            
    with col_b:
        if os.path.exists("school2.jpeg"):
            st.image("school2.jpeg", caption="Мектеп өмірінен көрініс (2)", use_container_width=True)
        if os.path.exists("school4.jpeg"):
            st.image("school4.jpeg", caption="Мектеп өмірінен көрініс (4)", use_container_width=True)

    # 🎥 СІЗ ЖІБЕРГЕН ФЕЙСБУК ВИДЕОЛАР БЛОГЫ
    st.write("---") 
    st.subheader("🎥 Мектептің виртуалды видеомұрағаты")
    st.write("Facebook әлеуметтік желісіндегі мектептің ресми іс-шаралары мен бейнероликтері:")
    
    v_col1, v_col2 = st.columns(2)
    with v_col1:
        st.video("https://www.facebook.com/share/r/1CTynihoVH/")
        st.caption("📽 Мектептің салтанатты іс-шарасы (1-видео)")
        
    with v_col2:
        st.video("https://www.facebook.com/share/r/1PoZLUPL3X/")
        st.caption("🎞 Мектеп тынысы мен маңызды сәттер (2-видео)")

elif section == "Оқушылар базасы":
    st.subheader("🎓 Оқушылар мен түлектер мәліметтер қоры")
    st.write("Мұражайдың осы бөлімінде белсенді оқушылардың тізімін іздеу жүйесі арқылы көруге болады:")
    
    df_students = pd.DataFrame(students_data)
    search = st.text_input("Оқушының атын жазып іздеңіз:")
    if search:
        filtered_df = df_students[df_students['Аты-жөні'].str.contains(search, case=False)]
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.dataframe(df_students, use_container_width=True)

elif section == "Кері байланыс":
    st.subheader("📞 Жаңа мәлімет қосу / Кері байланыс")
    st.write("Егер мұражай қорына қосатын тарихи материалдарыңыз болса, төмендегі форманы толтырыңыз:")
    name = st.text_input("Аты-жөніңіз:")
    info_type = st.selectbox("Ақпарат түрі:", ["Ұстаз туралы", "Оқушы туралы", "Тарихи жәдігер"])
    text = st.text_area("Сипаттамасы немесе ұсынысыңыз:")
    if st.button("Мәліметті жіберу"):
        st.success("Рахмет! Мәлімет қабылданды, тексерістен кейін базаға автоматты түрде қосылады.")
