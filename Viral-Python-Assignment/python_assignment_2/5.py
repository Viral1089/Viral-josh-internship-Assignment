"""Create a file hash.txt with some content. Append '#' to every next character and display the content on screen.​
Example :​
If the file hash.txt has the following content stored in it :​
THE WORLD IS NOT FLAT​

Your code should display the following content :​
T#H#E# #W#O#R#L#D# #I#S# #N#O#T# F#L#A#T#
"""

with open("hash.txt",'w') as f:
  f.write("THE WORLD IS NOT FLAT")
  
with open("hash.txt",'r') as f:
   content = f.read()
   hashoutput = "#".join(content)

print(hashoutput)