import seaborn as sns
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

class Reps:

    def __init__(self, name, reps, rampup=0.0):
        self.rampup = rampup
        self.name = name
        self.reps = reps

    def program(self, strategy, weight, step):
        l = len(self.reps)
        f = 1.0 - (l*self.rampup)
        reps = []
        for r in self.reps:
            f = f + self.rampup
            w = round(float(weight * strategy['ratio'] * f)/step) * step
            reps.append({'reps': r, 'weight': w})
        return reps


class Sets:
    """Sets logic containing a set of Reps logic objects."""

    def __init__(self, name, reps):
        self.name = name
        self.data = {}
        for r in reps:
            self.data[r.name] = r

    def program(self, strategy, weight, step):
        return self.data[strategy['reps']].program(strategy, weight, step)


class Modulation:
    """ Modulation logic containing a list of Set rules."""

    def __init__(self,sets):
        self.data = {}
        for s in sets:
            self.data[s.name] = s

    def program(self, strategy, weight, step):
        return self.data[strategy['sets']].program(strategy, weight, step)


class Exercise:
    """ Exercise to perform.
    An exercise has a name, a weight unit ('Kg' by default), weight
    increment step (5 by default), sets and reps that are set by
    using a Modulation object.
    """
    def __init__(self, name, modulation=None, unit="Kg", step=5):
        self.name = name
        self.sets = {}
        self.reps =  {}
        self.set_modulation(modulation)
        self.set_step(step)
        self.unit = unit

    def set_modulation(self, m):
        self.modulation = m

    def set_step(self,v):
        self.step = v

    def set_one_rep_max(self,v):
        self.orm = v

    def program(self,strategy):
        data = self.modulation.program(strategy, self.orm, self.step)
        return {'exercise':self.name,
                'sets':data,
                'unit':self.unit,
                'obj':self}


class Group:
    """ Group a list of Exercises or other Groups.
    A group will apply the training program on any contained items
    using a defined sets or reps selected and a weight ratio.
    """
    def __init__(self, name=None, sets_selector=None, reps_selector=None,
            ratio=1.0, fixed_ratio=0, plan=None):
        self.name = name
        self.sets_selector = sets_selector
        self.reps_selector = reps_selector
        self.ratio = ratio
        self.fixed_ratio = fixed_ratio
        self.parts = {}
        self.plan(plan)

    def plan(self, l):
        if l:
            for i in l:
                self.parts[i.name] = [i]
        return self

    def program(self, strategy=None):
        if strategy==None:
            strategy = {'ratio':1}
        tmp = strategy.copy()
        self.augment(tmp)
        ret = {}
        for p in self.parts:
            ret[p] = []
            for k in self.parts[p]:
                data = k.program(tmp)
                ret[p].append(data)
        return ret

    def augment(self, strategy):
        if self.sets_selector:
            strategy['sets'] = self.sets_selector
        if self.reps_selector:
            strategy['reps'] = self.reps_selector
        if self.fixed_ratio>0:
            strategy['ratio'] = self.fixed_ratio
        else:
            strategy['ratio'] = strategy['ratio'] * self.ratio

    def __str__(self):
        return self.print_block(self.program({'ratio':1}))

    def print_block(self, d, level=0):
        ret = ''
        for k in d:
            if k=='exercise':
                reps = []
                for r in d['sets']:
                    reps.append('%d x %.1f%s' % (r['reps'],
                                                 r['weight'],
                                                 d['unit']))
                ret = ret + '\t'*(level) + ' | '.join(reps) + '\n'
                break
            else:
                ret = ret + '\t'*level + k + '\n'
                for v in d[k]:
                    ret = ret + self.print_block(v, level+1)
        return ret

    def exercises(self, filter):
        return self._exercises(self.program({'ratio':1}), filter)

    def _exercises(self, d, filter):
        for k in d:
            if k=='exercise':
                if filter==None or d[k]==filter:
                    yield(d)
                break
            else:
                for v in d[k]:
                    yield from self._exercises(v, filter)


def volume(i):
    def inner(i):
        for x in i:
            reps = 0
            for s in x['sets']:
                reps = reps + s['reps']
            yield {'exercise':x['exercise'], 'volume':reps}
    return 'volume', [x for x in inner(i)]


def tonage(i):
    def inner(i):
        for x in i:
            total = 0
            reps = 0
            for s in x['sets']:
                total = total + s['reps'] * s['weight']
                reps = reps + s['reps']
            yield {'exercise':x['exercise'], 'tonage':total}
    return 'tonage', [x for x in inner(i)]


def intensity(i):
    def inner(i):
        for x in i:
            total = 0
            reps = 0
            for s in x['sets']:
                total = total + s['reps'] * s['weight']
                reps = reps + s['reps']
            yield {'exercise':x['exercise'],
                   'intensity':total/reps/x['obj'].orm}
    return 'intensity', [x for x in inner(i)]


def dataframe(exercises):
    label, iterator = exercises
    data = {'workout':[],label:[]}
    i=0
    for x in iterator:
        i=i+1
        data['workout'].append(i)
        data[label].append(x[label])
    return label, data


def plotCompare(d1, d2):
    label1, df1 = dataframe(d1)
    label2, df2 = dataframe(d2)
    sns.lineplot(x='workout', y=label1,
                 marker='o',
                 legend='full',
                 data=pd.DataFrame(df1))
    ax2 = plt.twinx()
    sns.lineplot(x='workout', y=label2,color='r',
                 marker='o',
                 legend='full',
                 data=pd.DataFrame(df2), ax=ax2)
    plt.show()


def plotData(d1):
    label1, df1 = dataframe(d1)
    sns.lineplot(x='workout', y=label1,
                 marker='o',
                 legend='full',
                 data=pd.DataFrame(df1))
    plt.show()
