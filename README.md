
# GitHub Gist Manager

A Python-based tool to create, update, and manage GitHub Gists using the GitHub API. The tool uses **PySimpleGUI** for an intuitive graphical interface.

## Features
- Authenticate with GitHub using OAuth.
- Create new Gists with custom filenames, descriptions, and content.
- Choose between public and private Gists.
- User-friendly GUI with **PySimpleGUI**.
- Manage access credentials securely.

## Requirements
- Python 3.7 or later.
- The following7779
 Python libraries:
  - `requests`
  - `PySimpleGUI`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/d3vn0o6/PyGistManager.git PyGistManager
   cd PyGistManager
   ```
  2. Create virtual environment:
   ```bash
  python3 -m venv 
  

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Follow the prompts to:
   - Enter your GitHub OAuth App credentials.
   - Authenticate with GitHub.
   - Create, update, or manage Gists.

3. After completing the workflow, your Gist link will be displayed.

## How to Create a GitHub OAuth App

To use this tool, you need to configure an OAuth App on GitHub:
1. Go to [GitHub Developer Settings](https://github.com/settings/developers).
2. Under "OAuth Apps," click **New OAuth App**.
3. Enter the required details:
   - **Application name**: Any name you prefer.
   - **Homepage URL**: Any valid URL.
   - **Authorization callback URL**: `http://localhost` (or customize for your needs).
4. Copy the **Client ID** and **Client Secret** after creating the app.

## Example Workflow

1. **Start the tool**:  
   Launch the script and provide your GitHub OAuth App credentials.

2. **Authenticate**:  
   Enter the authorization code received after GitHub's authentication.

3. **Create Gists**:  
   Enter a filename, content, description, and choose visibility (public or private).

4. **View Results**:  
   A link to your created Gist will be displayed upon success.

## Screenshots

### Main Interface
![Main Interface](https://via.placeholder.com/800x400.png?text=Screenshot+of+Main+Interface)

### Gist Creation
![Gist Creation](https://via.placeholder.com/800x400.png?text=Screenshot+of+Gist+Creation)

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

