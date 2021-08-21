from PyQt5 import QtCore
from .calculator import Calculator, get_parser


CALC_TIME_LIMIT = 1000
EXPR_LENGTH_LIMIT = 512
__all__ = ['EasyCalculator']


class EasyCalculator(QtCore.QObject):
    cmd_prefix = '!calc '

    def __init__(self, logger, core):
        super().__init__(core)
        self.core = core
        self.logger = logger
        self.disabled = False

        # load mcBasicLib
        self.utils = core.get_plugin('mcBasicLib')
        if self.utils is None:
            self.logger.error('Failed to load plugin "mcBasicLib", easyCalc will be disabled.')
            self.logger.error('Please make sure that "mcBasicLib" has been added to plugins.')
            self.disabled = True

        if self.disabled:
            return

        # connect signals and slots
        self.utils.sig_input.connect(self.on_player_input)

        self.parser = get_parser()

    def calc(self, expr):
        try:
            ans = self.parser.parse(expr)
            Calculator.last_ans = ans
            ans = str(ans)
        except ZeroDivisionError as e:
            ans = str(e)
        except OverflowError:
            ans = 'result too large'
        except:
            ans = 'unacceptable expression'
        self.utils.say('[EasyCalc] ' + ans)
    
    def help(self, player):
        help_msg = f'''\
-------------Command List-------------
"{self.cmd_prefix}help": Show this help message.
"{self.cmd_prefix}<expr>": Calculate the arithmetic expression.
----------------Notice----------------
Now we support the following operations:
addition (+), subtraction (-), multiplication (*), division(/),
modulo (%) and exponentiation (^).
The expression should not exceed the limit of {EXPR_LENGTH_LIMIT} characters.
--------------------------------------'''
        self.utils.tell(player, help_msg)
    
    @QtCore.pyqtSlot(tuple)
    def on_player_input(self, pair):
        self.logger.debug('EasyCalculator.on_player_input called')
        player, text = pair
        if text.startswith(EasyCalculator.cmd_prefix):
            expr = text[len(EasyCalculator.cmd_prefix):]
            if len(expr) > EXPR_LENGTH_LIMIT:
                self.utils.tell(player, 'Expression length limit exceeded.')
            elif expr.strip() == 'help':
                self.help(player)
            else:
                if player.is_console():
                    self.utils.say(text)
                self.calc(expr)
