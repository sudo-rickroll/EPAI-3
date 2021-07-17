from namedtuples import *
import pytest
from time import perf_counter

num_profiles = 10000
num_times_to_run = 5

def test_fake_profiles():

    @fake_profiles(num_profiles,'dict')
    def check_size(arr):
        return len(arr)

    assert check_size() == num_profiles, "Specified Number of profiles not fetched"

def test_profile_output_namedtuple():

    most_common_bloodgroup, average_location, oldest_age, average_age = calculate_stats_namedtuple()
    assert oldest_age >= average_age, "Oldest age cannot be lesser than average age in the namedtuple"

def test_profile_output_dict():

    most_common_bloodgroup, average_location, oldest_age, average_age = calculate_stats_dict()
    assert oldest_age >= average_age, "Oldest age cannot be lesser than average age in the dictionary"

def test_time_to_run():
    namedtuple_is_faster = False
    for i in range(num_times_to_run):
        start_namedtuple = perf_counter()
        _, _, _, _ = calculate_stats_namedtuple()
        end_namedtuple = perf_counter()

        time_namedtuple = end_namedtuple - start_namedtuple

        start_dict = perf_counter()
        _, _, _, _ = calculate_stats_dict()
        end_dict = perf_counter()

        time_dict = end_dict - start_dict

        if time_namedtuple < time_dict:
            namedtuple_is_faster = True
            break
    
    assert namedtuple_is_faster, "namedtuple is slower than dictionary"

def test_len():
    @fake_profiles(num_profiles,'dict')
    def check_size_dict(arr):
        return len(arr)

    @fake_profiles(num_profiles,'namedtuple')
    def check_size_namedtuple(arr):
        return len(arr)

    assert check_size_dict() == check_size_namedtuple(), "Size of Dictionary and namedtuple do not match"

    
