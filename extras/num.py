import numpy as np

def jaccard_num(a, b):
# Calculate the Jaccard distance between two sets of numbers.
    intersection = np.logical_and(a, b)
    union = np.logical_or(a, b)
    
    similarity = intersection.sum() / float(union.sum())
    return similarity

# Some vectors - customers in a store case 

'''
	item1	item2	item2	item4	item5	item6	item7	item8	item9
C1	    0	    1	    0	    0	    0	    1	    0	    0	    1
C2	    0	    0	    1	    0	    0	    0	    0	    0	    1
C3	    1	    1	    0	    0	    0   	1	    0	    0	    0

'''
v1 = [0, 1, 0, 0, 0, 1, 0, 0, 1]
v2 = [0, 0, 1, 0, 0, 0, 0, 0, 1]
v3 = [1, 1, 0, 0, 0, 1, 0, 0, 0]

sim_v1_v2 = jaccard_num(v1, v2)
sim_v1_v3 = jaccard_num(v1, v3)
sim_v2_v3 = jaccard_num(v2, v3)

print(' Similarity between v1 and v2 is', sim_v1_v2, '\n Similarity between v1 and v3 is ',
      sim_v1_v3, '\n Similarity between v2 and v3 is ', sim_v2_v3)
