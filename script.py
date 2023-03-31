
import re
txt = """

"""
headerPattern = r'^\d\.\d\.\d+ '
subheaderPattern = r'^\d\.\d\.\d..\d.'

headerArray = re.findall(headerPattern, txt, re.MULTILINE)
subheaderArray = re.findall(subheaderPattern, txt, re.MULTILINE)

print(subheaderArray)
for header in headerArray:
    txt = re.sub(header,"\n### " + header, txt)
for subheader in subheaderArray:
    txt = re.sub(subheader,("\n**" + subheader + "**").replace(" ",""), txt)

print(txt)
