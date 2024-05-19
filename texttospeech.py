# Import the required modules
from gtts import gTTS
from translate import Translator
import os

# Initialize the translator
translator = Translator(to_lang="fr")

# The text that you want to convert to audio
mytext = '''Staff at The Old Brennans Wine House opened its doors for a soft launch on May 11,
taking over the site of the former Brennans Cook Shop retail store which closed in 2020.
The new venue offers a range of light grub options and a fine selection of drink sourced
from around the world, as well as a few Cork producers. Its the latest major hospitality venture
from city publican Benny McCabe, who owns bars on the Cork Heritage Pub Trail including Mutton Lane,
The Oval, Crane Lane, The Bodega, El Fenix, The Black Dog, and The Poor Relation.'''


# Split the text into chunks (for example, by sentence or by some max length)
def split_text(text, max_length=500):
    sentences = text.split('. ')
    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        if current_length + len(sentence) + 1 > max_length:
            chunks.append('. '.join(current_chunk))
            current_chunk = [sentence]
            current_length = len(sentence)
        else:
            current_chunk.append(sentence)
            current_length += len(sentence) + 1

    if current_chunk:
        chunks.append('. '.join(current_chunk))

    return chunks


# Split the original text into smaller chunks
text_chunks = split_text(mytext)

# Translate each chunk and concatenate the results
translated_chunks = [translator.translate(chunk) for chunk in text_chunks]
translated_text = '. '.join(translated_chunks)

# Language in which you want to convert
language = 'fr'

# Convert the translated text to speech
myobj = gTTS(text=translated_text, lang=language, slow=False)

# Saving the converted audio in an mp3 file named 'welcome.mp3'
myobj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")
