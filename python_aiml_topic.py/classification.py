def classify_marks(marks):
    result = []
    
    for m in marks:
        if m >= 33:
            result.append('pass')
        else:
            result.append('fail')
    
    return result


def movie_result(budget,collection):
    profit = collection-budget
    profit_per = (profit/budget)*100
    result = []
    if profit<=0:
        return 'flop'
    elif profit_per <= 50:
        return 'hit'
    else:
        return 'superhit'
    
    




# Classify of marks
# marks=[10,20,50,33,20]
# output = classify_marks(marks)
# print(output)

#classify of movies result

print(movie_result(8000,10000))
print(movie_result(4000,2000))
print(movie_result(8000,18000))



