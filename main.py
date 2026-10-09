
import json
import os
import urllib.request

def send_telegram_message():
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    message = (
        "UNQ Quarterly Theory Report Bot\n\n"
        "Telegram connection test successful!\n\n"
        "Next setup: XAUUSD/XAGUSD market data, "
        "AMDX/XAMD classification, SSMT, and scheduled reports."
    )

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = json.dumps({
        "chat_id": chat_id,
        "text": message
    }).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        result = json.loads(response.read().decode("utf-8"))

    if not result.get("ok"):
        raise RuntimeError("Telegram could not send the test message.")

    print("Telegram test message sent successfully.")

if __name__ == "__main__":
    send_telegram_message()
