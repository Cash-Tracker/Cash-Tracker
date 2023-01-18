import tempfile
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def getTempImg(lables, vals):
    matplotlib.use("Agg")
    color = ['#dcedc1',
            '#ffd3b6',
            '#ffaaa5',
            '#ff8b94',
            '#47CACC',
            '#F3ABB6',
            '#A8E6CE',
            '#D67280',
            '#F9E07F',
            '#94B447',
            '#ABD1DC',
            '#C9BBCB',
            '#3da4ab',
            '#f6cd61',
            '#fe8a71',
            '#ee4035',
            '#f37736',
            '#fdf498', 
            '#7bc043',
            '#0392cf'
            ]
  

    def make_autopct(sizes):
        def my_autopct(pct):
            total = sum(sizes)
            val = int(round(pct*total/100.0))
            return '{p:.2f}%  ₹{v:d}'.format(p=pct,v=val) 
        return my_autopct

    
    plt.pie(vals, labels = lables, colors=color,autopct=make_autopct(vals) )
    plt.axis('equal')
    
    
    
    temp = tempfile.NamedTemporaryFile(suffix='.jpg')
    plt.savefig(temp, format = 'jpg')
    plt.clf()
    temp.seek(0)
    return temp