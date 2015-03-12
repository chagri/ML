import numpy as np
from scipy.stats import kstest
from scipy.stats import ks_2samp
from scipy.stats import spearmanr
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_1samp
import scipy 


def corr(X,Y):
	return np.corrcoef(X,Y)[0,1]

def ks2sample(X,Y):
	D,p = ks_2samp(X, Y)
	return (D,p)
# D static 2 sided p value: If the K-S statistic is small or the p-value is high, 
# then we cannot reject the hypothesis that the distributions of the two samples are the same.

def spearman(X,Y):
	rho, p = spearmanr(X,Y)
	return (rho, p)

def tTest(X,m):
	# parametric : particularly considers normal distribution
	t, p = ttest_1samp(x, m)
	return (t,p)

def manwhitneyUtest(X,Y):
	# non-parametric T test
	return mannwhitneyu(X,Y)[1]


X = [1,2,3,4]
Y = [4,5,1,3]

print corr(X,Y)
D,p = ks2sample(X,Y)
print D,p
print manwhitneyUtest(X,Y)


def rms_error(predictions, targets):
    return math.sqrt(ms_error(predictions, targets))

def ms_error(predictions, targets):
    return mean([(p - t)**2 for p, t in zip(predictions, targets)])

def mean_error(predictions, targets):
    return mean([abs(p - t) for p, t in zip(predictions, targets)])

def mean_boolean_error(predictions, targets):
    return mean([(p != t)   for p, t in zip(predictions, targets)])