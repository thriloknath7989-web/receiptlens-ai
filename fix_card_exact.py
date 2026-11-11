with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# రెండవ ఫోటో లాగా పర్ఫెక్ట్ వైట్ కార్డ్ అండ్ లైట్ బ్లూ అప్లోడ్ బాక్స్ కోసం CSS
perfect_css = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ReceiptLens AI</title>
    <link rel="manifest" href="manifest.json">
    <style>
        body {
            background-color: #f8fafc;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 20px 16px;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
            box-sizing: border-box;
        }
        .main-card {
            background: #ffffff;
            width: 100%;
            max-width: 400px;
            padding: 28px 24px;
            border-radius: 24px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06);
            text-align: center;
            box-sizing: border-box;
            margin-top: 10px;
        }
        h1 {
            font-size: 24px;
            color: #0f172a;
            margin-top: 0;
            margin-bottom: 8px;
            font-weight: 700;
        }
        p {
            color: #64748b;
            font-size: 14px;
            margin-bottom: 24px;
            line-height: 1.5;
        }
        .upload-box {
            border: 2px dashed #93c5fd;
            border-radius: 16px;
            padding: 24px 16px;
            background: #eff6ff;
            margin-bottom: 24px;
            text-align: center;
        }
        .upload-text {
            font-size: 14px;
            color: #1e40af;
            display: block;
            margin-bottom: 12px;
            font-weight: 500;
        }
        input[type="file"] {
            font-size: 13px;
            color: #475569;
        }
        .btn {
            background: #2563eb;
            color: white;
            border: none;
            width: 100%;
            padding: 14px;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
        }
        .btn:active {
            background: #1d4ed8;
        }
    </style>
</head>
<body>
    <div class="main-card">
        <h1>ReceiptLens AI</h1>
        <p>Instant receipt parsing & tax audit for modern businesses.</p>
        
        <div class="upload-box">
            <span class="upload-text">Tap to select receipt image</span>
            <input type="file" id="receiptInput" accept="image/*">
        </div>

        <button class="btn" onclick="alert('Scanning feature ready!')">Scan Receipt Now</button>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(perfect_css)

print("Exact match layout applied successfully!")
