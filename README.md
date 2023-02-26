# Marinara_to_Habitica

Python script that imports ["Marinara: Pomodoro Assistant"](https://github.com/schmich/marinara/) history to ["Habitica Pomodoro SiteKeeper"](https://github.com/ofekmiz/Habitica-Pomodoro-SiteKeeper/).

## Steps to import Marinara history to Habitica Pomodoro SiteKeeper

1. Open "Marinara: Pomodoro Assistant" and navigate to Pomodoro history.
2. Click on "Save as CSV" to export the Pomodoro history as a CSV file.
3. Copy the exported CSV file to the same directory as the `code.py` file.
4. Run the `code.py` file using a Python interpreter. This will generate an `output.json` file.
5. Open "Habitica Pomodoro SiteKeeper" and navigate to "History" -> "Full History & Backup".
6. Click on "Choose File" and select the `output.json` file generated in step 4.
7. Click on "Import" to import the Pomodoro history from Marinara to Habitica Pomodoro SiteKeeper.
8. All done! Your Pomodoro history from Marinara should now be imported into Habitica Pomodoro SiteKeeper.

## Usage
To run the script, simply navigate to the directory where code.py is located and run the following command in your terminal:
```bash 
python code.py
```

## Dependencies
This script requires the following dependencies:
* `csv`
* `json`
* `collections` (`defaultdict`)
* `datetime`

## Support 
If you encounter any issues or have any questions, please feel free to open an issue on this repository.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

