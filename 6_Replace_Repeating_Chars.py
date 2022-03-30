text_line = input()
result_text = ""

for i in range(len(text_line)):
    if i == 0:
        result_text += text_line[i]
    if not text_line[i] == result_text[-1] and i != 0:
        result_text += text_line[i]

print(result_text)
