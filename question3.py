#  Grade Average Calculator

def calculate_average(scores):
    average = (sum(scores)/len(scores))
    return average

def get_letter_grade(average):
    if 90 <= average <= 100:
        return "A"
    elif 80 <= average <= 89:
        return "B"
    elif 70 <= average <= 79:
        return "C"
    elif 60 <= average <= 69:
        return "D"
    elif 0 <= average <= 59:
        return "F"
    else:
        return "Average is out of range...!"

def main():
    print("main")
    scores_list = []
    counter = 1
    number_of_scores = 0
    try:
        number_of_scores = int(input("How many test scores do you want to enter? "))
        if number_of_scores == 0:
            print("Number of scores can not be 0! try again...")
            main()
        while counter <= number_of_scores:
            score = float(input(f"Enter score {counter}: "))
            if 0 <= score <= 100:
                scores_list.append(score)
                counter += 1
            else:
                print("Score has to be between 0 to 100! try again... ")
                continue
    except ValueError:
        print("Enter a valid number...! try again! ")
        scores_list = []
        main()
        
    if scores_list != [] and number_of_scores > 0:
        average = calculate_average(scores_list)
        letter_grade =  get_letter_grade(average)
        print("=== GRADE REPORT ===")
        print("Test Scores: ", scores_list)
        print(f"Average Score: {average:.2f}")
        print("Letter Grade: ", letter_grade)

main()