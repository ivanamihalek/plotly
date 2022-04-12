#!/usr/bin/python3 -u

import plotly.graph_objs as go


def clean(x):
    if x < 0: return 0
    if x > 1: return 1
    return x


def to255(x):
    if x < 0: return 0
    if x >= 1: return 255
    return round(255 * x, 0)


def score_to_rgb(genotype_score):
    cutoff_point = 0.15
    if genotype_score < cutoff_point:
        r = 1 - genotype_score / cutoff_point
        g = 0
        b = 1 - r
    else:
        r = 0
        g = (genotype_score - cutoff_point) / (1 - cutoff_point)
        b = 1 - g
    return [clean(r), clean(g), clean(b)]


def score_to_rgb_plotly(genotype_score):
    cutoff_point = 0.15
    if genotype_score < cutoff_point:
        r = 1 - genotype_score / cutoff_point
        g = 0
        b = 1 - r
    else:
        r = 0
        g = (genotype_score - cutoff_point) / (1 - cutoff_point)
        b = 1 - g
    return f"rgb({to255(r)}, {to255(g)}, {to255(b)})"


def plot3d(xs, ys, zs):

    colors = list(map(lambda z: score_to_rgb_plotly(z), zs))

    trace = go.Scatter3d(x=xs, y=ys, z=zs, mode='markers', marker=dict(size=10, color=colors, opacity=0.9))
    layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0))
    camera = dict(projection=dict(type="orthographic"))

    fig = go.Figure(data=[trace], layout=layout)
    fig.update_layout(scene_camera=camera)
    fig.show()

    return


def parse_input(infile):
    xs = []
    ys = []
    zs = []
    with open(infile) as inf:
        for line in inf:
            [x, y, z] = [float(s) for s in line.strip().split("\t")]
            xs.append(x)
            ys.append(y)
            zs.append(z)
    return [xs, ys, zs]


#########################################
def main():

    [xs, ys, zs] = parse_input("test.tsv")
    plot3d(xs, ys, zs)


#########################################
if __name__ == '__main__':
    main()
