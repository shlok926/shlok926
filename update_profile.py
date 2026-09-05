import urllib.request
import xml.etree.ElementTree as ET
import re
import random

# Curated list of quotes related to Cyber Security, AI, Tech, and Motivation
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
    '"Technology trust is a good thing, but control is a better one." – Stephane Nappo',
    '"One of the main cyber-risks is to think they don’t exist." – Stephane Nappo',
]

def fetch_latest_rss_item(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        response = urllib.request.urlopen(req, timeout=10)
        xml_data = response.read()
        root = ET.fromstring(xml_data)
        
        # Find the first item in the RSS feed
        item = root.find('./channel/item')
        if item is not None:
            title = item.find('title').text
            link = item.find('link').text
            return f'<a href="{link}" target="_blank">{title}</a>'
        return None
    except Exception as e:
        print(f"Error fetching from {url}: {e}")
        return None

def update_readme():
    readme_path = 'README.md'
    
    # RSS Feeds for Cybersecurity News and CVEs
    cve_feed = "https://hnrss.org/newest?q=CVE"
    news_feed = "https://hnrss.org/newest?q=Cybersecurity"
    
    print("Fetching latest CVE...")
    cve_item = fetch_latest_rss_item(cve_feed)
    if not cve_item:
        cve_item = "Stay tuned for the latest CVE updates."
        
    print("Fetching latest Tech News...")
    news_item = fetch_latest_rss_item(news_feed)
    if not news_item:
        news_item = "Stay tuned for the latest Tech News."
        
    quote = random.choice(quotes)
    
    print("Reading README.md...")
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replacements
    content = re.sub(r'<!-- QUOTE_START -->.*?<!-- QUOTE_END -->', 
                     f'<!-- QUOTE_START -->\n  <i>{quote}</i>\n  <!-- QUOTE_END -->', 
                     content, flags=re.DOTALL)
                     
    content = re.sub(r'<!-- CVE_START -->.*?<!-- CVE_END -->', 
                     f'<!-- CVE_START -->\n  {cve_item}\n  <!-- CVE_END -->', 
                     content, flags=re.DOTALL)
                     
    content = re.sub(r'<!-- NEWS_START -->.*?<!-- NEWS_END -->', 
                     f'<!-- NEWS_START -->\n  {news_item}\n  <!-- NEWS_END -->', 
                     content, flags=re.DOTALL)
    
    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print("README.md has been successfully updated!")

if __name__ == '__main__':
    update_readme()
