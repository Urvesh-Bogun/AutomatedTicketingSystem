import requests
import json

# Freshdesk API details
FRESHDESK_DOMAIN = "liverhulac.freshdesk.com" 
FRESHDESK_API_KEY = "3vCpw1Xp4NId0h74gvvM"

# Slack Webhook URL
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

# Fetch tickets from Freshdesk
def fetch_freshdesk_tickets():
    url = f"https://{FRESHDESK_DOMAIN}/api/v2/tickets"
    headers = {
        "Content-Type": "application/json",
    }
    auth = (FRESHDESK_API_KEY, "X")  # Freshdesk API uses API_KEY:X for authentication
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching tickets: {response.status_code} - {response.text}")
        return []

# Send notification to Slack
def send_slack_notification(message):
    payload = {
        "text": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("Notification sent to Slack!")
    else:
        print(f"Error sending message to Slack: {response.status_code} - {response.text}")

# Main function
def main():
    tickets = fetch_freshdesk_tickets()
    if tickets:
        for ticket in tickets:
            ticket_id = ticket["id"]
            subject = ticket["subject"]
            status = ticket["status"]
            priority = ticket["priority"]
            message = f"New Ticket! 🎫\nID: {ticket_id}\nSubject: {subject}\nStatus: {status}\nPriority: {priority}"
            send_slack_notification(message)
    else:
        print("No new tickets found.")

if __name__ == "__main__":
    main()