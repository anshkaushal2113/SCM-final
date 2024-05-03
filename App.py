from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
import os


load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')

# Set OpenAI API key and organization
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG")

def generate_cover_letter(prompt):
      response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",  # Change the model ID here if needed
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        # engine="davinci"  # Make sure to specify the engine
    )
      print(response)
      return response.choices[0].text
    

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get form data
    position = request.form.get('position')
    company = request.form.get('company')
    description = request.form.get('description')
    word_count = request.form.get('wordCount')
    tone = request.form.get('tone')

    # Create the prompt
    prompt = f"""
    Dear ChatGPT,

    I am currently applying for the {position} position at {company} and I am seeking your assistance in crafting a compelling cover letter.

    Could you please help me by using the following information to create an effective cover letter?

    Job Description: {description}
    Additional instructions: The cover letter should be between {word_count} words long. The tone should be {tone}. The text should be well-structured with clearly defined paragraphs.
    Thank you for your assistance, and I look forward to seeing what you create.
    """
    

    cover_letter = generate_cover_letter(prompt)
    print(cover_letter)

    # Return the generated cover letter as JSON
    return jsonify(cover_letter=cover_letter)

if __name__ == '__main__':
    app.run(debug=True)
