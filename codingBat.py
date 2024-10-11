#Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
  shorter = a if len(a) < len(b) else b
  longer = b if len(a) < len(b) else a
  return shorter + longer + shorter


#The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"



#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
def extra_end(str):
  last_two = str[-2:]
  result = ""
  for i in range(3):
   result += last_two
  return result

#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
  result = ""
  for i in range(n):
    result += str
  return result
