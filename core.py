from lxml import etree

saveLocation = ''

class STACKQuestion:
    def __init__(self, questionName=r"""Untitled"""):
        self.name = questionName
        #Default values
        self.questionVariables = ''
        self.questionText = ''
        self.generalQuestionFeedback = ''
        self.specificQuestionFeedback = ''
        self.questionNoteText = ''
        self.grade = r"""1"""
        self.penalty = r"""0"""
        self.hidden = r"""0"""
        self.version = r"""current"""
        self.simplify = r"""1"""
        self.assumePositive = r"""0"""
        self.assumeReal = r"""0"""
        self.correctText = r"""Correct answer, well done."""
        self.partiallyCorrectText = r"""Your answer is partially correct."""
        self.incorrectText = r"""Incorrect answer."""
        self.multiplicationSign = r"""dot"""
        self.sqrtSign = r"""1"""
        self.complexNo = r"""i"""
        self.inverseTrig = r"""cos-1"""
        self.matrixParens = r"""["""
        self.inputArr = []
        self.partArr = []

    def inputQuestionVariables(self, string=""):
        self.questionVariables = string
    
    def inputQuestionText(self, string=""):
        self.questionText = textToString(string)

    def inputSpecificFeedbackText(self, string=""):
        self.specificQuestionFeedback = string

    def inputGeneralFeedbackText(self, string=""):
        self.generalQuestionFeedback = textToString(string)

    def inputQuestionNote(self, string=""):
        self.questionNoteText = string

    def inputAnswerField(self, inputName = "", tAns = "", boxSize = "5"):
        answerField = ansField(inputName, tAns, boxSize)
        self.inputArr.append(answerField)

    def inputPartField(self, prtName = "", answerTest = "", tAns = "", sAns = "", testOptions = ""):
        partArrayLen = len(self.partArr)
        partFieldObj = prtField(partArrayLen, prtName, answerTest, tAns, sAns, testOptions)
        self.partArr.append(partFieldObj)

    def saveQuestion(self):

        root = etree.Element("quiz")
        question = etree.SubElement(root, "question", type="stack")
        questionName = etree.SubElement(question, "name")
        questionNameTextTag = etree.SubElement(questionName, "text")
        questionNameTextTag.text = self.name

        questionText = etree.SubElement(question, "questiontext", format="html")
        questionTextTag = etree.SubElement(questionText, "text")
        questionTextTag.text = etree.CDATA(self.questionText)

        generalFeedback = etree.SubElement(question, "generalfeedback", format="html")
        generalFeedbackTextTag = etree.SubElement(generalFeedback, "text")
        generalFeedbackTextTag.text = etree.CDATA(self.generalQuestionFeedback)

        defaultGrade = etree.SubElement(question, "defaultgrade")
        defaultGrade.text = self.grade

        penalty = etree.SubElement(question, "penalty")
        penalty.text = self.penalty

        hidden = etree.SubElement(question, "hidden")
        hidden.text = self.hidden

        idNumber = etree.SubElement(question, "idnumber")

        stackVersion = etree.SubElement(question, "stackversion")
        stackVersionTextTag = etree.SubElement(stackVersion, "text")
        stackVersionTextTag.text = self.version

        questionVariables = etree.SubElement(question, "questionvariables")
        questionVariablesTextTag = etree.SubElement(questionVariables, "text")
        questionVariablesTextTag.text =self.questionVariables

        specificFeedback = etree.SubElement(question, "specificfeedback", format="html")
        specificFeedbackTextTag = etree.SubElement(specificFeedback, "text")
        specificFeedbackTextTag.text = self.specificQuestionFeedback

        questionNote = etree.SubElement(question, "questionnote")
        questionNoteTextTag = etree.SubElement(questionNote, "text")
        questionNoteTextTag.text = self.questionNoteText

        questionSimplify = etree.SubElement(question, "questionsimplify")
        questionSimplify.text = self.simplify

        assumePositive = etree.SubElement(question, "assumepositive")
        assumePositive.text = self.assumePositive

        assumeReal = etree.SubElement(question, "assumereal")
        assumeReal.text = self.assumeReal

        prtCorrect = etree.SubElement(question, "prtcorrect", format="html")
        prtCorrectTextTag = etree.SubElement(prtCorrect, "text")
        prtCorrectTextTag.text = self.correctText

        prtPartiallyCorrect = etree.SubElement(question, "prtpartiallycorrect", format="html")
        prtPartiallyCorrectTextTag = etree.SubElement(prtPartiallyCorrect, "text")
        prtPartiallyCorrectTextTag.text = self.partiallyCorrectText

        prtIncorrect = etree.SubElement(question, "prtincorrect", format="html")
        prtIncorrectTextTag = etree.SubElement(prtIncorrect, "text")
        prtIncorrectTextTag.text = self.incorrectText

        multiplicationSign = etree.SubElement(question, "multiplicationsign")
        multiplicationSign.text = self.multiplicationSign

        sqrtSign = etree.SubElement(question, "sqrtsign")
        sqrtSign.text = self.sqrtSign

        complexNo = etree.SubElement(question, "complexno")
        complexNo.text = self.complexNo

        inverseTrig = etree.SubElement(question, "inversetrig")
        inverseTrig.text = self.inverseTrig

        matrixParens = etree.SubElement(question, "matrixparens")
        matrixParens.text = self.matrixParens

        variantsSelectionSeed = etree.SubElement(question, "variantsselectionseed")

        inputArrSize = len(self.inputArr)
        XMLinputArr, inputName, inputTAns, inputBoxSize, options, inputType, strictSyntax, insertStars, syntaxHint, syntaxAttribute, forbidWords, allowWords, forbidFloat, requireLowestTerms, checkAnswerType, mustVerify, showValidation = ([0 for i in range(inputArrSize)] for j in range(17))
        i = 0

        for i in range(inputArrSize):
            XMLinputArr[i] = etree.SubElement(question, "input")
            inputName[i] = etree.SubElement(XMLinputArr[i], "name")
            inputName[i].text = self.inputArr[i].inputName

            inputType[i] = etree.SubElement(XMLinputArr[i], "type")
            inputType[i].text = self.inputArr[i].inputType

            inputTAns[i] = etree.SubElement(XMLinputArr[i], "tans")
            inputTAns[i].text = self.inputArr[i].inputTAns

            inputBoxSize[i] = etree.SubElement(XMLinputArr[i], "boxsize")
            inputBoxSize[i].text = self.inputArr[i].inputBoxSize

            strictSyntax[i] = etree.SubElement(XMLinputArr[i], "strictsyntax")
            strictSyntax[i].text = self.inputArr[i].strictSyntax

            insertStars[i] = etree.SubElement(XMLinputArr[i], "insertstars")
            insertStars[i].text = self.inputArr[i].insertStars

            syntaxHint[i] = etree.SubElement(XMLinputArr[i], "syntaxhint")
            syntaxHint[i].text = self.inputArr[i].syntaxHint

            syntaxAttribute[i] = etree.SubElement(XMLinputArr[i], "syntaxattribute")
            syntaxAttribute[i].text = self.inputArr[i].syntaxAttribute

            forbidWords[i] = etree.SubElement(XMLinputArr[i], "forbidwords")
            forbidWords[i].text = self.inputArr[i].forbidWords

            allowWords[i] = etree.SubElement(XMLinputArr[i], "allowwords")
            allowWords[i].text = self.inputArr[i].allowWords

            forbidFloat[i] = etree.SubElement(XMLinputArr[i], "forbidfloat")
            forbidFloat[i].text = self.inputArr[i].forbidFloat

            requireLowestTerms[i] = etree.SubElement(XMLinputArr[i], "requirelowestterms")
            requireLowestTerms[i].text = self.inputArr[i].requireLowestTerms

            checkAnswerType[i] = etree.SubElement(XMLinputArr[i], "checkanswertype")
            checkAnswerType[i].text = self.inputArr[i].checkAnswerType

            mustVerify[i] = etree.SubElement(XMLinputArr[i], "mustverify")
            mustVerify[i].text = self.inputArr[i].mustVerify

            showValidation[i] = etree.SubElement(XMLinputArr[i], "showvalidation")
            showValidation[i].text = self.inputArr[i].showValidation

            options[i] = etree.SubElement(XMLinputArr[i], "options")
            options[i].text = self.inputArr[i].options

            i = i + 1

        partArrSize = len(self.partArr)
        #Supports only one node per tree
        XMLpartArr, feedbackVariablesTextTag, trueFeedbackTextTag, falseFeedbackTextTag, partName, partValue, autoSimplify, feedbackVariables, node, nodeName, answerTest, sAns, partTAns, testOptions, nodeQuiet, trueScoreMode, trueScore, truePenalty, trueNextNode, trueAnswerNote, trueFeedback, falseScoreMode, falseScore, falsePenalty, falseNextNode, falseAnswerNote, falseFeedback = ([0 for i in range(partArrSize)] for j in range(27))

        i = 0

        for i in range(partArrSize):
            XMLpartArr[i] = etree.SubElement(question, "prt")

            partName[i] = etree.SubElement(XMLpartArr[i], "name")
            partName[i].text = self.partArr[i].prtName
 
            partValue[i] = etree.SubElement(XMLpartArr[i], "value")
            partValue[i].text = self.partArr[i].partValue

            autoSimplify[i] = etree.SubElement(XMLpartArr[i], "autosimplify")
            autoSimplify[i].text = self.partArr[i].autoSimplify

            feedbackVariables[i] = etree.SubElement(XMLpartArr[i], "feedbackvariables")
            feedbackVariablesTextTag[i] = etree.SubElement(feedbackVariables[i], "text")
            feedbackVariablesTextTag[i].text = self.partArr[i].feedbackVariablesText

            node[i] = etree.SubElement(XMLpartArr[i], "node")

            nodeName[i] = etree.SubElement(node[i], "name")
            nodeName[i].text = self.partArr[i].nodeName

            answerTest[i] = etree.SubElement(node[i], "answertest")
            answerTest[i].text = self.partArr[i].answerTest

            sAns[i] = etree.SubElement(node[i], "sans")
            sAns[i].text = self.partArr[i].sAns

            partTAns[i] = etree.SubElement(node[i], "tans")
            partTAns[i].text = self.partArr[i].partTAns

            testOptions[i] = etree.SubElement(node[i], "testoptions")
            testOptions[i].text = self.partArr[i].testOptions

            nodeQuiet[i] = etree.SubElement(node[i], "quiet")
            nodeQuiet[i].text = self.partArr[i].nodeQuiet

            trueScoreMode[i] = etree.SubElement(node[i], "truescoremode")
            trueScoreMode[i].text = self.partArr[i].trueScoreMode

            trueScore[i] = etree.SubElement(node[i], "truescore")
            trueScore[i].text = self.partArr[i].trueScore

            truePenalty[i] = etree.SubElement(node[i], "truepenalty")

            trueNextNode[i] = etree.SubElement(node[i], "truenextnode")
            trueNextNode[i].text = self.partArr[i].trueNextNode

            trueAnswerNote[i] = etree.SubElement(node[i], "trueanswernote")
            trueAnswerNote[i].text = self.partArr[i].trueAnswerNoteText

            trueFeedback[i] = etree.SubElement(node[i], "truefeedback", format="html")
            trueFeedbackTextTag[i] = etree.SubElement(trueFeedback[i], "text")
            trueFeedbackTextTag[i].text = self.partArr[i].trueFeedbackText

            falseScoreMode[i] = etree.SubElement(node[i], "falsescoremode")
            falseScoreMode[i].text = self.partArr[i].falseScoreMode

            falseScore[i] = etree.SubElement(node[i], "falsescore")
            falseScore[i].text = self.partArr[i].falseScore

            falsePenalty[i] = etree.SubElement(node[i], "falsepenalty")

            falseNextNode[i] = etree.SubElement(node[i], "falsenextnode")
            falseNextNode[i].text = self.partArr[i].falseNextNode

            falseAnswerNote[i] = etree.SubElement(node[i], "falseanswernote")
            falseAnswerNote[i].text = self.partArr[i].falseAnswerNoteText

            falseFeedback[i] = etree.SubElement(node[i], "falsefeedback", format="html")
            falseFeedbackTextTag[i] = etree.SubElement(falseFeedback[i], "text")
            falseFeedbackTextTag[i].text = self.partArr[i].falseFeedbackText

            i = i + 1

        print(etree.tostring(root, pretty_print=True, encoding='unicode'))
        # Allow user to specify location
        document = open(saveLocation, 'wb')
        document.write(etree.tostring(root, xml_declaration=True, encoding="UTF-8", pretty_print=True))
        document.close

        return 1
        
class ansField:
    def __init__(self, inputName = "", tAns = "", boxSize = "5"):
        self.inputName = inputName
        self.inputType = r"""algebraic"""
        self.inputTAns = tAns
        self.inputBoxSize = boxSize
        self.strictSyntax = r"""1"""
        self.insertStars = r"""0"""
        self.syntaxHint = ''
        self.syntaxAttribute = r"""0"""
        self.forbidWords = ''
        self.allowWords = ''
        self.forbidFloat = r"""0"""
        self.requireLowestTerms = r"""0"""
        self.checkAnswerType = r"""0"""
        self.mustVerify = r"""1"""
        self.showValidation = r"""1"""
        self.options = ''

class prtField:
    def __init__(self, partArrLen, prtName = "", answerTest = "", tAns = "", sAns = "", testOptions = ""):
        self.prtName = prtName
        self.partValue = r"""1.0"""
        self.autoSimplify = r"""1"""
        self.feedbackVariablesText = ''
        self.nodeName = r"""0"""
        self.answerTest = answerTest
        self.sAns = sAns
        self.partTAns = tAns
        self.testOptions = testOptions
        self.nodeQuiet = r"""0"""
        self.trueScoreMode = r"""="""
        self.trueScore = r"""1.0"""
        #truePenalty
        self.trueNextNode = r"""-1"""
        self.trueAnswerNoteText = 'prt' + str(partArrLen + 1) + '-1-T'
        self.trueFeedbackText = r""""""
        self.falseScoreMode = r"""="""
        self.falseScore = r"""0.0"""
        #falsePenalty
        self.falseNextNode = r"""-1"""
        self.falseAnswerNoteText = 'prt' + str(partArrLen + 1) + '-1-F'
        self.falseFeedbackText = r""""""


def textToString(string):
    s2 = "<p>" + string.replace("\n", "<br>") + "</p>"
    return s2