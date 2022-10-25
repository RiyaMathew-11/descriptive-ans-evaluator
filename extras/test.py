import pandas as pd
from config import new_path, save_path
from sentence_sim import preprocess, Jaccard_Similarity, answer_score

final_data = pd.DataFrame(columns=['Question', 'Model_Answer',
                          'User_Answer', 'Jaccard_Score', 'Answer_Score'])

data = pd.read_csv(new_path)

print("\n\nThe questions are : ")
for i in range(len(data.Question)):
    print("\nQuestion.", i+1, ":", data.Question[i],".....done")

    doc1 = preprocess(data.Model_Answer[i])

    doc2 = preprocess(data.User_Answer[i])

    j_index = Jaccard_Similarity(doc1, doc2)
    ans_score  = answer_score(j_index)
    
    row_data = pd.DataFrame({"Question": [data.Question[i]],
                             "Model_Answer": [data.Model_Answer[i]],
                             "User_Answer": [data.User_Answer[i]],
                             "Jaccard_Score": [round(j_index, 2)],
                             "Answer_Score": [ans_score]})
    
    print(row_data.head())
    final_data = pd.concat([final_data, row_data], axis=0)
    print(final_data.head())
    

final_data.to_csv(save_path)

print("\n All done")

