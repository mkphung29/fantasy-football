# Fantasy Football Player Recommendations

This app displays the best NFL players for users to pick for their teams during their fantasy football drafts. First, I used Beautiful Soup to scrape the most important stats for each position (QB, RB, WR, TE, D/ST, K) into CSV files. Then, I used these stats to calculate a "recomendation rating" for each player–each statistic is assigned a certain weight based on their importance for fantasy points and then I divided the sum of the weighted values by the sum of the weights to normalize the result. This ensures that the combined rec_rating is within a reasonable range and reflects a weighted average of the individual percentages.

Players are displayed to users from those with the highest to the lowest recommendation ratings. Note: the calculations are simplified and not based on those used by actual fantasy football sites. 

## Research
My calculations are based on the research I did using these links:
[Quarterbacks]('https://www.sharpfootballanalysis.com/fantasy/quarterback-stats-that-matter-fantasy-football-2023/')
[Running Backs]('https://www.sharpfootballanalysis.com/fantasy/running-back-stats-that-matter-fantasy-football-2023/')
[Wide Receivers]('https://www.sharpfootballanalysis.com/fantasy/wide-receiver-stats-that-matter-fantasy-football-2023/')
[Tight Ends]('https://www.sharpfootballanalysis.com/fantasy/te-stats-that-matter-fantasy-football/')
[Defense/Special Teams]('https://www.lineups.com/fantasy-football-stats/defense')
[Kickers]('https://www.sharpfootballanalysis.com/fantasy/te-stats-that-matter-fantasy-football/')

## Usage
This website is deployed to Netlify. Here is the link to access it: 

## List of what I used
- Python
- Flask
- Beautiful Soup
- Pandas