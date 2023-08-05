import pandas as pd

from robotpt_common_utils import pandas_lib


def get_total_active_steps(
    dataframe,
    min_steps_for_entry_to_be_active,
    max_contiguous_non_active_entries_for_continuous_session,
    min_consecutive_active_entries_to_count_as_activity,
    steps_column="Steps"
):
    dataframe = get_active_steps_dataframe(
        dataframe,
        min_steps_for_entry_to_be_active,
        max_contiguous_non_active_entries_for_continuous_session,
        min_consecutive_active_entries_to_count_as_activity,
        steps_column=steps_column
    )

    if dataframe is None:
        return 0
    else:
        return dataframe[steps_column].sum()


def get_active_steps_dataframe(
        dataframe,
        min_steps_for_entry_to_be_active,
        max_contiguous_non_active_entries_for_continuous_session,
        min_consecutive_active_entries_to_count_as_activity,
        steps_column="Steps"
):
    dataframes = get_active_steps_dataframes(
        dataframe,
        min_steps_for_entry_to_be_active,
        max_contiguous_non_active_entries_for_continuous_session,
        min_consecutive_active_entries_to_count_as_activity,
        steps_column=steps_column
    )
    if len(dataframes) > 0:
        return pd.concat(dataframes)
    else:
        return None


def get_active_steps_dataframes(
        dataframe,
        min_steps_for_entry_to_be_active,
        max_contiguous_non_active_entries_for_continuous_session,
        min_consecutive_active_entries_to_count_as_activity,
        steps_column="Steps"
):
    df_with_enough_steps = dataframe.where(
        dataframe[steps_column] >= min_steps_for_entry_to_be_active
    )
    df_ = pandas_lib.remove_consecutive_nans(
        df_with_enough_steps,
        steps_column,
        max_contiguous_non_active_entries_for_continuous_session
    )
    activity_dfs = pandas_lib.split_on_nan(df_, steps_column)

    return [
            df
            for df in activity_dfs
            if len(df) >= min_consecutive_active_entries_to_count_as_activity
        ]


if __name__ == '__main__':

    dataframe_ = pd.DataFrame({
        "Steps":
            [40, 42, 40, 20, 0, 45, 42, 0, 0, 0, 50, 50, 52],
        "Steps2":
            [40, 42, 40, 20, 0, 45, 42, 0, 0, 0, 50, 50, 52],
    })
    steps = get_total_active_steps(dataframe_, 40, 2, 5)
    print(steps)

