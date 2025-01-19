import requests
import PySimpleGUI as sg

# Constants for OAuth and API
CLIENT_ID = None
CLIENT_SECRET = None
ACCESS_TOKEN = None
API_BASE_URL = "https://api.github.com"

# Prompt user for input (with PySimpleGUI)
def prompt_user(title, message, default_text=""):
    layout = [
        [sg.Text(message)],
        [sg.InputText(default_text, key="input")],
        [sg.Button("OK"), sg.Button("Cancel")]
    ]
    window = sg.Window(title, layout)
    event, values = window.read()
    window.close()

    if event == "OK":
        return values["input"]
    return None

# Display error alert
def display_error(title, message):
    sg.popup_error(message, title=title)

# Display confirmation popup
def confirm_action(title, message):
    return sg.popup_yes_no(message, title=title) == "Yes"

# Exchange code for an access token
def exchange_code_for_token(code):
    global ACCESS_TOKEN
    url = "https://github.com/login/oauth/access_token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code
    }
    headers = {"Accept": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        ACCESS_TOKEN = response.json().get("access_token")
    else:
        display_error("Error", f"Failed to fetch access token: {response.text}")

# Create a gist
def create_gist(filename, content, description, public):
    url = f"{API_BASE_URL}/gists"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json"
    }
    payload = {
        "description": description,
        "public": public,
        "files": {
            filename: {"content": content}
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        gist_url = response.json().get("html_url")
        sg.popup(f"Gist created successfully: {gist_url}", title="Success")
    else:
        display_error("Error", f"Failed to create gist: {response.text}")

# Main workflow
def main():
    global CLIENT_ID, CLIENT_SECRET

    sg.theme("DarkBlue3")

    CLIENT_ID = prompt_user("GitHub OAuth", "Enter your GitHub OAuth App Client ID:")
    CLIENT_SECRET = prompt_user("GitHub OAuth", "Enter your GitHub OAuth App Client Secret:")

    if not CLIENT_ID or not CLIENT_SECRET:
        display_error("Error", "Client ID and Client Secret are required.")
        return

    # Simulate OAuth flow
    code = prompt_user("GitHub OAuth", "Enter the code received from GitHub after authorization:")
    if code:
        exchange_code_for_token(code)
    else:
        display_error("Error", "Authorization code is required.")
        return

    if ACCESS_TOKEN:
        filename = prompt_user("Gist File", "Enter the file name for your Gist:")
        content = prompt_user("Gist Content", "Enter the content of your Gist:")
        description = prompt_user("Gist Description", "Enter a description for your Gist:")
        public = confirm_action("Gist Visibility", "Make the Gist public?")

        if filename and content and description:
            create_gist(filename, content, description, public)
        else:
            display_error("Error", "All fields are required to create a Gist.")
    else:
        display_error("Error", "Failed to obtain access token.")

if __name__ == "__main__":
    main()
