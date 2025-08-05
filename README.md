# Pa## Features

- ✨ Split long paragraphs into smaller, meaningful ones based on semantics and logic
- 🎯 **Semantic Division**: Most natural, based on topics and content logic
- ⚖️ **Balanced Division**: Combines meaning with appropriate length
- 📝 **Detailed Division**: Split into many parts for easy reading and tracking
- 🌐 Supports English text processing
- 📊 Display text statistics (paragraphs, sentences, words)
- 💾 Download results as text file
- 🎨 User-friendly interfacevider App

An application that splits long paragraphs into smaller, meaningful paragraphs using OpenAI and Streamlit.

## Tính năng

- ✨ Chia đoạn văn dài thành các đoạn nhỏ hơn theo nghĩa và logic
- � **Chia theo nghĩa (Semantic)**: Tự nhiên nhất, dựa trên chủ đề và logic nội dung
- ⚖️ **Chia cân bằng (Balanced)**: Kết hợp giữa nghĩa và độ dài phù hợp
- 📝 **Chia chi tiết (Detailed)**: Chia nhỏ nhiều để dễ đọc và theo dõi
- 🌐 Hỗ trợ tiếng Việt và tiếng Anh
- 📊 Hiển thị thống kê văn bản (số đoạn, câu, từ)
- 💾 Tải xuống kết quả dạng file text
- 🎨 Giao diện thân thiện với người dùng

## Installation

### 1. Clone repository

```bash
git clone <repository-url>
cd ParagraphDivider
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure OpenAI API Key

#### Method 1: Streamlit Secrets (Recommended)

1. Create `.streamlit` directory (if not exists):
   ```bash
   mkdir -p .streamlit
   ```

2. Create `secrets.toml` file:
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   ```

3. Get API key from [OpenAI Platform](https://platform.openai.com/api-keys)

4. Open `.streamlit/secrets.toml` and replace `your_openai_api_key_here` with your actual API key:
   ```toml
   OPENAI_API_KEY = "sk-1234567890abcdef..."
   ```

#### Method 2: Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Get API key from [OpenAI Platform](https://platform.openai.com/api-keys)

3. Open `.env` file and replace `your_openai_api_key_here` with your actual API key:
   ```
   OPENAI_API_KEY=sk-1234567890abcdef...
   ```

## Usage

### Run the application

```bash
streamlit run main.py
```

The application will open at `http://localhost:8501`

### How to use

1. **Configure API Key**: API key is automatically loaded from Streamlit secrets or .env file
2. **Paste text**: Paste long paragraph in the "Original Text" area
3. **Settings**: 
   - Choose division style:
     - **🎯 Semantic**: Divide by topics and natural logic
     - **⚖️ Balanced**: Balance between meaning and appropriate length
     - **📝 Detailed**: Detailed breakdown for easy reading
4. **Split**: Click "Split Paragraph" button
5. **View result**: Result is displayed on the right with detailed statistics
6. **Download**: Use "Download Result" button to save file

## Example

**Original Text:**
```
Artificial intelligence (AI) is comprehensively transforming how we live and work. From automating simple tasks like answering emails to solving complex problems like weather prediction and disease diagnosis, AI has become an indispensable part of modern life. AI applications are widely used in various fields: healthcare, education, transportation, and business. However, the rapid development of AI also poses serious challenges regarding ethics, security, and social impact.
```

**Result after Semantic Division:**
```
Artificial intelligence (AI) is comprehensively transforming how we live and work. From automating simple tasks like answering emails to solving complex problems like weather prediction and disease diagnosis, AI has become an indispensable part of modern life.

AI applications are widely used in various fields: healthcare, education, transportation, and business.

However, the rapid development of AI also poses serious challenges regarding ethics, security, and social impact.
```

### Division Styles

- **🎯 Semantic**: Divide by logical topics, creating the most natural paragraphs
- **⚖️ Balanced**: Combine content logic with appropriate length  
- **📝 Detailed**: Split into many parts for easy reading, suitable for complex texts

## Project Structure

```
ParagraphDivider/
├── main.py                    # Main file containing Streamlit application
├── requirements.txt           # Python dependencies
├── .env.example              # Template for environment configuration
├── .env                      # Environment configuration file (to be created)
├── .streamlit/
│   ├── secrets.toml.example  # Template for Streamlit secrets
│   └── secrets.toml          # Streamlit secrets file (to be created)
├── .gitignore               # Git ignore rules
├── venv/                    # Python virtual environment
└── README.md                # This guide
```

## System Requirements

- Python 3.8+
- OpenAI API key
- Internet connection

## Notes

- Requires OpenAI API key to use
- Each use consumes a small amount of OpenAI credits
- Application uses GPT-4o model for best results

## Support

If you encounter issues, please:
1. Check if API key is configured correctly
2. Ensure internet connection is available
3. Check OpenAI account balance

## License

MIT License
