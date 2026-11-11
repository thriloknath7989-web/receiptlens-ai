with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# స్టైల్ ట్యాగ్ లేదా కార్డ్ క్లాస్ ని అడ్జస్ట్ చేయడం కోసం సింపుల్ CSS యాడ్ చేద్దాం
card_css = """
<style>
  body {
    background-color: #f0f4f8;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    margin: 0;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  }
  .app-card {
    background: #ffffff;
    max-width: 400px;
    width: 100%;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    box-sizing: border-box;
  }
</style>
"""

# <head> లోపల CSS పెట్టడం లేదా ఇప్పటికే ఉంటే రిప్లేస్ చేయడం
if "<head>" in html:
    html = html.replace("<head>", "<head>\n" + card_css)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("UI Card style added successfully!")
