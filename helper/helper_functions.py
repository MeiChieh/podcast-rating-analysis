import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from termcolor import cprint
import sqlite3
from collections import Counter
import os
import duckdb
from scipy.stats import binomtest


# plotting related
def s():
    """
    Lazy function for plt.show()
    """
    plt.show()


def fs(w=3, h=3):
    """
    Lazy function for setting figure size

    Args:
        w (int, optional): set fig width. Defaults to 3.
        h (int, optional): set fig length. Defaults to 3.
    """
    plt.figure(figsize=(w, h))


def bprint(input):
    """
    Style printing

    Args:
        input (any): content to print
    """
    cprint(f"\n{input}", "cyan", attrs=["bold"])


def round_percent(val, has_percent=False):
    """
    Return float in percentage rounded to 2nd digit

    Args:
        val (float): float to round
        has_percent (bool, optional): whether percentage sign should be shown. Defaults to False.

    Returns:
        rounded_num (float/ string): if has_percent, return string (val%), else return int(%)
    """
    result = round(val * 100, 2)
    if has_percent:
        return f"{result}%"
    else:
        return result


def mark_bar(plot):
    """
    Append bar values on the bars

    Args:
        plot (matplotlib axis): plot
    """
    for i in plot.containers:
        plot.bar_label(
            i,
        )


def qry(query):
    """wrapper function for running duckdb query, and convert result to pandas dataframe

    Args:
        query (str): sql query

    Returns:
        query result: query result in pandas dataframe
    """
    return duckdb.sql(query).to_df()


def data_sampling(sample_target_df, sample_fraction):
    """
    wrapper function for pandas dataframe sampling, returns sample_df and sample size

    Args:
        sample_target_df (DataFrame): df to sample from

    Returns:
        sample_df (DataFrame): sample dataframe
        sample_fraction (int): percentage of sample_target_df as sample_df size
    """
    sample_df = sample_target_df.sample(replace=True, frac=sample_fraction)
    return (sample_df, len(sample_df))


def binomial_test(
    sample_p, population_p, alpha, total_trials, reject, fail_to_reject, alt=False
):
    """
    Wrapper function for doing binomial testing

    Args:
        sample_p (float): sample_proportion
        population_p (float): population_proportion
        alpha (float): significance level
        total_trials (int): number of trials to run
        reject (str): alternative hypothesis string
        fail_to_reject (str): null hypothesis string
        alt (('less' | 'greater'), optional): Single tail comparison. Defaults to False if two tailed test.
    """

    print(
        f"Sample proportion is: {round(sample_p, 4)}, Population proportion is: {round(population_p, 4)},\nsample proportion is smaller than population proportion,\ntest if this difference is significant:"
    )

    if alt == False:  # default two tails
        p_value = binomtest(int(sample_p * total_trials), total_trials, population_p)
    else:  # single tail
        p_value = binomtest(
            int(sample_p * total_trials), total_trials, population_p, alternative=alt
        )

    bprint("Binomial Test Results:")
    print(p_value)
    print(f"P-value: {p_value.pvalue} \n")
    print("p_value < alpha :", p_value.pvalue < alpha)

    # compare pvalue with alpha
    if p_value.pvalue <= alpha:
        print(f"=> Reject the null hypothesis: {reject}")
    else:
        print(f"=> Fail to reject the null hypothesis: {fail_to_reject}")
