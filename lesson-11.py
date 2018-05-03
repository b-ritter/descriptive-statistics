import math
import statistics as s
from salaries import salaries as sal2


salaries = [
  38946,
  43420,
  49191,
  50430,
  50557,
  52580,
  53595,
  54135,
  60181,
  62076
]

def pstdev(sal):
  return math.sqrt(s.pvariance(sal))

m = s.mean(salaries)
standard_dev_sample = math.sqrt(sum([math.pow(sal - m, 2) for sal in salaries])/(len(salaries)-1))
standard_dev_population = math.sqrt(sum([math.pow(sal - m, 2) for sal in salaries])/(len(salaries)))


# print(pstdev(sal2))

pop = [18, 20, 23, 22, 21, 15, 17, 18, 21]

print(pstdev(pop))