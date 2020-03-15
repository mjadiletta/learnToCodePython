from solutions.codeFunctionsSolutions import codeFunctionsSolutions
from solutions.loopSimpleSolutions import loopSimpleSolutions
from solutions.conditionalStatementsSolutions import conditionalStatementsSolutions
from solutions.listSimpleSolutions import listSimpleSol
from solutions.numpySimpleSolutions import numpySimpleSol
from solutions.matplotlibIntroductionSolutions import matplotlibIntroductionSol
from solutions.projectSolutions import projectSolutions


class CheckSolutions:
    def __init__(self):
        self.functionSolutions = {}
        self.functionSolutions['example1'] = codeFunctionsSolutions().ex1
        self.functionSolutions['example2'] = codeFunctionsSolutions().ex2
        self.functionSolutions['example3'] = codeFunctionsSolutions().ex3
        self.functionSolutions['example4'] = codeFunctionsSolutions().ex4
        self.functionSolutions['example5'] = codeFunctionsSolutions().ex5
        self.functionSolutions['example6'] = codeFunctionsSolutions().ex6
        self.functionSolutions['example7'] = codeFunctionsSolutions().ex7
        self.functionSolutions['example8'] = codeFunctionsSolutions().ex8
        self.functionSolutions['example9'] = codeFunctionsSolutions().ex9
        self.functionSolutions['example10'] = codeFunctionsSolutions().ex10
        self.functionSolutions['example11'] = codeFunctionsSolutions().ex11
        self.functionSolutions['example12'] = codeFunctionsSolutions().ex12
        self.functionSolutions['example13'] = codeFunctionsSolutions().ex13
        self.functionSolutions['example14'] = codeFunctionsSolutions().ex14

        self.loopSolutions = {}
        self.loopSolutions['example1'] = loopSimpleSolutions().ex1
        self.loopSolutions['example2'] = loopSimpleSolutions().ex2
        self.loopSolutions['example3'] = loopSimpleSolutions().ex3
        self.loopSolutions['example4'] = loopSimpleSolutions().ex4
        self.loopSolutions['example5'] = loopSimpleSolutions().ex5
        self.loopSolutions['example6'] = loopSimpleSolutions().ex6
        self.loopSolutions['example7'] = loopSimpleSolutions().ex7
        self.loopSolutions['example8'] = loopSimpleSolutions().ex8
        self.loopSolutions['example9'] = loopSimpleSolutions().ex9
        self.loopSolutions['example10'] = loopSimpleSolutions().ex10
        self.loopSolutions['example11'] = loopSimpleSolutions().ex11

        self.conditionalSolutions = {}
        self.conditionalSolutions['example1'] = conditionalStatementsSolutions().ex1
        self.conditionalSolutions['example2'] = conditionalStatementsSolutions().ex2
        self.conditionalSolutions['example3'] = conditionalStatementsSolutions().ex3
        self.conditionalSolutions['example4'] = conditionalStatementsSolutions().ex4

        self.listSimpleSolutions = {}
        self.listSimpleSolutions['example1'] = listSimpleSol().ex1
        self.listSimpleSolutions['example2'] = listSimpleSol().ex2
        self.listSimpleSolutions['example3'] = listSimpleSol().ex3
        self.listSimpleSolutions['example4'] = listSimpleSol().ex4
        self.listSimpleSolutions['example5'] = listSimpleSol().ex5
        self.listSimpleSolutions['example6'] = listSimpleSol().ex6
        self.listSimpleSolutions['example7'] = listSimpleSol().ex7
        self.listSimpleSolutions['example8'] = listSimpleSol().ex8
        self.listSimpleSolutions['example9'] = listSimpleSol().ex9
        self.listSimpleSolutions['example10'] = listSimpleSol().ex10

        self.numpySimpleSolutions = {}
        self.numpySimpleSolutions['example1'] = numpySimpleSol().ex1
        self.numpySimpleSolutions['example2'] = numpySimpleSol().ex2
        self.numpySimpleSolutions['example3'] = numpySimpleSol().ex3
        self.numpySimpleSolutions['example4'] = numpySimpleSol().ex4
        self.numpySimpleSolutions['example5'] = numpySimpleSol().ex5
        self.numpySimpleSolutions['example6'] = numpySimpleSol().ex6
        self.numpySimpleSolutions['example7'] = numpySimpleSol().ex7
        self.numpySimpleSolutions['example8'] = numpySimpleSol().ex8
        self.numpySimpleSolutions['example9'] = numpySimpleSol().ex9
        self.numpySimpleSolutions['example10'] = numpySimpleSol().ex10
        self.numpySimpleSolutions['example11'] = numpySimpleSol().ex11
        self.numpySimpleSolutions['example12'] = numpySimpleSol().ex12
        self.numpySimpleSolutions['example13'] = numpySimpleSol().ex13
        self.numpySimpleSolutions['example14'] = numpySimpleSol().ex14
        self.numpySimpleSolutions['example15'] = numpySimpleSol().ex15
        self.numpySimpleSolutions['example16'] = numpySimpleSol().ex16
        self.numpySimpleSolutions['example17'] = numpySimpleSol().ex17
        self.numpySimpleSolutions['example18'] = numpySimpleSol().ex18
        self.numpySimpleSolutions['example19'] = numpySimpleSol().ex19
        self.numpySimpleSolutions['example20'] = numpySimpleSol().ex20

        self.matplotlibIntro = {}
        self.matplotlibIntro['example1'] = matplotlibIntroductionSol().ex1
        self.matplotlibIntro['example2'] = matplotlibIntroductionSol().ex2
        self.matplotlibIntro['example3'] = matplotlibIntroductionSol().ex3
        self.matplotlibIntro['example4'] = matplotlibIntroductionSol().ex4

        self.projectSolutions = {}
        self.projectSolutions['project1'] = projectSolutions().proj1
        self.projectSolutions['project2p1'] = projectSolutions().proj2p1
        self.projectSolutions['project2p2'] = projectSolutions().proj2p2
        self.projectSolutions['project2p3a'] = projectSolutions().proj2p3a
        self.projectSolutions['project2p3b'] = projectSolutions().proj2p3b

