import streamlit as st
import openai
import os
from dotenv import load_dotenv
import re

load_dotenv()

class ParagraphDivider:
    def __init__(self):
        self.client = None
        self.setup_openai()
    
    def setup_openai(self):
        """Setup OpenAI client with API key"""
        api_key = None
        try:
            api_key = st.secrets["OPENAI_API_KEY"]
        except (KeyError, FileNotFoundError):
            api_key = os.getenv("OPENAI_API_KEY")
        
        if api_key:
            self.client = openai.OpenAI(api_key=api_key)
        else:
            self.client = None
    
    def split_paragraph(self, text, division_style="semantic"):
        """
        Split a long paragraph into smaller, meaningful paragraphs using OpenAI
        
        Args:
            text (str): The input text to split
            division_style (str): Style of division - "semantic", "balanced", or "detailed"
        
        Returns:
            str: Formatted text with proper paragraph breaks
        """
        if not self.client:
            return "❌ OpenAI API key not configured. Please set OPENAI_API_KEY in Streamlit secrets or .env file"
        
        # Define division strategies
        division_strategies = {
            "semantic": {
                "description": "Divide by meaning and logical topics",
                "rules": """
1. Analyze the meaning and themes of the text
2. Split paragraphs at natural topic transition points
3. Each paragraph must have a clear and complete main idea
4. Prioritize logical connection over sentence count
5. Create paragraphs with appropriate length for the content"""
            },
            "balanced": {
                "description": "Balance between meaning and length",
                "rules": """
1. Divide by meaning but try to keep paragraphs relatively even in length
2. Each paragraph should have 2-4 sentences, unless logic requires otherwise
3. Find balance between coherence and length
4. Prioritize meaning when there's conflict with length"""
            },
            "detailed": {
                "description": "Detailed breakdown for readability",
                "rules": """
1. Split into many short paragraphs for easy reading
2. Each paragraph focuses on one specific aspect
3. Create many natural stopping points for readers
4. Suitable for long and complex texts"""
            }
        }
        
        strategy = division_strategies.get(division_style, division_strategies["semantic"])
        
        try:
            prompt = f"""
You are a professional text editor expert. Your task is to split a long paragraph into smaller, meaningful paragraphs that maintain logical flow and coherence.

Division Strategy: {strategy['description']}

Detailed Rules:
{strategy['rules']}

General Principles:
- Preserve the original meaning and flow of thought in the text
- Use natural break points (topic changes, time transitions, viewpoints)
- Keep the text in English
- Don't add any content or commentary
- Only return the text divided with appropriate paragraph breaks
- Use double line breaks (\\n\\n) to separate paragraphs

Text to split:
{text}

Please return the text divided into well-structured paragraphs:
"""
            
            response = self.client.chat.completions.create(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "system", "content": "You are a professional text editor specializing in paragraph structuring and text formatting for English texts."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=2500
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"❌ Error processing text: {str(e)}"
    
    def count_paragraphs(self, text):
        """Count the number of paragraphs in text"""
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        return len(paragraphs)
    
    def count_sentences(self, text):
        sentences = re.findall(r'[.!?]+', text)
        return len(sentences)

def main():
    st.set_page_config(
        page_title="Paragraph Divider",
        page_icon="📝",
        layout="wide"
    )
    
    st.title("📝 Paragraph Divider")
    st.subheader("Split long paragraphs into smaller, meaningful ones")
    st.markdown("---")
    
    # Initialize the paragraph divider
    divider = ParagraphDivider()
    
    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Check API Key status
        if divider.client:
            st.success("Hello chopchop")
        else:
            st.error("❌ OpenAI API Key not configured")
            st.info("💡 Please configure API key in Streamlit secrets or .env file")
        
        # Division style selection
        division_style = st.selectbox(
            "Division Style",
            ["semantic", "balanced", "detailed"],
            format_func=lambda x: {
                "semantic": "🎯 Semantic",
                "balanced": "⚖️ Balanced", 
                "detailed": "📝 Detailed"
            }[x],
            index=0,
            help="Choose the paragraph division style that fits your purpose"
        )
        
        style_descriptions = {
            "semantic": "Divide by meaning and logical topics - most natural",
            "balanced": "Balance between meaning and length - good for most cases",
            "detailed": "Detailed breakdown for readability - good for complex texts"
        }
        
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📄 Original Text")
        input_text = st.text_area(
            "Enter long paragraph to split:",
            height=400,
            placeholder="Paste your long paragraph here...",
            help="Enter or paste the long paragraph you want to split into smaller ones"
        )
        
        if input_text:
            original_paragraphs = divider.count_paragraphs(input_text)
            original_sentences = divider.count_sentences(input_text)
            
            st.info(f"📊 **Original Text Statistics:**\n"
                   f"- Paragraphs: {original_paragraphs}\n"
                   f"- Sentences: {original_sentences}\n"
                   f"- Words: {len(input_text.split())}")
    
    with col2:
        st.header("✨ Split Result")
        
        if st.button("🔄 Split Paragraph", type="primary", use_container_width=True):
            if not input_text:
                st.warning("⚠️ Please enter text to split")
            elif not divider.client:
                st.error("❌ Please configure OpenAI API Key in Streamlit secrets or .env file")
            else:
                with st.spinner("🤔 Processing text..."):
                    result = divider.split_paragraph(
                        input_text, 
                        division_style=division_style
                    )
                
                if result.startswith("❌"):
                    st.error(result)
                else:
                    st.success("✅ Paragraph split successfully!")
                    
                    # Display result
                    st.text_area(
                        "Result:",
                        value=result,
                        height=350,
                        help="Text has been split into smaller paragraphs"
                    )
                    
                    # Statistics for result
                    new_paragraphs = divider.count_paragraphs(result)
                    new_sentences = divider.count_sentences(result)
                    
                    st.info(f"📈 **Result Statistics:**\n"
                           f"- New paragraphs: {new_paragraphs}\n"
                           f"- Sentences: {new_sentences}\n"
                           f"- Words: {len(result.split())}")
                    
                    # Download button
                    st.download_button(
                        label="💾 Download Result",
                        data=result,
                        file_name="divided_paragraphs.txt",
                        mime="text/plain"
                    )
    

if __name__ == "__main__":
    main()