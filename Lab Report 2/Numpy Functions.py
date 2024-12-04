import numpy as np

def calculate_average_scores(scores):
    
    average_scores = np.mean(scores, axis=1)
    return average_scores

def find_highest_average(scores):
   
    average_scores = calculate_average_scores(scores)
    highest_average_index = np.argmax(average_scores)
    highest_average_score = average_scores[highest_average_index]
    return highest_average_index, highest_average_score

# Example usage:
student_scores = np.array([[85, 90, 78],
                           [92, 88, 95],
                           [85, 82, 80]])

average_scores = calculate_average_scores(student_scores)
print("Average scores for each student:", average_scores)

highest_index, highest_score = find_highest_average(student_scores)
print(f"Student with the highest average score (index {highest_index}): {highest_score}")