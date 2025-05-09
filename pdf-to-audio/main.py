from google.cloud import texttospeech
import fitz

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()

        return text
    

pdf_text = extract_text_from_pdf("pdf-to-audio/test.pdf")


client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text=pdf_text)
voice = texttospeech.VoiceSelectionParams(
    language_code="de-DE", 
    name="de-DE-Wavenet-F",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

