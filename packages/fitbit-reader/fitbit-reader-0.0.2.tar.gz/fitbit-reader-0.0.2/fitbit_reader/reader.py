import fitbit_reader.gather_keys_oauth2 as Oauth2
import fitbit_reader.fitbit_steps_tools as tools

import fitbit
import pandas as pd
import datetime


class FitbitReader:

    def __init__(
            self,
            client_id,
            client_secret,
            min_steps_for_entry_to_be_active=20,
            max_contiguous_non_active_entries_for_continuous_session=3,
            min_consecutive_active_entries_to_count_as_activity=10,
    ):

        server = Oauth2.OAuth2Server(client_id, client_secret)
        server.browser_authorize()
        ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
        REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
        self._client = fitbit.Fitbit(
            client_id,
            client_secret,
            oauth2=True,
            access_token=ACCESS_TOKEN,
            refresh_token=REFRESH_TOKEN,
        )

        self._min_steps_for_entry_to_be_active = min_steps_for_entry_to_be_active
        self._max_contiguous_non_active_entries_for_continuous_session = \
            max_contiguous_non_active_entries_for_continuous_session
        self._min_consecutive_active_entries_to_count_as_activity = \
            min_consecutive_active_entries_to_count_as_activity

    def get_total_active_steps(
            self,
            date='today',
            steps_column="Steps",
    ):
        steps = self.get_intraday_steps_dataframe(
            date,
            detail_level='1min',
            steps_column=steps_column,
        )
        return tools.get_total_active_steps(
            steps,
            min_steps_for_entry_to_be_active=
            self._min_steps_for_entry_to_be_active,
            max_contiguous_non_active_entries_for_continuous_session=
            self._max_contiguous_non_active_entries_for_continuous_session,
            min_consecutive_active_entries_to_count_as_activity=
            self._min_consecutive_active_entries_to_count_as_activity
        )

    def get_active_steps_dataframe(
            self,
            date='today',
            steps_column="Steps",
    ):
        steps = self.get_intraday_steps_dataframe(
            date,
            detail_level='1min',
            steps_column=steps_column,
        )
        return tools.get_active_steps_dataframe(
            steps,
            min_steps_for_entry_to_be_active=
            self._min_steps_for_entry_to_be_active,
            max_contiguous_non_active_entries_for_continuous_session=
            self._max_contiguous_non_active_entries_for_continuous_session,
            min_consecutive_active_entries_to_count_as_activity=
            self._min_consecutive_active_entries_to_count_as_activity
        )

    def get_active_steps_dataframes(
            self,
            date='today',
            steps_column="Steps",
    ):
        steps = self.get_intraday_steps_dataframe(
            date,
            detail_level='1min',
            steps_column=steps_column,
        )
        return tools.get_active_steps_dataframes(
            steps,
            min_steps_for_entry_to_be_active=
            self._min_steps_for_entry_to_be_active,
            max_contiguous_non_active_entries_for_continuous_session=
            self._max_contiguous_non_active_entries_for_continuous_session,
            min_consecutive_active_entries_to_count_as_activity=
            self._min_consecutive_active_entries_to_count_as_activity
        )

    def get_intraday_steps_dataframe(
            self,
            date='today',
            detail_level='1min',
            steps_column="Steps",
            time_column="Time",
    ):

        if type(date) is datetime.datetime:
            date = FitbitReader.datetime_to_string(date)

        steps_data = self._client.intraday_time_series(
            'activities/steps',
            base_date=date,
            detail_level=detail_level,
        )

        time_list = []
        val_list = []
        for i in steps_data['activities-steps-intraday']['dataset']:
            val_list.append(i['value'])
            time_list.append(i['time'])
        return pd.DataFrame({steps_column: val_list, time_column: time_list})

    def get_total_steps(self, date='today'):

        if type(date) is datetime.datetime:
            date = FitbitReader.datetime_to_string(date)

        time_series = int(self._client.time_series(
            'activities/tracker/steps',
            base_date=date,
            period='1d'
        )['activities-tracker-steps'][0]['value'])

        return time_series

    def get_last_sync(
            self,
            device_num=0,
            datetime_string_format='%Y-%m-%dT%H:%M:%S.%f',
    ):
        """
        :param device_num:
            This can be modified if multiple people are connected to the same
            fitbit app.
        :param datetime_string_format:
            A string that tells how to parse fitbit's returned date time string.
            See the following for datetime_format codes
            https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
        :return:
            A datetime object with the last sync time.
        """
        last_sync_str = self._client.get_devices()[device_num]['lastSyncTime']
        return datetime.datetime.strptime(last_sync_str, datetime_string_format)

    @staticmethod
    def datetime_to_string(date):
        return date.strftime('%Y-%m-%d')


