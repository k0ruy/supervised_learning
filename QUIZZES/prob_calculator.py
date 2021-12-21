from fractions import Fraction


def get_prob_dict(column):
    return {i: Fraction(column.count(i), len(column)) for i in column}


def prob_given(column_a, column_b, a: str, b: str):
    count = 0
    for i in range(len(column_a)):
        if column_a[i] == a and column_b[i] == b:
            count += 1
    prob_dict = get_prob_dict(column_b)
    return Fraction(Fraction(count, len(column_a)), prob_dict[b])


def main():
    weather = ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny',
               'Rainy', 'Sunny', 'Overcast', 'Rainy']
    temperature = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool',
                   'Mild', 'Mild', 'Hot', 'Mild']
    play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

    prob_weather = get_prob_dict(weather)
    prob_temperature = get_prob_dict(temperature)
    prob_play = get_prob_dict(play)

    for key, i in prob_weather.items():
        print(f"p({key}) = {i}")
    for key, i in prob_temperature.items():
        print(f"p({key}) = {i}")
    for key, i in prob_play.items():
        print(f"p({key}) = {i}")

    print(f"p(Sunny|Hot) = {prob_given(weather, temperature, 'Sunny', 'Hot')}")
    print(f"p(Hot|Sunny) = {prob_given(temperature, weather, 'Hot', 'Sunny')}")

    print(f"p(Play|hot,rainy) = {prob_given(weather, play, 'Rainy', 'Yes')*prob_given(temperature, play, 'Hot','Yes')*prob_play['Yes']}")
    print(f"p(No Play|Overcast,Mild) = {prob_given(weather, play, 'Overcast', 'No')*prob_given(temperature, play, 'Mild','No')*prob_play['No']}")


if __name__ == '__main__':
    main()


