def print_df(df):
    from tabulate import tabulate
    # import pandas as pd
    # pd.set_option('display.unicode.ambiguous_as_wide', True)
    print(tabulate(df, headers='keys', tablefmt='psql'))

