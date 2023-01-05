import tempfile
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def getTempImg(lables, vals):
    matplotlib.use("Agg")
    plt.pie(vals, labels = lables)
    temp = tempfile.NamedTemporaryFile(suffix='.jpg')
    plt.savefig(temp, format = 'jpg')
    plt.clf()
    temp.seek(0)
    return temp