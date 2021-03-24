from xml.etree import cElementTree as ElementTree
from lxml import etree
import codecs
import html2text
import warnings

parser2 = html2text.HTML2Text()
#parser2.unicode_snob = True
#parser2.escape_snob = False
parser2.re_slash_chars = False
#parser2.asdsadasdasda = True

def fxn():
    warnings.warn("deprecated", DeprecationWarning)


def parser(data, tags):
    tree = ElementTree.iterparse(data)
    
    for event, node in tree:
        if node.tag in tags:
            yield node.tag, node.text


tree = ElementTree.parse('D:\TestXML.xml')
root = tree.getroot()
#print(root)
for child in root:
    print(child)

for node in tree.findall('.//name'):   
    warnings.filterwarnings("ignore")
    for snode in node.getchildren():
        print('\033[93m ' + 'Question name:'+ '\033[0m',snode.text)
        name = parser2.handle(snode.text)

for node in tree.findall('.//questionvariables'):   
    warnings.filterwarnings("ignore")
    for snode in node.getchildren():
        print('\033[93m ' + 'Question variables:'+ '\033[0m',snode.text)
        qvar = snode.text
        #qvar = parser2.handle(snode.text).replace( ';', ';\n' )
       

for node in tree.findall('.//questiontext'):   
    warnings.filterwarnings("ignore")
    for snode in node.getchildren():
        print('\033[93m ' + 'Question text:'+ '\033[0m',parser2.handle(snode.text))
        qtest = parser2.handle(snode.text).replace( '\\\\', '\\' )
        

for node in tree.findall('.//specificfeedback'):   
    warnings.filterwarnings("ignore")
    for snode in node.getchildren():
        print('\033[93m ' + 'Specific feedback:'+ '\033[0m',html2text.html2text(snode.text))
        sfeedback = html2text.html2text(snode.text)

for node in tree.findall('.//generalfeedback'):   
    warnings.filterwarnings("ignore")
    for snode in node.getchildren():
        print('\033[93m ' + 'General feedback:'+ '\033[0m',parser2.handle(snode.text))
        gfeedback = parser2.handle(snode.text).replace( '\\\\', '\\' )
'''
with open('D:\TestXML.xml', 'r') as myFile:
    results = parser(myFile, {'questiontext'})
    for tag, text in results:
        print('\033[93m '+ tag + '\033[0m', text)
 
'''
for node in tree.findall('.//questionnote'):   
    warnings.filterwarnings("ignore")
    for snode in node.getchildren():
        print('\033[93m ' + 'Question Note:'+ '\033[0m',html2text.html2text(snode.text))
        qnote = html2text.html2text(snode.text)
ansname = []
tans = []
boxsize = []
for node in tree.findall('.//input'):   
    warnings.filterwarnings("ignore")
    for node2 in node.findall('.//name') :
        print('\033[93m ' + 'name:'+ '\033[0m',html2text.html2text(node2.text).rstrip("\n")) 
        ansname.append(html2text.html2text(node2.text).rstrip("\n"))       
    for node2 in node.findall('.//tans') :
        print('\033[93m ' + 'tans:'+ '\033[0m',html2text.html2text(node2.text).rstrip("\n"))        
        tans.append(html2text.html2text(node2.text).rstrip("\n"))
    for node2 in node.findall('.//boxsize') :
        print('\033[93m ' + 'boxsize:'+ '\033[0m',html2text.html2text(node2.text).rstrip("\n")) 
        boxsize.append(html2text.html2text(node2.text).rstrip("\n"))

fback = []
answertest = []
tans2 = []
sans = []
testoptions = []     
for node in tree.findall('.//prt'):   
    warnings.filterwarnings("ignore")
    for node2 in node.findall('.//name'):
        print('\033[93m ' + 'name:'+ '\033[0m',html2text.html2text(node2.text)) 
        fback.append(html2text.html2text(node2.text).rstrip("\n")) 
        
    for node2 in node.findall('.//answertest') :
        print('\033[93m ' + 'tans:'+ '\033[0m',html2text.html2text(node2.text)) 
        answertest.append(html2text.html2text(node2.text).rstrip("\n")) 
    for node2 in node.findall('.//tans') :
        print('\033[93m ' + 'boxsize:'+ '\033[0m',html2text.html2text(node2.text)) 
        tans2.append(html2text.html2text(node2.text).rstrip("\n")) 
    for node2 in node.findall('.//sans') :
        print('\033[93m ' + 'tans:'+ '\033[0m',html2text.html2text(node2.text)) 
        sans.append(html2text.html2text(node2.text).rstrip("\n")) 
    for node2 in node.findall('.//testoptions') :
        print('\033[93m ' + 'boxsize:'+ '\033[0m',html2text.html2text(node2.text)) 
        testoptions.append(html2text.html2text(node2.text).rstrip("\n"))        

zero = '0'
for i  in fback:
    if(i == '0'):
	    fback.remove(i)

name = name.rstrip("\n")
'''
fback = fback.rstrip("\n")
answertest = answertest.rstrip("\n")
sans = sans.rstrip("\n")
testoptions = testoptions.rstrip("\n")
'''
Write_Name = "test = STACKQuestion(\""+name+"\")\n\n"
#qvar = qvar.rstrip("\n")

Write_InputQVar = "test.inputQuestionVariables(r\"\"\" "+qvar+"  \"\"\")\n\n"
Write_InputQTest = "test.inputQuestionText(r\"\"\" "+qtest+"  \"\"\")\n\n"
Write_SpecFeedback = "test.inputSpecificFeedbackText(r\"\"\" "+sfeedback+"  \"\"\")\n\n"
Write_GenFeedback = "test.inputGeneralFeedbackText(r\"\"\" "+gfeedback+"  \"\"\")\n\n"
Write_InputQNote = "test.inputQuestionNote(r\"\"\" "+qnote+"  \"\"\")\n\n"



f = open("stackwriter.py", "w")
f.write("from core import STACKQuestion\n\n")
f.write(Write_Name)
f.write(Write_InputQVar)
f.write(Write_InputQTest)
f.write(Write_SpecFeedback)
f.write(Write_GenFeedback)
f.write(Write_InputQNote)
i=0
for i in range(len(ansname)):
    Write_InputAns = "test.inputAnswerField(\""+ansname[i]+"\", \""+tans[i]+"\" , \""+boxsize[i]+"\")\n\n"
    f.write(Write_InputAns)
j=0    
for j in range(len(answertest)):    
    Write_InputParts = "test.inputPartField(\""+fback[j]+"\", \""+answertest[j]+"\" , \""+tans2[j]+"\",\""+sans[j]+"\", \""+testoptions[j]+"\")\n\n"
    f.write(Write_InputParts)
    

f.write("test.saveQuestion()")
f.close()



#with open("stackwriter.py", "w") as f:
  