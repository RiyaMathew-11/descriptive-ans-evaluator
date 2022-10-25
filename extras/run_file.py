import pandas as pd
from config import csv_path
from sentence_sim import preprocess,Jaccard_Similarity, answer_score

data = pd.read_csv(csv_path)

print("\n\nThe questions are : ")
for i in range(3,4):
    print("\nQuestion.",i+1, ":", data.Question[i])
    
    doc1 = preprocess(data.Model_Answer[i])

    user_answer = input("Enter your answer: ")
    
    doc2 = preprocess(user_answer)
    
    index = Jaccard_Similarity(doc1, doc2)
    
    print("\nJaccard score = ", round(index, 3))
    
    print("\nAnswer score = ", answer_score(index))
    
    
    
    
    



