# Fantasy Football Player Recommendations

This app displays the best NFL players for users to pick for their teams during their fantasy football drafts. First, I used Beautiful Soup to scrape the most important stats for each position (QB, RB, WR, TE, D/ST, K) into CSV files. Then, I used these stats to calculate a "recomendation rating" for each player–each statistic is assigned a certain weight based on their importance for fantasy points and then I divided the sum of the weighted values by the sum of the weights to normalize the result. This ensures that the combined rec_rating is within a reasonable range and reflects a weighted average of the individual percentages.

Players are displayed to users from those with the highest to the lowest recommendation ratings. Note: the calculations are simplified and not based on those used by actual fantasy football sites. 

## Research
My calculations are based on the research I did using these links:
[Quarterbacks](https://www.sharpfootballanalysis.com/fantasy/quarterback-stats-that-matter-fantasy-football-2023/),
[Running Backs](https://www.sharpfootballanalysis.com/fantasy/running-back-stats-that-matter-fantasy-football-2023/),
[Wide Receivers](https://www.sharpfootballanalysis.com/fantasy/wide-receiver-stats-that-matter-fantasy-football-2023/),
[Tight Ends](https://www.sharpfootballanalysis.com/fantasy/te-stats-that-matter-fantasy-football/),
[Defense/Special Teams](https://www.lineups.com/fantasy-football-stats/defense'),
[Kickers](https://www.sharpfootballanalysis.com/fantasy/te-stats-that-matter-fantasy-football/)

## Demo
Link: https://www.youtube.com/watch?v=XnlI7SXFZvk

## List of what I used
- Python
- Flask
- Beautiful Soup
- Pandas

## How to set it up on your local machine

To run this app locally, first clone this repository to your local machine...

`git clone url-to-this-repository`

... and then do the following:

### Set up a Python virtual environment

This command creates a new virtual environment with the name `.venv`:

```bash
python3 -m venv .venv
```

#### Activate the virtual environment

To activate the virtual environment named `.venv`...

On Mac:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate.bat
```

#### Install the dependencies into the virtual environment

The file named, `requirements.txt` contains a list of dependencies - other Python modules that this app depends upon to run.

To install the dependencies into the currently-active virtual environment, use `pip`, the default Python "package manager" - software that takes care of installing the correct version of any module into your in the correct place for the current environment.

```bash
pip3 install -r requirements.txt
```

### Run the app

1. define two environment variables from the command line: on Mac, use the commands: `export FLASK_APP=app.py` and `export FLASK_ENV=development`; on Windows, use `set FLASK_APP=app.py` and `set FLASK_ENV=development`.
1. copy the file named `env.example` into a new file named `.env`, and enter your own MongoDB database connection credentials into that file where indicated.
1. start flask with `flask run` - this will output an address at which the app is running locally, e.g. https://127.0.0.1:5000. Visit that address in a web browser.
1. in some cases, the command `flask` will not be found when attempting `flask run`... you can alternatively launch it with `python3 -m flask run --host=0.0.0.0 --port=10000`.