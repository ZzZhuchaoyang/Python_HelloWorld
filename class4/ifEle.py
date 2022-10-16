# score = 66
# text = "the student's score is: {} {}"
#
# # isA = score >= 90
# # isB = 80 <= score < 90
# # isC = 60 <= score < 80
#
# # if isA:
# #     print(text.format(score, "A"))
# # else:
# #     print("学生的成绩不是A")
# #     if isB:
# #         print(text.format(score, "B"))
#
# # else if
# if score >= 90:
#     print(text.format(score, "A"))
# elif 80 <= score < 90:
#     print(text.format(score, "B"))
# elif 60 <= score < 80:
#     print(text.format(score, "C"))
# else:print(text.format(score, "D"))


def printScoreFunction(score):
    text = "the student's score is: {} {}"
    if score >= 90:
        print(text.format(score, "A"))
    elif 80 <= score < 90:
        print(text.format(score, "B"))
    elif 60 <= score < 80:
        print(text.format(score, "C"))
    else:
        print(text.format(score, "D"))


def getScoreFunction(score):
    text = "the student's score is: {} {}"
    if score >= 90:
        return text.format(score, "A")
    elif 80 <= score < 90:
        return text.format(score, "B")
    elif 60 <= score < 80:
        return text.format(score, "C")
    else:
        return text.format(score, "D")

# printScoreFunction(60)
# printScoreFunction(90)
# printScoreFunction(80)
#
# stdAScoreComment = getScoreFunction(95)