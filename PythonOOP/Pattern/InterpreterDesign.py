#!/usr/bin/python
#coding:utf8
'''
Interpreter
'''

class Context:
    def __init__(self):
        self.input=''
        self.output=''
class AbstractExpression:
    def interpret(self,context):
        pass

class ExpressionOne(AbstractExpression):
    def interpret(self, context):
        print(f'express One:{context}')
class ExpressionTwo(AbstractExpression):
    def interpret(self,context):
        print(f'express Two:{context}')

if __name__=='__main__':
    context="life's a struggle"
    expressions=[]
    expressions=[ExpressionOne()]
    expressions=expressions+[ExpressionTwo()]
    expressions=expressions+[ExpressionTwo()]
    expressions=expressions+[ExpressionOne()]
    for ex in expressions:
        ex.interpret(context=context)
