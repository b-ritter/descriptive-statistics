import math
import statistics as st

from friends import friends
from memory_scores import recognition, temporal

distance = lambda inp: math.sqrt(math.pow(inp, 2))

mean = st.mean(friends)

print(f"mean: {mean}")

deviations_from_mean = [friend - mean for friend in friends]

print(sum(deviations_from_mean)/len(friends)) # About equal to 0

squared_deviations_from_mean = [math.pow(friend - mean, 2) for friend in friends]

print(f'sum of squared deviations: {sum(squared_deviations_from_mean)}')

variance = st.pvariance(friends)
print(f'variance: {variance}')

standard_deviation = math.sqrt(variance)
print(f'standard deviation: {standard_deviation}')

one_stdv_above = mean + standard_deviation
print(f'one standard deviation above mean: {one_stdv_above}')

one_stdv_below = mean - standard_deviation
print(f'one standard deviation below mean: {one_stdv_below}')

middle_of_distro = len([friend for friend in friends if friend >= one_stdv_below and friend <= one_stdv_above])

ratio_of_middle_distro_to_total = middle_of_distro / len(friends)

print(f'{ratio_of_middle_distro_to_total} of Udacians have friends within one standard deviation of mean')

sample_std_dev = st.stdev(friends)
print(f'Sample standard deviation {sample_std_dev}')

pstdev = lambda vals: math.sqrt(st.pvariance(vals))


temporal_st_dev = pstdev(temporal)

print(f'Temporal Standard Deviation: {temporal_st_dev}')

recognition_st_dev = pstdev(recognition)
print(f'Recognition Standard Deviation: {recognition_st_dev}')