from SentenceReadingAgent import SentenceReadingAgent


def test():
    # This will test your SentenceReadingAgent
    # with nine initial test cases.

    test_agent = SentenceReadingAgent()

    sentence_1 = "Ada brought a short note to Irene."
    question_1 = "Who brought the note?"
    question_2 = "What did Ada bring?"
    question_3 = "Who did Ada bring the note to?"
    question_4 = "How long was the note?"

    sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
    question_5 = "Who does Lucy go to school with?"
    question_6 = "Where do David and Lucy go?"
    question_7 = "How far do David and Lucy walk?"
    question_8 = "How do David and Lucy get to school?"
    question_9 = "At what time do David and Lucy walk to school?"

    print(test_agent.solve(sentence_1, question_1))  # "Ada"
    print(test_agent.solve(sentence_1, question_2))  # "note" or "a note"
    print(test_agent.solve(sentence_1, question_3))  # "Irene"
    print(test_agent.solve(sentence_1, question_4))  # "short"
    #
    print(test_agent.solve(sentence_2, question_5))  # "David"
    print(test_agent.solve(sentence_2, question_6))  # "school"
    print(test_agent.solve(sentence_2, question_7))  # "mile" or "a mile"
    print(test_agent.solve(sentence_2, question_8))  # "walk"
    print(test_agent.solve(sentence_2, question_9))  # "8:00AM"

    sentence_3 = "There are a thousand children in this town."
    question_10 = "How many children are in this town?"
    print(test_agent.solve(sentence_3, question_10))  # "thousand"

    sentence_4 = "The white dog and the blue horse play together."
    question_11 = "What color is the horse?"
    print(test_agent.solve(sentence_4, question_11))  # "blue"

    sentence_5 = "The red fish is in the river."
    question_12 = "What color is the fish?"
    print(test_agent.solve(sentence_5, question_12))  # "red"

    sentence_6 = "The island is east of the city."
    question_13 = "What is east of the city?"
    question_132 = "Where is the island?"
    print(test_agent.solve(sentence_6, question_13))  # "island"
    print(test_agent.solve(sentence_6, question_132))  # "city"

    sentence_7 = "There are one hundred adults in that city."
    question_14 = "How many adults are in this city?"
    print(test_agent.solve(sentence_7, question_14))  # "hundred"

    sentence_8 = "The blue bird will sing in the morning."
    question_15 = "When will the bird sing?" # morning
    print(test_agent.solve(sentence_8, question_15))  # "morning"

    sentence_9 = "The water is blue."
    question_16 = "What color is the water?"
    print(test_agent.solve(sentence_9, question_16))  # "blue"

    sentence_10 = "She told her friend a story."
    question_17 = "Who told a story?"
    print(test_agent.solve(sentence_10, question_17))  # "friend"

    sentence_11 = "Serena and Ada took the blue rock to the street."
    question_18 = "What was blue?"
    print(test_agent.solve(sentence_11, question_18))  # "rock"

    sentence_12 = "It will snow soon"
    question_19 = "When will it snow?"
    print(test_agent.solve(sentence_12, question_19))  # "rock"

    sentence_13 = "My dog Red is very large"
    question_20 = "What is my dog's name?"
    print(test_agent.solve(sentence_13, question_20))  # "Red"

    sentence_14 = "Lucy will write a book"
    question_21 = "What will Lucy do?"
    print(test_agent.solve(sentence_14, question_21))  # "write"

    sentence_15 = "Frank took the horse to the farm."
    question_22 = "Where did the horse go?"
    print(test_agent.solve(sentence_15, question_22))  # "farm"

    sentence_16 = "Bring the box to the other room."
    question_23 = "Where should the box go?"
    print(test_agent.solve(sentence_16, question_23))  # "farm"

    sentence_13 = "My dog Red is very large"
    question_20 = "What animal is Red?"
    print(test_agent.solve(sentence_13, question_20))  # "dog"

    sentence_14 = "She will write him a love letter."
    question_21 = "What will she write to him?"
    print(test_agent.solve(sentence_14, question_21))  # "dog"

    sentence_19 = "Give us all your money."
    question_27 = "How much of your money should you give us?"
    print(test_agent.solve(sentence_19, question_27))  # "dog"

    sentence_20 = "This year David will watch a play."
    question_28 = "What will David watch?"
    print(test_agent.solve(sentence_20, question_28))  # "dog"

    sentence_21 = "Give us all your money."
    question_29 = "Who should you give your money to?"
    print(test_agent.solve(sentence_21, question_29))  # "dog"

    sentence_22 = "Serena saw a home last night with her friend."
    question_30 = "Who was with Serena?"
    print(test_agent.solve(sentence_22, question_30))  # "dog"

if __name__ == "__main__":
    test()
