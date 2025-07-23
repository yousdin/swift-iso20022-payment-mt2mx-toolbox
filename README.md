# iso20022_toolbox.py – SWIFT Payment ISO 20022 Toolbox

## Overview

`iso20022_toolbox.py` is a Streamlit-based web application for uploading and working with payment files, including CSV and XML formats, in the context of SWIFT ISO 20022 standards. The app provides an interface to upload files, view their contents, and serves as a toolbox for payment message conversion and analysis.

## How to Use

1. **Install Requirements**

   Make sure you have Python installed. Install Streamlit if you haven’t already:
   ```bash
   pip install streamlit
   ```

2. **Run the App**

   In your terminal, navigate to the directory containing `iso20022_toolbox.py` and run:
   ```bash
   streamlit run iso20022_toolbox.py
   ```

3. **Upload a File**

   - The app will open in your default web browser.
   - Click the “Browse files” button to select a file from your computer.
   - After uploading, the name of the file will be displayed on the page.

## Features

- Upload any file type from your computer.
- Instantly displays the name of the uploaded file.
- Uses Streamlit’s wide layout for a better viewing experience.

## Example Code Snippet

```python
import streamlit as st

st.set_page_config(layout="wide")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(f"Uploaded file name: {uploaded_file.name}")
```

## Notes

- You can further customize the app to process or save the uploaded files as needed.
- For more customization, refer to the [Streamlit documentation](https://docs.streamlit.io/).
