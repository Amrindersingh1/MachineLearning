import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

data = fetch_movielens(min_rating=4.0)

print(repr(data['train']))
print(repe(data['test']))

model = LightFM(loss='warp')

model.fit(data['train'], epachs=30, num_threads=2)

def sample_recommends(model, data, user_ids):
	n_user,n_items = data['train'].shape

	for user_id in user_ids:

		known_positives = data['item_labels'][data['train']].tocsr()[user_id].indices]

		scores = model.pred