import streamlit as st
from PIL import Image
import io
import base64

st.title("密码验证")

# 硬编码的六位密码
correct_password = "837562"

# 硬编码的 Base64 图像数据（小图示例）
base64_image = (
    "iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAE0lEQVR4nO3BMQEAAADCoPVPbQkfoAAAAC8DnIyMrEIBz1UAAAAASUVORK5CYII="
)

# 输入密码
password_input = st.text_input("请输入密码", type="password")

if password_input:
    if password_input == correct_password:
        st.success("✅ 密码正确！")
        st.balloons()

        # 解析并显示 Base64 图像
        try:
            img_data = base64.b64decode(base64_image)
            image = Image.open(io.BytesIO(img_data))
            st.header("已解密的图片")
            st.image(image, use_container_width=False, caption="Base64 解码图像")
            st.write(f"📊 图像大小: {image.size}")
            st.write(f"🎨 颜色模式: {image.mode}")
            st.write(f"📦 数据大小: {len(img_data)} 字节")
        except Exception as e:
            st.error(f"解析 Base64 图像失败: {e}")

    else:
        st.error("❌ 密码错误！")

st.divider()
st.write("💡 提示：密码是 6 位数字")
