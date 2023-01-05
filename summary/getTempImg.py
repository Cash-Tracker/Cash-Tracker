import tempfile
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def getTempImg(lables, vals):
    matplotlib.use("Agg")
    color = ['#47CACC','#F3ABB6','#A8E6CE','#D67280']
  

    def make_autopct(sizes):
        def my_autopct(pct):
            total = sum(sizes)
            val = int(round(pct*total/100.0))
            return '{p:.2f}%  ₹{v:d}'.format(p=pct,v=val)  # add rupee symbol
        return my_autopct
    plt.pie(vals, labels = lables, colors=color,autopct=make_autopct(vals) )
    plt.axis('equal')
    
    
    
    temp = tempfile.NamedTemporaryFile(suffix='.jpg')
    plt.savefig(temp, format = 'jpg')
    plt.clf()
    temp.seek(0)
    return temp