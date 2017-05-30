import mujoco_py
import imp
import argparse
import numpy as np

class Simulator():
    """
    Cross Entropy Method Stochastic Optimizer
    """
    def __init__(self):

        parser = argparse.ArgumentParser(description='simulator')
        parser.add_argument('conf', type=str, help='config file')
        args = parser.parse_args()

        config = args.conf
        confmod = imp.load_source('conf','configs/' + config + '.py')
        self.conf = confmod.config


        self.model = mujoco_py.MjModel(self.conf['modelfile'])

        gofast = False
        self.viewer = mujoco_py.MjViewer(visible=True, init_width=480,
                                         init_height=480, go_fast=gofast)
        self.viewer.start()
        self.viewer.set_model(self.model)
        # self.viewer.cam.camid = 0

    def start(self):
        for t in range(self.conf['T']):
            # self.model.data.ctrl = np.ones_like(self.model.data.ctrl)*10
            self.model.data.ctrl = np.zeros_like(self.model.data.ctrl)
            self.viewer.loop_once()
            self.model.step()

if __name__ == '__main__':
    simulator = Simulator()
    simulator.start()