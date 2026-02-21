text = {"CU" : "see you", ":-)" : "I’m happy", ":-(" : "I’m unhappy", ";-)" : "wink",
            ":-P" : "stick out my tongue", "(~.~)" : "sleepy", "TA" : "totally awesome",
            "CCC" : "Canadian Computing Competition", "CUZ" : "because", "TY" : "thank-you",
            "YW" : "you’re welcome", "TTYL" : "talk to you later"}

while 1:
    word = input()

    if word in text:
        print(text[word])
        if word == "TTYL":
            break
    else:
        print(word)