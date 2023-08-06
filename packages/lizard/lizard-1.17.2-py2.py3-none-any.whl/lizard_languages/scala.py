'''
Language parser for Scala
'''
from .swift import SwiftStates
from .code_reader import CodeReader
from .clike import CCppCommentsMixin
from .golike import GoLikeStates
__author__ = 'David Baum'


class ScalaReader(CodeReader, CCppCommentsMixin):
    # pylint: disable=R0903

    ext = ['scala']
    language_names = ['scala']
    _conditions = set(['if', 'for', 'while', '&&', '||', '?', 'catch',
                      'case', 'do'])

    def __init__(self, context):
        super(ScalaReader, self).__init__(context)
        self.parallel_states = [ScalaStates(context)]


class ScalaStates(GoLikeStates):  # pylint: disable=R0903
    def _state_global(self, token):
        if token == 'def':
            self._state = self._function_name
        elif token in ('}',):
            self.statemachine_return()
        elif token == '{':
            self.sub_state(ScalaStates(self.context))

    def _expect_function_dec(self, token):
        if token == '(':
            self._state = self._function_dec
        else:
            self._state = self._state_global

    def _expect_function_impl(self, token):
        if token == "=":
            self._state = self._expect_function_body
        else:
            super(ScalaStates, self)._expect_function_impl(token)

    def _expect_function_body(self, token):
        if self.context.newline:
            self.context.end_of_function()
            self.next(self._state_global, token)
        elif token == '{':
            self.sub_state(ScalaStates(self.context))


    def statemachine_before_return(self):
        if self._state == self._expect_function_body:
            self.context.end_of_function()


