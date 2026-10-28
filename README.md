# Wikipedia Search

A small Flask app that searches Wikipedia and displays a two-sentence summary.

## Run locally

1. Install [Python 3.10 or newer](https://www.python.org/downloads/).
2. Clone this repository and open a terminal in the project folder.
3. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, run `.\.venv\Scripts\activate.bat` from Command Prompt instead.

4. Install the project dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the development server:

   ```powershell
   python app.py
   ```

6. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

The app needs an internet connection to retrieve summaries from Wikipedia.

## Search behavior

Enter a topic in the search box to see a short summary. If a term has multiple meanings, the app offers suggested topics; if no matching page is found or Wikipedia is unavailable, it displays an explanatory message.
