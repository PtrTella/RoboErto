#Move Wrapper Class
class NaoMove:
    def __init__(self, name, duration=None, preconditions=None, postconditions=None):
        self.name = name
        self.duration = duration
        self.preconditions = preconditions 
        self.postconditions = postconditions  

#Moves
initial =   NaoMove('I_StandInit', 1.60, None, None)
goal    =   NaoMove('F_Crouch', 1.32, None, None)

intermediate = [    NaoMove('StandUp', 8.35,  {'standing': False}, {'standing': True}),
                    NaoMove('AirGuitar', 4.10,   {'standing': True},  {'standing': True}),
                    NaoMove('ArmDance', 10.42, {'standing': True},  {'standing': True}),
                    NaoMove('BlowKisses', 4.58, {'standing': True} ,{'standing': True}),
                    NaoMove('Bow', 3.86,   {'standing': True},  {'standing': True}),
                    NaoMove('DiagonalRight', 2.56,  {'standing': True},  {'standing': True}),
                    NaoMove('DanceMove', 6.13,  {'standing': True},  {'standing': True}),
                    NaoMove('SprinklerL', 4.14,   {'standing': True},  {'standing': True}),
                    NaoMove('SprinklerR', 4.36,  {'standing': True},  {'standing': True}),
                    NaoMove('TheRobot', 6.10,   {'standing': True},  {'standing': True}),
                    NaoMove('ComeOn', 3.62,   {'standing': True},  {'standing': True}),
                    NaoMove('StayingAlive', 5.90,   {'standing': True},  {'standing': True}),
                    NaoMove('Rhythm', 2.95,  {'standing': True},  {'standing': True}),
                    NaoMove('PulpFiction', 5.8,   {'standing': True},  {'standing': True}),
                    NaoMove('Wave', 3.72,  None, None),
                    NaoMove('Glory', 3.28,  None, None),
                    NaoMove('Clap', 4.10,  None, None),
                    NaoMove('Joy', 4.50,  None, None),
                    NaoMove('DoubleMovement', 10.6, None,  None),
                    NaoMove('CowboyMove', 22.10, {'standing': True},  {'standing': True}),
                    NaoMove('Macarena', 2.95, {'standing': True},  {'standing': True})]

mandatory = [   NaoMove('M_WipeForehead', 4.48, None , None),
                NaoMove('M_Stand', 2.32, None, {'standing': True} ),
                NaoMove('M_Hello', 4.34, None, None),
                NaoMove('M_Sit', 9.84, None,  {'standing': False}),
                NaoMove('M_SitRelax', 3.92, None,  {'standing': False}),
                NaoMove('M_StandZero',1.4, None,  {'standing': True})]

list_fast_moves = ['I_StandInit', 'M_StandZero', 'M_Stand', 'Rhythm', 'DiagonalRight', 'F_Crouch', 'Macarena']
list_normal_moves = ['ComeOn','Wave','Glory', 'M_SitRelax', 'M_Hello', 'M_WipeForehead','AirGuitar', 'BlowKisses', 'Bow', 'SprinklerL', 'SprinklerR', 'Clap', 'Joy' ]
list_slow_moves = ['ArmDance','StandUp', 'DanceMove', 'TheRobot','StayingAlive', 'PulpFiction', 'M_Sit', 'DoubleMovement', 'CowboyMove' ]
