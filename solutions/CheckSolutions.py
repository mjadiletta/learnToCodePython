from solutions.a1_codeFunctionsSolutions import codeFunctionsSolutions
from solutions.a2_loopSimpleSolutions import loopSimpleSolutions
from solutions.a3_conditionalStatementsSolutions import conditionalStatementsSolutions
from solutions.a5_listSimpleSolutions import listSimpleSol
from solutions.a6_numpySimpleSolutions import numpySimpleSol
from solutions.a7_matplotlibIntroductionSolutions import matplotlibIntroductionSol
from solutions.a9_dictionarySolutions import dictionarySol
from solutions.a10_listsComplexSolutions import listComplexSolutions
from solutions.a11_numpyComplexSolutions import numpyComplexSolutions
from solutions.a13_classesSimpleSolutions import classesSimpleSolutions
from solutions.a14_classesComplexSolutions import classesComplexSolutions
from solutions.a15_fileSeparationSolutions import fileSeparationSolutions
from solutions.a17_fileIOSolutions import fileIOSolutions
from solutions.a18_graphicsIntroSolutions import graphicsIntroSolutions
from solutions.a19_graphicsComplexSolutions import graphicsComplexSolutions

from solutions.a4_project1Solution import project1Solutions
from solutions.a8_project2Solution import project2Solutions
from solutions.a12_project3Solution import project3Solutions
from solutions.a16_project4Solution import project4Solutions
from solutions.a20_project5Solution import project5Solutions


class CheckSolutions:
    def __init__(self):
        # lecture 1
        self.functionSolutions = codeFunctionsSolutions().functionSolutions

        # lecture 2
        self.loopSolutions = loopSimpleSolutions().loopSolutions

        # lecture 3
        self.conditionalSolutions = conditionalStatementsSolutions().conditionalSolutions

        # lecture 4: Project 1
        self.project4Solutions = project4Solutions().projectSolutions

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
        self.fileSeparationSolutions = fileSeparationSolutions().fileSeparationSol

        # lecture 16: Project 4
        self.project4Solutions = project4Solutions().projectSolutions

        # lecture 17
        self.fileIOSolutions = fileIOSolutions().fileIOSolutions

        # lecture 18
        self.graphicsIntroSolutions = graphicsIntroSolutions().graphicsIntroSolutions

        # lecture 19
        self.graphicsComplexSolutions = graphicsComplexSolutions().graphicsComplexSolutions

        # lecture 20: Project 5
        self.project5Solutions = project5Solutions().projectSolutions


