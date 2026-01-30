import streamlit as st
from PIL import Image
import io
import base64

st.title("密码验证")

# 硬编码的六位密码
correct_password = "837562"

# 输入密码
password_input = st.text_input("请输入密码", type="password")

if password_input:
    if password_input == correct_password:
        st.success("✅ 密码正确！")
        st.balloons()
    else:
        st.error("❌ 密码错误！")

st.divider()
st.write("💡 提示：密码是 6 位数字")
