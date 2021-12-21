if __name__ == '__main__':
    n = int(input("Number of classes: "))
    matrix = []
    row = []
    for i in range(n):
        for j in range(n):
            row.append(int(input(f'{i}, {j}:')))
        matrix.append(row)
        row = []
    print(matrix)

    num_accuracy = 0
    for i in range(n):
        for j in range(n):
            if i==j:
                num_accuracy += matrix[i][j]

    denum_accuracy = 0
    for i in range(n):
        for j in range(n):
            denum_accuracy += matrix[i][j]

    accuracy = num_accuracy / denum_accuracy
    print(f'accuracy: {accuracy}')

    precision = []
    for i in range(n):
        denum_precision = 0
        for j in range(n):
            denum_precision += matrix[i][j]
        precision.append(matrix[i][i]/denum_precision)

    for i in range(n):
        print(f'precision class {i}: {precision[i]}')

    recall = []
    for i in range(n):
        denum_recall = 0
        for j in range(n):
            denum_recall += matrix[j][i]
        recall.append(matrix[i][i] / denum_recall)

    for i in range(n):
        print(f'recall class {i}: {recall[i]}')


    f_score = []
    for i in range(n):
        f_score.append(2 * ((precision[i] * recall[i]) / (precision[i] + recall[i])))
    for i in range(n):
        print(f'f-score class {i}: {f_score[i]}')
