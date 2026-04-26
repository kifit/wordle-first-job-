import streamlit as st

st.set_page_config(page_title="Проверка букв", page_icon="📝")

# Создаем хранилище для истории, если его еще нет
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("🔍 Проверка слова")

target = "алмаз"
word = st.text_input("Введите слово:", key="input_word")

if st.button("Проверить"):
    if word:
        # Формируем результат проверки
        current_result = []
        for letter in word:
            status = "✅ YES" if letter.lower() in target.lower() else "❌ NO"
            current_result.append(f"{letter}: {status}")
        
        # Добавляем в начало истории (чтобы новое было сверху)
        st.session_state.history.insert(0, {"word": word, "res": current_result})
    else:
        st.warning("Введите хоть что-нибудь!")

# Отображение истории
if st.session_state.history:
    st.divider()
    st.subheader("📜 Прошлые попытки:")
    
    for item in st.session_state.history:
        # Делаем выпадающий список для каждой попытки
        with st.expander(f"Слово: {item['word']}"):
            for line in item['res']:
                st.write(line)

# Кнопка очистки истории
if st.sidebar.button("Очистить историю"):
    st.session_state.history = []
    st.rerun()
