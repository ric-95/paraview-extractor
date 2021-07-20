import json
from string import Template
import numpy as np


def parse_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("--num-lines-per-sample", type=int, default=16,
                        help="Number of lines to extract per sample.")
    parser.add_argument("--timesteps-to-sample", nargs="+", type=float,
                        help="Timesteps at which to extract samples.")
    parser.add_argument("--point1", nargs=2, type=float,
                        help="Radial and axial coordinates of first point of"
                             "line. First value is the radial position, second"
                             "value is the axial position.")
    parser.add_argument("--point2", nargs=2, type=float,
                        help="Radial and axial coordinates of second point of"
                             "line.First value is the radial position, second"
                             "value is the axial position.")
    parser.add_argument("--line-resolution", type=int, help="Resolution of "
                                                            "extracted lines.")
    parser.add_argument("--output-dir", type=str, help="Directory to write"
                                                       "csv dump.")
    return parser.parse_args()


FILE_TEMPLATE = Template("LINE_${number}_T=${timestep}.csv")
TARGET_DICT = {"lines": [{}]}
PI = np.pi
def create_line_definition(point_1, )

def main():
    args = parse_args()



if __name__ == "__main__":
    main()
