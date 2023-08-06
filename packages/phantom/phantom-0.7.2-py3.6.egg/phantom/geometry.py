"""
Geometrical transformations over images.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

from .utils import imshow


class Grid:
    """
    Represents a grid for grid tranform mappings.
    """
    def __init__(self, panels, size):
        self.panels = panels
        self.size = size
    
    def _draw_lines(self, img, color, thick, direction="h", debug=False):
        for panel in self.panels:
            p, q, r, s = map(tuple, panel)  # unpack the tuple
            print(f"p:{p}, q:{q}, r:{r}, s:{s}")
            if direction == "h":
                cv2.line(img, p, q, color, thickness=thick)
                cv2.line(img, p, r, color, thickness=thick)
                cv2.line(img, q, s, color, thickness=thick)
                cv2.line(img, r, s, color, thickness=thick)
            else:
                cv2.line(img, p, q, color, thickness=thick)
                cv2.line(img, p, s, color, thickness=thick)
                cv2.line(img, q, r, color, thickness=thick)
                cv2.line(img, r, s, color, thickness=thick)
            if debug:
                cv2.circle(img, p, thick, (  0,   0, 255), thickness=thick)
                cv2.circle(img, q, thick, (  0, 255, 255), thickness=thick)
                cv2.circle(img, r, thick, (  0, 255,   0), thickness=thick)
                cv2.circle(img, s, thick, (255, 255,   0), thickness=thick)
                break
        return None
    
    def _draw_points(self, img, color, thick):
        """
        Subclasses can define the logic for drawing this shape over an image,
        using points, however a base implementation is provided.
        """
        for panel in self.panels:
            for point in panel:
                cv2.circle(img, tuple(point), thick, color, thickness=thick)
        return None
    
    def equivalent(self, other):
        """
        Tests wether a grid is equivalent to another. That means, that both
        grids can be mapped between each other.
        """
        pass


def _borders(panel):
    """
    Returns the borders of a panel, where panel is an array of [x, y] x4 points
    that define the plane. It should come from a Grid instance.

    :param panel: ndarray of 4 [x, y] points that define the plane
    :return: tuple of leftmost, topmost, width and height of the region of
        interest for the plane
    """
    x = panel[:, 0]
    y = panel[:, 1]
    return x.min(), y.min(), x.max() - x.min(), y.max() - y.min()


def _split_line(line, steps=1):
    """
    Takes a line by segments (two points at each end) and splits it in half. The
    process can be repeated multiple times while preserving precision in the
    point locations.
    
    :param line: list of (x, y) tuples, at list two points long
    :param steps: number of times to perform line-splitting
    :return: list of (x, y) tuples
    """
    # TODO: extend the mechanism to work over curves
    line_ = line[:]
    for _step in range(steps):
        new_line = []
        for p1, p2 in zip(line_, line_[1:]):
            p_mid = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            new_line += [p1, p_mid]
        new_line.append(p2)  # and now we add the last point back
        line_ = new_line[:]
    new_line = [(round(x), round(y)) for x, y in new_line]
    return new_line


def grid_from_lines(lines, size=(1, 1)):
    """
    Helper function. Creates a Grid object from a sequence of lines. Order in
    the sequence matters. The assumed direction is top to bottom. All lines must
    have the same length. A line is expected to be a sequence of at least two
    tuples of (x, y) points in an image.
    
    No checks are done to see if the resulting Grid is meaningful -- that is
    left as an  excercise to the user.

    :param lines: list of lists, each being a list of (x, y) points
    :param size: numpy style tuple for the shape of the resulting Grid (used when
        transforming images through `grid_transform()`)
    :return: Grid object, with panels built from the lines passed
    """
    panels = []
    line_pairs = zip(lines, lines[1:])
    for p, q in line_pairs:
        for p1, p2, q1, q2 in zip(p, p[1:], q, q[1:]):
            panels.append(np.array([p1, p2, q2, q1]))
    return Grid(panels, size)


def grid_transform(source, grid_src, grid_dst, *, inter=cv2.INTER_CUBIC):
    """
    Applies a grid transform over an image.

    Maps the panels from grid_src to the correspondent panels on grid_dst
    using perspective transforms.

    :param source: source image to transform (ndarray/cv2 image)
    :param grid_src: Grid which defines the region-of-interest (ROI) over
        the source image.
    :param grid_dst: Grid which defines the mapping of grid_src over the
        transformed image.
    :return:
    """
    size = grid_dst.size
    if len(source.shape) == 3:
        size += (source.shape[2],)
    out = np.zeros(size)
    for src, dst in zip(grid_src.panels, grid_dst.panels):
        x, y, w, h = _borders(src)
        roi = source[y: y + h, x: x + w]  # it seems we're not using the ROI yet
        x, y, w, h = _borders(dst)
        t_dst = dst - [x, y]  # transform the dst positions to render-coordinates
        mask = np.zeros((h, w, 3), dtype=np.float32)
        cv2.fillConvexPoly(mask, t_dst, (1.0, 1.0, 1.0))
        imask = -1. * (mask - 1)
        hom, _status = cv2.findHomography(np.float32(src), np.float32(t_dst))
        render = cv2.warpPerspective(source, hom, (w, h), flags=inter, borderMode=cv2.BORDER_DEFAULT)
        #print(f"out.shape: {out.shape}")
        #print(f"y:{y} h:{h} x:{x}, w:{w}, x+w{x+w}")
        d_roi_pos = (slice(y, y + h), slice(x, x + w))# y: y + h, x: x + w
        #print(f"d_roi_pos: {d_roi_pos}")
        d_roi = out[d_roi_pos]
        #imshow(render * mask)
        #print(f"d_roi.shape:{d_roi.shape}, imask.shape:{imask.shape}")
        #imshow(imask)
        #imshow(d_roi)
        #imshow(d_roi * imask)
        #print(f"y:{y} h:{h} x:{x}, w:{w}, dst:{dst}, t_dst:{t_dst}")
        out[y: y + h, x: x + w] = (render * mask) + (d_roi * imask)
    return out.astype(np.uint8)
