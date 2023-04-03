import streamlit as st
import base64

file_path='C:/Users/win10/Desktop/avsc.12388.pdf'

# Display a file uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Check if a file is uploaded
if uploaded_file is not None:

    # Encode the file using base64
    base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")

    # Embed the pdf file in HTML iframe
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'

    # Render the pdf file in streamlit
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Display a download button
    st.download_button("Download PDF", uploaded_file, "application/pdf")


def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


show_pdf('C:/Users/win10/Desktop/small-prin-test.pdf')