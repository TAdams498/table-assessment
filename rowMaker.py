import pyperclip

startStr = "<td>"
endStr = "</td>"
x = input()
data = x.replace(" ", "</td>\n<td>")
print(startStr + data + endStr)

pyperclip.copy(startStr + data + endStr)