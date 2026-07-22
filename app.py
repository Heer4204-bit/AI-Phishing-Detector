<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Phishing Shield</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --accent-blue: #38bdf8;
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --safe-color: #22c55e;
            --danger-color: #ef4444;
            --warning-color: #f59e0b;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            width: 100%;
            max-width: 700px;
            background: var(--card-bg);
            border-radius: 16px;
            padding: 32px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
            border: 1px solid #334155;
        }

        .header {
            text-align: center;
            margin-bottom: 24px;
        }

        .header h1 {
            font-size: 1.8rem;
            color: var(--accent-blue);
            margin-bottom: 8px;
        }

        .header p {
            color: var(--text-sub);
            font-size: 0.95rem;
        }

        .input-group {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 24px;
        }

        textarea {
            width: 100%;
            height: 120px;
            background-color: #0f172a;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 12px;
            color: var(--text-main);
            font-size: 0.95rem;
            resize: vertical;
            outline: none;
            transition: border-color 0.2s;
        }

        textarea:focus {
            border-color: var(--accent-blue);
        }

        button {
            background-color: var(--accent-blue);
            color: #0f172a;
            font-weight: bold;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            transition: opacity 0.2s;
        }

        button:hover {
            opacity: 0.9;
        }

        /* Result Section */
        .result-card {
            display: none;
            background: #0f172a;
            border-radius: 12px;
            padding: 20px;
            border: 1px solid #334155;
            animation: fadeIn 0.3s ease-in-out;
        }

        .result-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }

        .status-badge {
            padding: 6px 12px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.85rem;
            text-transform: uppercase;
        }

        .safe { background: rgba(34, 197, 94, 0.15); color: var(--safe-color); }
        .danger { background: rgba(239, 68, 68, 0.15); color: var(--danger-color); }

        .meter-container {
            margin: 16px 0;
        }

        .meter-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.85rem;
            color: var(--text-sub);
            margin-bottom: 6px;
        }

        .meter-bar {
            height: 10px;
            background: #334155;
            border-radius: 5px;
            overflow: hidden;
        }

        .meter-fill {
            height: 100%;
            width: 0%;
            transition: width 0.5s ease;
        }

        .analysis-list {
            list-style: none;
            margin-top: 16px;
            font-size: 0.9rem;
            color: var(--text-sub);
        }

        .analysis-list li {
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>🛡️ AI Phishing Shield</h1>
        <p>Paste an email message or link to analyze potential security threats.</p>
    </div>

    <div class="input-group">
        <textarea id="userInput" placeholder="Paste link or email text here... (e.g., 'Urgent: Your account is suspended! Click http://bit.ly/fake')"></textarea>
        <button onclick="analyzeText()">Analyze Content</button>
    </div>

    <div id="resultCard" class="result-card">
        <div class="result-header">
            <span id="resultTitle" style="font-size: 1.1rem; font-weight: bold;">Scan Results</span>
            <span id="statusBadge" class="status-badge">Safe</span>
        </div>

        <div class="meter-container">
            <div class="meter-label">
                <span>Phishing Risk Level</span>
                <span id="riskScore">0%</span>
            </div>
            <div class="meter-bar">
                <div id="meterFill" class="meter-fill"></div>
            </div>
        </div>

        <ul id="analysisList" class="analysis-list"></ul>
    </div>
</div>

<script>
function analyzeText() {
    const input = document.getElementById('userInput').value.trim();
    const resultCard = document.getElementById('resultCard');
    const statusBadge = document.getElementById('statusBadge');
    const riskScore = document.getElementById('riskScore');
    const meterFill = document.getElementById('meterFill');
    const analysisList = document.getElementById('analysisList');

    if (!input) {
        alert("Please paste some text or a link to analyze.");
        return;
    }

    // Heuristic analysis logic (Client-side simulation)
    let score = 0;
    let flags = [];

    // Check for suspicious patterns
    if (/urgent|immediately|action required|verify now|suspended/i.test(input)) {
        score += 35;
        flags.push("⚠️ High-urgency/coercive language detected.");
    }
    if (/bit\.ly|tinyurl|goo\.gl|t\.co|is\.gd/i.test(input)) {
        score += 30;
        flags.push("⚠️ Shortened URL detected (hides true destination).");
    }
    if (/http:\/\//i.test(input)) {
        score += 20;
        flags.push("⚠️ Unencrypted connection (HTTP instead of HTTPS).");
    }
    if (/password|ssn|credit card|login|bank/i.test(input)) {
        score += 15;
        flags.push("⚠️ Sensitive information request detected.");
    }

    // Display updates
    resultCard.style.display = 'block';
    riskScore.textContent = `${score}%`;
    meterFill.style.width = `${score}%`;

    analysisList.innerHTML = '';
    if (flags.length === 0) {
        flags.push("✅ No obvious suspicious patterns detected.");
    }
    
    flags.forEach(flag => {
        const li = document.createElement('li');
        li.textContent = flag;
        analysisList.appendChild(li);
    });

    // Update styling based on risk score
    if (score >= 50) {
        statusBadge.textContent = "High Risk";
        statusBadge.className = "status-badge danger";
        meterFill.style.backgroundColor = "var(--danger-color)";
    } else if (score > 20) {
        statusBadge.textContent = "Moderate Risk";
        statusBadge.className = "status-badge danger";
        meterFill.style.backgroundColor = "var(--warning-color)";
    } else {
        statusBadge.textContent = "Likely Safe";
        statusBadge.className = "status-badge safe";
        meterFill.style.backgroundColor = "var(--safe-color)";
    }
}
</script>

</body>
</html>

