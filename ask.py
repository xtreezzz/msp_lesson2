def ask_user(_request_question=None):
    if _request_question:
        while True:
            lib_answer = {"Как дела?": "Хорошо!",
                          "Что делаешь?":
                              "Программирую",
                          "Как мне выйти из цикла?":
                              "Спросить меня 'Как мне выйти из цикла?'",
                          "Как мне выйти из VIM?":
                              ":q!"}
            if lib_answer.get(_request_question, 'Wrong') == 'Wrong':
                _request_question \
                    = input('Так интересно, спроси меня что-нибудь ещё! ')
            else:
                print(lib_answer[_request_question])
                break
    else:
        while True:
            answer = input("Как дела? ")
            if answer == 'Хорошо':
                break


ask_user()
request_question = input("Задай мне вопрос: ")
ask_user(request_question)
