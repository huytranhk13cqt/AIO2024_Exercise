# Q1. -> A

```python
# hiển thị chuỗi văn bản trong streamlit
st.text(...)
```

# Q2. -> C

```python
import streamlit as st

options = st.multiselect("Your favorite colors:", [
                         "Green", "Yellow", "Red", "Blue"], ["Yellow", "Red"])
st.write("You selected:", options)
```

# Q3. -> D

```python
# người dùng nhập văn bản trong streamlit
st.text_input('Enter your name')
```

# Q4. -> C

```python
import streamlit as st

# khai báo sai
st.image("../practice_exercise/data/cris2.jpg",
         caption="Uploaded Image", width="RGB", channels="RGB")

# khai báo đúng
import streamlit as st

st.image("../practice_exercise/data/cris2.jpg",
         caption="Uploaded Image", width=300, channels="RGB")
```

# Q5. -> A

```python
# thêm vào file vocab "elements"
# chạy word_correction.py
# nhập elmets
# quan sát kết quả
```

# Q6. -> D

```python
import streamlit as st

# Initialize session state variables
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Define a function to increment the counter
def increment_counter():
    st.session_state.counter += 1

# Define a function to reset the counter
def reset_counter():
    st.session_state.counter = 0

# Display the current value of the counter
st.write(f"Counter value: {st.session_state.counter}")

# Create buttons to interact with the counter
st.button("Increment", on_click=increment_counter)
st.button("Reset", on_click=reset_counter)

# Use session state to manage a text input
if 'user_name' not in st.session_state:
    st.session_state.user_name = ''

user_input = st.text_input("Enter your name", st.session_state.user_name)
if user_input:
    st.session_state.user_name = user_input

st.write(f"Hello, {st.session_state.user_name}!")

# Store and retrieve session state for other widgets
if 'slider_value' not in st.session_state:
    st.session_state.slider_value = 0

slider_input = st.slider("Select a value", 0, 100, st.session_state.slider_value)
st.session_state.slider_value = slider_input

st.write(f"Slider value: {st.session_state.slider_value}")
```

# Q7. -> D

```python
import streamlit as st

with st.form("my_form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        st.write(f"First Name: {f_name}" + "-" + f"Last Name: {l_name}")
```

# Q8 -> A

```python
import streamlit as st
from PIL import Image

# Title of the Streamlit app
st.title("Upload Multiple Images")

# File uploader allowing multiple file uploads
uploaded_files = st.file_uploader("Choose images", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# Display uploaded images
if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        # Open the image using PIL
        image = Image.open(uploaded_file)
        # Display the image with a caption of the filename
        st.image(image, caption=uploaded_file.name)
```

# Q9 -> D

```python
# a) st.code(...): Hàm này được sử dụng để hiển thị mã nguồn với định dạng code.

# b) st.echo(...): Hàm này hiển thị mã nguồn và cũng thực thi nó, giúp kiểm tra mã nguồn ngay trong ứng dụng.

# c) st.markdown(...): Hàm này có thể hiển thị code thông qua sử dụng định dạng Markdown, nhưng không phải là công cụ chính để hiển thị code.

# d) st.slider(...): Hàm này được sử dụng để tạo một thanh trượt, không liên quan đến việc hiển thị mã nguồn.
```

# Q10 -> B

```python
# 200 MB
```
