def CamelCase(strParam):
  result = ""

  for i, char in enumerate(strParam):
        if i == 0:
            result += char
        else:
            if ((strParam[i-1].isalpha()) & (strParam[i].isalpha())):
                result += char.lower()

            elif not strParam[i-1].isalnum():
                result += char.upper()
            else:
                pass
  return result

print(CamelCase(input()))
