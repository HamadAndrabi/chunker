
# Streamlit Chunker

This project is a Streamlit application that allows users to upload PDF files, process them into text chunks, and perform similarity searches on the text. Users can adjust chunking parameters and view the most similar chunks retrieved.

## Features

- Upload multiple PDF files
- Extract text from PDFs
- Chunk text with adjustable parameters
- Search for similar text chunks
- Display top similar chunks with similarity scores
- User-configurable settings via sidebar

## Requirements

- Python 3.7+
- Streamlit
- langchain_community
- langchain_openai
- PyPDF2

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/hamadandrabi/streamlit-chunker.git
   cd streamlit-chunker
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```sh
   streamlit run main.py
   ```

2. Open a web browser and navigate to `http://localhost:8501`.

3. In the sidebar, paste your OpenAI API key.

4. Adjust the chunking parameters (chunk size and overlap) as needed.

5. Upload your PDF files and click "Process".

6. Enter a search query to find similar text chunks.

## Configuration

- **API Key**: Enter your OpenAI API key in the sidebar.
- **Chunk Size**: Use the slider to select the size of each text chunk.
- **Chunk Overlap**: Use the slider to select the overlap between chunks.
- **Number of Chunks**: Specify how many top similar chunks to display.

## Running on Ports 80 or 443

To run the Streamlit app on ports 80 or 443, you need administrative privileges.

### On Windows

1. Open Command Prompt as an administrator.
2. Run the Streamlit app with the desired port:
   ```sh
   streamlit run main.py --server.port 80
   ```

### On Linux/macOS

1. Open a terminal.
2. Run the Streamlit app with `sudo`:
   ```sh
   sudo streamlit run main.py --server.port 80
   ```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Streamlit for the awesome web app framework
- Langchain for the vector store and embedding support
- PyPDF2 for PDF text extraction
