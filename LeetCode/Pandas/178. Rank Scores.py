import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
   scores['rank'] = scores[['score']].rank(method='dense', ascending=False)
   scores.sort_values('rank', inplace=True)

   
   return scores[['score', 'rank']]