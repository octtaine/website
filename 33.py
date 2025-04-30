import streamlit as st

st.set_page_config(page_title="Поліція України", page_icon="🛡️")

st.title("🛡️ Національна поліція України")
st.image("123.png", width=200)

st.markdown("""
Національна поліція України — це центральний орган виконавчої влади, який забезпечує охорону правопорядку, прав і свобод громадян.
""")

st.header("📌 Основні відділи поліції:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚓 Патрульна поліція")
    st.image("127.png", caption="Патрульна поліція", use_container_width=True)
    st.write("Забезпечує безпеку на вулицях, регулює дорожній рух, реагує на виклики громадян.")

with col2:
    st.subheader("🕵️ Кримінальна поліція")
    st.image("124.png", caption="Кримінальна поліція", use_container_width=True)
    st.write("Розслідує кримінальні правопорушення, займається боротьбою зі злочинністю.")

col3, col4 = st.columns(2)

with col3:
    st.subheader("👮 Спеціальні підрозділи")
    st.image("125.png", caption="Спецпідрозділи", use_container_width=True)
    st.write("Призначені для боротьби з організованою злочинністю, тероризмом, охорони масових заходів.")

with col4:
    st.subheader("🧑‍💼 Слідчий відділ")
    st.image("126.png", caption="Слідчий відділ", use_container_width=True)
    st.write("Займається документуванням злочинів, збором доказів, слідчими діями.")

st.header("📞 Контакти")

st.markdown("""
- **Гаряча лінія поліції**: 102
- **Офіційний сайт**: [npu.gov.ua](https://npu.gov.ua)
- **Facebook**: [facebook.com/UA.Police](https://www.facebook.com/UA.Police)
""")

st.markdown("---")
st.caption("© 2025 Інформативний проєкт про поліцію України. Всі зображення з офіційного сайту НПУ.")
