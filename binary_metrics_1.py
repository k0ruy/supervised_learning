if __name__ == '__main__':
    true_positive: int = int(input("Real: Positive,  Predicted: Positive (TP): "))
    true_negative: int = int(input("Real: Negative, Predicted: Negative (TN): "))
    false_negative: int = int(input("Real: Positive, Predicted: Negative (FN): "))
    false_positive: int = int(input("Real: Negative, Predicted: Positive (FP): "))

    samples = true_negative + true_positive + false_positive + false_negative
    accuracy = (true_positive + true_negative) / samples
    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    f_score = 2 * ((precision * recall)/(precision + recall))
    # also equal to true_positive / (true_positive + 0.5*(false_positive + false_negative))

    print(f'{samples=}')
    print(f'{accuracy=}')
    print(f'{precision=}')
    print(f'{recall=}')
    print(f'{f_score=}')
