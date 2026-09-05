import re
import random

# A curated list of quotes related to Cyber Security, AI, Tech, and Motivation
quotes = [
    '"Security is a process, not a product." – Bruce Schneier',
    '"There are only two types of companies: those that have been hacked, and those that will be." – Robert Mueller',
    '"If you think technology can solve your security problems, then you don\'t understand the problems and you don\'t understand the technology." – Bruce Schneier',
    '"The only truly secure system is one that is powered off, cast in a block of concrete and sealed in a lead-lined room with armed guards - and even then I have my doubts." – Gene Spafford',
    '"Hardware is easy to protect: lock it in a room, chain it to a desk, or buy a spare. Information poses more of a problem." – Bruce Schneier',
    '"Amateurs hack systems, professionals hack people." – Bruce Schneier',
    '"Artificial intelligence is the new electricity." – Andrew Ng',
    '"Some people worry that artificial intelligence will make us feel inferior, but then, anybody in his right mind should have an inferiority complex every time he looks at a flower." – Alan Kay',
    '"We are entering a new world. The technologies of machine learning, speech recognition, and natural language understanding are reaching a nexus of capability." – Bill Gates',
    '"The question of whether a computer can think is no more interesting than the question of whether a submarine can swim." – Edsger W. Dijkstra',
    '"By far, the greatest danger of Artificial Intelligence is that people conclude too early that they understand it." – Eliezer Yudkowsky',
    '"In the world of cyber security, the last thing you want is a target painted on your back." – Anonymous',
    '"Cybersecurity is a shared responsibility, and it boils down to this: in cybersecurity, the more systems we secure, the more secure we all are." – Jeh Johnson',
    '"Privacy is not an option, and it shouldn\'t be the price we accept for just getting on the internet." – Gary Kovacs',
    '"As we’ve come to realize, the idea that security starts and ends with the purchase of a prepackaged firewall is simply misguided." – Art Wittmann',
    '"Technology trust is a good thing, but control is a better one." – Stephane Nappo',
    '"Cyber-Security is much more than a matter of IT." – Stephane Nappo',
    '"One of the main cyber-risks is to think they don’t exist." – Stephane Nappo',
    '"The advance of technology is based on making it fit in so that you don\'t really even notice it, so it\'s part of everyday life." – Bill Gates',
    '"It has become appallingly obvious that our technology has exceeded our humanity." – Albert Einstein',
]

def update_readme():
    readme_path = 'README.md'
    
    # Read the current content of the README
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Select a random quote
    quote = random.choice(quotes)
    
    # Define the new text to replace the old block
    replacement = f'<!-- QUOTE_START -->\n  <i>{quote}</i>\n  <!-- QUOTE_END -->'
    
    # Replace the text between the markers
    pattern = r'<!-- QUOTE_START -->.*?<!-- QUOTE_END -->'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write the updated content back to the README
    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
        
    print(f"Updated README with quote: {quote}")

if __name__ == '__main__':
    update_readme()
