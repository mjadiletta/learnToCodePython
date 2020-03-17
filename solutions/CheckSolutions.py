from solutions.codeFunctionsSolutions import codeFunctionsSolutions
from solutions.loopSimpleSolutions import loopSimpleSolutions
from solutions.conditionalStatementsSolutions import conditionalStatementsSolutions
from solutions.listSimpleSolutions import listSimpleSol
from solutions.numpySimpleSolutions import numpySimpleSol
from solutions.matplotlibIntroductionSolutions import matplotlibIntroductionSol
from solutions.dictionarySolutions import dictionarySol
from solutions.listsComplexSolutions import listComplexSolutions
from solutions.numpyComplexSolutions import numpyComplexSolutions
from solutions.classesSimpleSolutions import classesSimpleSolutions
from solutions.classesComplexSolutions import classesComplexSolutions
from solutions.fileSeparationSolutions import fileSeparationSolutions

from solutions.projectSolutions import projectSolutions


class CheckSolutions:
    def __init__(self):
        # lecture 1
        self.functionSolutions = codeFunctionsSolutions().functionSolutions

        # lecture 2
        self.loopSolutions = loopSimpleSolutions().loopSolutions

        # lecture 3
        self.conditionalSolutions = conditionalStatementsSolutions().conditionalSolutions

        # lecture 5
        self.listSimpleSolutions = listSimpleSol().listSimpleSolutions

        # lecture 6
        self.numpySimpleSolutions = numpySimpleSol().numpySimpleSolutions

        # lecture 7
        self.matplotlibIntro = matplotlibIntroductionSol().matplotlibIntro

        # lecture 9
        self.dictionarySolutions = dictionarySol().dictionarySolutions

        # lecture 10
        self.listComplexSolutions = listComplexSolutions().listComplexSol

        # lecture 11
        self.numpyComplexSolutions = numpyComplexSolutions().numpyComplexSol

        # lecture 13
        self.classesSimpleSolutions = classesSimpleSolutions().classesSimpleSol

        # lecture 14
        self.classesComplexSolutions = classesComplexSolutions().classesComplexSol

        # lecture 15
        self.fileSeparationSolutions = fileSeparationSolutions().fileSeparationSol

        # 4, 8, 12, 16
        self.projectSolutions = projectSolutions().projectSolutions


