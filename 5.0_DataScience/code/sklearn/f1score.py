# The F1 score can be interpreted as a weighted average of the precision and recall, where an F1 score reaches its best value at 1 and worst score at 0. The relative contribution of precision and recall to the F1 score are equal. The formula for the F1 score is:

# F1 = 2 * (precision * recall) / (precision + recall)

from sklearn.metrics import f1_score

y_true = [0, 1, 2, 0, 1, 2]
y_prd = [0, 2, 1, 0, 0, 1]
f11 = f1_score(y_true, y_prd, average='macro')
print(f11)
f1_score(y_true, y_prd, average='micro')

f1_score(y_true, y_prd, average='weighted')

f1_score(y_true, y_prd, average=None)

# array([ 0.8,  0. ,  0. ])
