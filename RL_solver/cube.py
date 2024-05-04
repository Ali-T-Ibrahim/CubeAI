import numpy as np


class Cube:
    def __init__(self):
        # Initialize each face to 3 by 3 matrix
        # green front white up
        self.face = {
            'U': np.full((3, 3), 'W'),
            'D': np.full((3, 3), 'Y'),
            'F': np.full((3, 3), 'G'),
            'B': np.full((3, 3), 'B'),
            'R': np.full((3, 3), 'R'),
            'L': np.full((3, 3), 'O'),
        }

        # current move for logging
        self.move = None

    def z2(self):
        # z2 rotation to prep for solve
        self.face['U'], self.face['D'], self.face['L'], self.face['R'] = (self.face['D'],
                                                                          self.face['U'],
                                                                          self.face['R'],
                                                                          self.face['L'])
    def u_move(self):
        # matrix manipulation
        temp = self.face['F'][0].copy()
        self.face['F'][0] = self.face['R'][0]
        self.face['R'][0] = self.face['B'][0]
        self.face['B'][0] = self.face['L'][0]
        self.face['L'][0] = temp
        # logging
        self.move = "U"

    def up_move(self):
        # matrix manipulation
        temp = self.face['F'][0].copy()
        self.face['F'][0] = self.face['L'][0]
        self.face['L'][0] = self.face['B'][0]
        self.face['B'][0] = self.face['R'][0]
        self.face['R'][0] = temp
        # logging
        self.move = "U'"

    def d_move(self):
        # matrix manipulation
        temp = self.face['F'][2].copy()
        self.face['F'][2] = self.face['L'][2]
        self.face['L'][2] = self.face['B'][2]
        self.face['B'][2] = self.face['R'][2]
        self.face['R'][2] = temp
        # logging
        self.move = "D"

    def dp_move(self):
        # matrix manipulation
        temp = self.face['F'][2].copy()
        self.face['F'][2] = self.face['R'][2]
        self.face['R'][2] = self.face['B'][2]
        self.face['B'][2] = self.face['L'][2]
        self.face['L'][2] = temp
        # logging
        self.move = "D'"

    def f_move(self):
        # matrix manipulation
        temp = self.face['U'][2].copy()
        self.face['U'][2] = self.face['L'][:, 2]
        self.face['L'][:, 2] = self.face['D'][0]
        self.face['D'][0] = self.face['R'][:, 0]
        self.face['R'][:, 0] = temp
        # logging
        self.move = "F"

    def fp_move(self):
        # matrix manipulation
        temp = self.face['U'][2].copy()
        self.face['U'][2] = self.face['R'][:, 0]
        self.face['R'][:, 0] = self.face['D'][0]
        self.face['D'][0] = self.face['L'][:, 2]
        self.face['L'][:, 2] = temp
        # logging
        self.move = "F'"
    def b_move(self):
        # matrix manipulation
        temp = self.face['U'][0].copy()
        self.face['U'][0] = self.face['R'][:, 2]
        self.face['R'][:, 2] = self.face['D'][2]
        self.face['D'][2] = self.face['L'][:, 0]
        self.face['L'][:, 0] = temp
        # logging
        self.move = "B"

    def bp_move(self):
        # matrix manipulation
        temp = self.face['U'][0].copy()
        self.face['U'][0] = self.face['L'][:, 0]
        self.face['L'][:, 0] = self.face['D'][2]
        self.face['D'][2] = self.face['R'][:, 2]
        self.face['R'][:, 2] = temp
        # logging
        self.move = "B'"

    def r_move(self):
        # matrix manipulation
        temp = self.face['U'][:, [2]].copy()
        self.face['U'][:, [2]] = self.face['F'][:, [2]]
        self.face['F'][:, [2]] = self.face['D'][:, [2]]
        self.face['D'][:, [2]] = self.face['B'][:, [2]]
        self.face['B'][:, [2]] = temp
        # logging
        self.move = "R"

    def rp_move(self):
        # matrix manipulation
        temp = self.face['U'][:, [2]].copy()
        self.face['U'][:, [2]] = self.face['B'][:, [2]]
        self.face['B'][:, [2]] = self.face['D'][:, [2]]
        self.face['D'][:, [2]] = self.face['F'][:, [2]]
        self.face['F'][:, [2]] = temp
        # logging
        self.move = "R'"

    def l_move(self):
        # matrix manipulation
        temp = self.face['U'][:, [0]].copy()
        self.face['U'][:, [0]] = self.face['B'][:, [0]]
        self.face['B'][:, [0]] = self.face['D'][:, [0]]
        self.face['D'][:, [0]] = self.face['F'][:, [0]]
        self.face['F'][:, [0]] = temp
        # logging
        self.move = "L"

    def lp_move(self):
        # matrix manipulation
        # matrix manipulation
        temp = self.face['U'][:, [0]].copy()
        self.face['U'][:, [0]] = self.face['F'][:, [0]]
        self.face['F'][:, [0]] = self.face['D'][:, [0]]
        self.face['D'][:, [0]] = self.face['B'][:, [0]]
        self.face['B'][:, [0]] = temp
        # logging
        self.move = "L'"



    def visualize_string(self):
        for face in self.face:
            print(f"{face} face: \n{self.face[face]}")


cube = Cube()
cube.z2()
cube.visualize_string()
cube.u_move()
cube.visualize_string()
