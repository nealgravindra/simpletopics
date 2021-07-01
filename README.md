# simpletopics
composite scores for indexed descriptions to target document(s)

## ideas
1. one question is how to construct good priors and the idea here is to evaluate the model based on scientific knowledge priors, which can get complicated, depending on the lang model used. This will allow one to at least satisfy hill's criterion of consistency w.r.t. causal knowledge, at least complementing hidden structure coherently
2. bleed into training (as reg?)? or is this a terrible idea... could avoid mode collapse issues if done carefully

## experiments
1. see if this can be done with a kind of hyperfoods heuristic, i.e., get simpletopics up and running

## results
1. wtf should this look like? at least have modules for parsing .xml description text and full literature, have a comparison of sensibility between topics by trying review -> description para and vice versa, and store these steps somewhere. Post distillation here
