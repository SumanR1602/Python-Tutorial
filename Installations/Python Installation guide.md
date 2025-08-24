# How to Install Python and Use It with VS Code on a Laptop (Windows)

## 1. Download Python

- Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Click the "Download Python" button (choose the latest version).

## 2. Run the Installer

- Locate the downloaded file (usually in your Downloads folder).
- Double-click the installer (e.g., `python-3.x.x.exe`).

## 3. Install Python

- On the installer window, **check the box that says "Add Python to PATH"** (very important).
- Click **Install Now**.
- Wait for the installation to finish.
- Click **Close** when done.

## 4. Manually Add Python to Environment Variables (if needed)

If you forgot to check "Add Python to PATH" during installation:

- Press `Win + S` and type **Environment Variables**, then select **Edit the system environment variables**.
- In the System Properties window, click **Environment Variables…**.
- Under **System variables**, find and select **Path**, then click **Edit**.
- Click **New** and add the following (adjust version number to your installed Python version):

  ```
  C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python3x\
  C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python3x\Scripts\
  ```

- Click **OK** on all windows to save changes.
- Restart Command Prompt.

## 5. Verify Python Installation

- Open the **Command Prompt** (press `Win + R`, type `cmd`, and press Enter).
- Type:
  ```
  python --version
  ```
- You should see the installed Python version.

## 6. Install VS Code (if not already installed)

- Follow the steps in the "VS Code installation" guide.

## 7. Install the Python Extension in VS Code

- Open VS Code.
- Go to the Extensions view (click the square icon on the sidebar or press `Ctrl+Shift+X`).
- Search for **Python** and install the extension by Microsoft.

## 8. (Optional) Install the Code Runner Extension

The Code Runner extension makes it easier to quickly run Python (and many other) files with one click.

- In VS Code, go to Extensions (`Ctrl+Shift+X`).
- Search for **Code Runner** (by Jun Han).
- Click **Install**.
- To run a Python file, right-click inside the editor and choose **Run Code**, or press `Ctrl+Alt+N`.

## 9. Create and Run a Python File in VS Code

- Open a folder or create a new file with a `.py` extension (e.g., `hello.py`).
- Write your Python code, for example:
  ```python
  print("Hello, world!")
  ```
- Save the file.
- To run:
  - With the Python extension: Right-click and select **Run Python File in Terminal**.
  - With Code Runner: Right-click and select **Run Code**, or press `Ctrl+Alt+N`.

## 10. See the Output

- The output will appear in the terminal at the bottom of VS Code.

> **Tip:** You can install additional Python packages using the terminal with `pip install package_name`.