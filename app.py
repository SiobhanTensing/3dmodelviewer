import streamlit as st
import base64
import html

st.title("GLB 3D Model Viewer")

uploaded_file = st.file_uploader("Upload a GLB file", type=["glb"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    model_bytes = uploaded_file.read()
    b64 = base64.b64encode(model_bytes).decode("utf-8")
    data_url = f"data:model/gltf-binary;base64,{b64}"

    # Minimal HTML that uses the model-viewer web component to display the GLB
    html_content = f'''
    <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
    <model-viewer src="{html.escape(data_url)}"
                  alt="Uploaded GLB"
                  camera-controls
                  auto-rotate
                  exposure="1"
                  style="width:100%; height:640px; background-color: #f0f0f0;">
    </model-viewer>
    '''

    st.components.v1.html(html_content, height=700)