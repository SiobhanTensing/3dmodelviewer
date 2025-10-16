import streamlit as st
import pythreejs as p3d
import numpy as np

st.title("GLB 3D Model Viewer")

uploaded_file = st.file_uploader("Upload a GLB file", type=["glb"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    
    # Load the GLB file
    model_data = uploaded_file.read()
    
    # Create a 3D scene
    scene = p3d.Scene()
    camera = p3d.PerspectiveCamera(position=[0, 1, 3], fov=75)
    renderer = p3d.Renderer(camera=camera, scene=scene, controls=[p3d.OrbitControls(controlling=camera)])
    
    # Create a GLB loader
    loader = p3d.GLTFLoader()
    loader.load(model_data, lambda gltf: scene.add(gltf.scene))
    
    # Display the 3D model
    st.pydeck_chart(renderer)