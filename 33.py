import streamlit as st

st.set_page_config(page_title="Поліція України", page_icon="🛡️")

# Заголовок
st.title("🛡️ Національна поліція України")
st.image("123.png", width=200)

st.markdown("""
Національна поліція України — це центральний орган виконавчої влади, який забезпечує охорону правопорядку, прав і свобод громадян.
""")

# Розділи поліції
st.header("📌 Основні відділи поліції:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚓 Патрульна поліція")
    st.image("https://npu.gov.ua/assets/main/img/patrulna.jpg", caption="Патрульна поліція", use_column_width=True)
    st.write("Забезпечує безпеку на вулицях, регулює дорожній рух, реагує на виклики громадян.")

with col2:
    st.subheader("🕵️ Кримінальна поліція")
    st.image("https://npu.gov.ua/assets/main/img/krim-police.jpg", caption="Кримінальна поліція", use_column_width=True)
    st.write("Розслідує кримінальні правопорушення, займається боротьбою зі злочинністю.")

col3, col4 = st.columns(2)

with col3:
    st.subheader("👮 Спеціальні підрозділи")
    st.image("https://npu.gov.ua/assets/main/img/spets-pidrozdil.jpg", caption="Спецпідрозділи", use_column_width=True)
    st.write("Призначені для боротьби з організованою злочинністю, тероризмом, охорони масових заходів.")

with col4:
    st.subheader("🧑‍💼 Слідчий відділ")
    st.image("https://npu.gov.ua/assets/main/img/slidchiy.jpg", caption="Слідчий відділ", use_column_width=True)
    st.write("Займається документуванням злочинів, збором доказів, слідчими діями.")

# Контакти
st.header("📞 Контакти")

st.markdown("""
- **Гаряча лінія поліції**: 102
- **Офіційний сайт**: [npu.gov.ua](https://npu.gov.ua)
- **Facebook**: [facebook.com/UA.Police](https://www.facebook.com/UA.Police)
""")

# Футер
st.markdown("---")
st.caption("© 2025 Інформативний проєкт про поліцію України. Всі зображення з офіційного сайту НПУ.")
