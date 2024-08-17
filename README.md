# Automate Search with Python 
 
This project includes scripts to perform Google searches using different browsers. 
 
## Requirements 
- Python 3.x 
- `selenium` and `webdriver-manager` libraries 
 
Install the required libraries using: 
```bash 
pip install selenium webdriver-manager 
``` 
 
## Scripts 
 
### `search_chrome.py` 
Runs the search script using Google Chrome. Run the script with: 
```bash 
python chrome/search_chrome.py "<search_query>" 
```
 
### `search_firefox.py` 
Runs the search script using Mozilla Firefox. Run the script with: 
```bash 
python firefox/search_firefox.py "<search_query>" 
``` 
 
### `search_edge.py` 
Runs the search script using Microsoft Edge. Run the script with: 
```bash 
python edge/search_edge.py "<search_query>" 
``` 
 
## Logging 
Logs are saved in `search_script.log`. 
