from solutions.checkSolutionsFiles.a1_codeFunctionsSolutions import codeFunctionsSolutions
from solutions.checkSolutionsFiles.a2_loopSimpleSolutions import loopSimpleSolutions
from solutions.checkSolutionsFiles.a3_conditionalStatementsSolutions import conditionalStatementsSolutions
from solutions.checkSolutionsFiles.a5_listSimpleSolutions import listSimpleSol
from solutions.checkSolutionsFiles.a6_numpySimpleSolutions import numpySimpleSol
from solutions.checkSolutionsFiles.a7_matplotlibIntroductionSolutions import matplotlibIntroductionSol
from solutions.checkSolutionsFiles.a9_dictionarySolutions import dictionarySol
from solutions.checkSolutionsFiles.a10_listsComplexSolutions import listComplexSolutions
from solutions.checkSolutionsFiles.a11_numpyComplexSolutions import numpyComplexSolutions
from solutions.checkSolutionsFiles.a13_classesSimpleSolutions import classesSimpleSolutions
from solutions.checkSolutionsFiles.a14_classesComplexSolutions import classesComplexSolutions
from solutions.checkSolutionsFiles.a15_searchingSortingSolutions import searchingSortingSolutions
from solutions.checkSolutionsFiles.a17_fileIOSolutions import fileIOSolutions
from solutions.checkSolutionsFiles.a18_graphicsIntroSolutions import graphicsIntroSolutions
from solutions.checkSolutionsFiles.a19_graphicsComplexSolutions import graphicsComplexSolutions

from solutions.checkSolutionsFiles.a4_project1Solution import project1Solutions
from solutions.checkSolutionsFiles.a8_project2Solution import project2Solutions
from solutions.checkSolutionsFiles.a12_project3Solution import project3Solutions
from solutions.checkSolutionsFiles.a16_project4Solution import project4Solutions


class CheckSolutions:
    def __init__(self):
        # lecture 1
        self.functionSolutions = codeFunctionsSolutions().functionSolutions

        # lecture 2
        self.loopSolutions = loopSimpleSolutions().loopSolutions

        # lecture 3
        self.conditionalSolutions = conditionalStatementsSolutions().conditionalSolutions

        # lecture 4: Project 1
        self.project1Solutions = project1Solutions().projectSolutions

        # lecture 5
        self.listSimpleSolutions = listSimpleSol().listSimpleSolutions

        # lecture 6
        self.numpySimpleSolutions = numpySimpleSol().numpySimpleSolutions

        # lecture 7
        self.matplotlibIntro = matplotlibIntroductionSol().matplotlibIntro

        # lecture 8: Project 2
        self.project2Solutions = project2Solutions().projectSolutions

        # lecture 9
        self.dictionarySolutions = dictionarySol().dictionarySolutions

        # lecture 10
        self.listComplexSolutions = listComplexSolutions().listComplexSol

        # lecture 11
        self.numpyComplexSolutions = numpyComplexSolutions().numpyComplexSol

        # lecture 12: Project 3
        self.project3Solutions = project3Solutions().projectSolutions

        # lecture 13
        self.classesSimpleSolutions = classesSimpleSolutions().classesSimpleSol

        # lecture 14
        self.classesComplexSolutions = classesComplexSolutions().classesComplexSol

        # lecture 15
        self.searchingSortingSolutions = searchingSortingSolutions().searchingSortingSol

        # lecture 16: Project 4
        self.project4Solutions = project4Solutions().projectSolutions

        # lecture 17
        self.fileIOSolutions = fileIOSolutions().fileIOSolutions

        # lecture 18
        self.graphicsIntroSolutions = graphicsIntroSolutions().graphicsIntroSolutions

        # lecture 19
        self.graphicsComplexSolutions = graphicsComplexSolutions().graphicsComplexSolutions


