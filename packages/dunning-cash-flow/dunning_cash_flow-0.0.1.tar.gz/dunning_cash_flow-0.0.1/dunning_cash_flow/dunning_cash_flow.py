# -*- coding: utf-8 -*-

import countries_utils
from pandas.io.json import json_normalize
import datetime as dt
import inspect
import json
import logging
import numpy as np
import os
import pandas as pd
import requests
import sys

"""
environment variables

apiToken=twikey-api-token
apiUrl=https://api.beta.twikey.com | https://api.twikey.com
authorizationUrl=/api/twikeyauthentication/authorization/code
serverUrl=https://dunningcashflow-api.azurewebsites.net
transactionFeedUrl=/creditor/transaction
twikeyApiToken=<40 chars>
"""


class DunningCashflow:
    def __init__(self, caller="DunningCashflow"):
        logging.info(
            f"{'='*25} {inspect.currentframe().f_code.co_name}"
        )
        logging.info(f"caller : {caller}")


class Authentication:
    """
    Twikey authentication
    https://www.beta.twikey.com/api/index.html#authentication
    """
    api_token = None
    url = None
    authorization = None

    def __init__(self,  caller="Authentication"):
        logging.info(
            f"{'='*25} {inspect.currentframe().f_code.co_name}"
        )
        logging.info(f"caller : {caller}")

    def login(self, api_token="empty", url=f"{os.environ['apiUrl']}/creditor"):

        logging.debug(
            "%s %s - %s",
            "="*10,
            "Authentication",
            inspect.currentframe().f_code.co_name
        )
        self.api_token = api_token
        self.url = url
        url = url  # e.g; "https://api.beta.twikey.com/creditor"

        payload = "apiToken={}&otp=".format(self.api_token)

        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'User-Agent': "altf1bepython/0.0.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "api.beta.twikey.com",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        try:
            response = requests.request(
                "POST",
                url,
                data=payload,
                headers=headers
            )
        except requests.exceptions.ConnectionError as e:
            logging.exception(e)
            logging.warning("Check the internet connectivity")
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            logging.exception(e)
            logging.warning("Run Python 3.6 at least")
            logging.warning(
                "Install the SSL Module if the SSL module IS NOT available : `pip install pyOpenSSL`")
            sys.exit(1)

        self.authorization = json.loads(response.text)
        logging.debug(f"Response authorization is {response.text}")


class Transactions:
    """
    Transactions
    https://www.twikey.com/api/index.html#transaction-feed
    """
    tx_json = None
    tx_json_raw = None
    external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
    app = None
    df = None
    bkerrors = None
    contract_ids = None
    transactions_range = None
    bkdate_start = None
    bkdate_end = None
    bkdate_min_year = None
    bkdate_max_year = None
    bkdates_in_weeks_dict = None
    bkdates_in_months_dict = None
    bkerrors_only = None

    # brussels = timezone("Europe/Brussels")
    # now = dt.datetime.now(tz=brussels)

    def __init__(self, caller=None):
        """
        Initialize data of the Transactions Class
        """
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")
        logging.info(f"caller : {caller}")

    def setup(self):
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")
        self.get_transactions()
        self.df = self.get_df()

    def filter_dataframe(self, bkerrors_statuses, contract_ids, month_slider):
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")

        logging.info(f"bkerrors_statuses : {bkerrors_statuses}")
        logging.info(f"contract_ids : {contract_ids}")
        logging.info(f"month_slider : {month_slider}")
        logging.info(
            f"Start date slider: {self.get_transactions_range()[month_slider[0]]}, "
            f"End date slider: {self.get_transactions_range()[month_slider[1]] + pd.offsets.MonthEnd(n=1)}"
        )
        logging.debug(
            f"bkerror : {self.df['bkerror']}"
        )
        logging.debug(
            f"bkerror is in bkerrors_statuses? : {self.df['bkerror'].isin(bkerrors_statuses)}")

        logging.debug(
            f"contractId is in contract_ids? : {self.df['contractId'].isin(contract_ids)}"
        )
        logging.debug("bkdate.head(1) %s", self.df["bkdate"].head(1))

        dff = self.df[
            self.df["bkerror"].isin(bkerrors_statuses)
            & self.df["contractId"].isin(contract_ids)
            & (self.df["bkdate"] >= (self.get_transactions_range()[month_slider[0]]))
            & (self.df["bkdate"] <= (self.get_transactions_range()[month_slider[1]]
                                     + pd.offsets.MonthEnd(n=1)))
        ]

        logging.info(f"len(dff): {len(dff)}")
        logging.debug(f"dff : {dff}")
        return dff

    def set_bkdates(self):
        """
            set bkdates linked to the error codes generated when
            a transactions failed bkdates are the dates used to
            filter and select the error codes to produce
            charts (RangeSlider, Bar Charts...)
        """
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")
        self.bkdate_min_year = self.df["bkdate"].min().year
        self.bkdate_max_year = self.df["bkdate"].max().year

        self.bkdate_start = dt.date(self.bkdate_min_year, 1, 1)
        self.bkdate_end = dt.date(self.bkdate_max_year, 12, 31)

        bkdates_in_weeks = pd.date_range(
            start=self.bkdate_start, end=self.bkdate_end, freq="W")
        bkdates_in_weeks = pd.Series(bkdates_in_weeks)
        self.bkdates_in_weeks_dict = dict(
            zip(bkdates_in_weeks.index.format(), bkdates_in_weeks))

        bkdates_in_months = pd.date_range(
            start=self.bkdate_start, end=self.bkdate_end, freq="M")
        bkdates_in_months = bkdates_in_months.strftime("%b '%y")
        bkdates_in_months = pd.Series(bkdates_in_months)
        self.bkdates_in_months_dict = dict(
            zip(bkdates_in_months.index.format(), bkdates_in_months))

        logging.info("bkdate_min_year : %s, bkdate_max_year : %s",
                     self.bkdate_min_year, self.bkdate_max_year)
        logging.info('df["bkdate"].min() : %s, df["bkdate"].max() : %s',
                     self.df["bkdate"].min(), self.df["bkdate"].max())
        logging.info("bkdates_in_months_dict : %s",
                     self.bkdates_in_months_dict)

    def get_df(self):
        """
        normalize the json transactions.
        df contains all entries
        columns : id, contractId, mndtId, contract, amount, msg,
        place, ref, date, final, state, bkerror, bkmsg, bkdate,
        bkamount, reqcolldt
        """

        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")
        if self.tx_json is None:
            self.get_transactions()
        if self.df is None:
            try:
                logging.info('%s tx_json : %s', '*'*40, self.tx_json[:50])
                self.df = pd.read_json(
                    self.tx_json,
                    encoding="utf-8"
                )
            except ValueError as e:
                # See https://books.google.be/books?id=xYmNDQAAQBAJ&pg=PA184&lpg=PA184&dq=%22ValueError:+Trailing+data%22
                logging.error(
                    '%s ValueError : tx_json : %s',
                    '*'*40, self.tx_json[:25]
                )
                logging.exception(e, exc_info=True)
            except Exception as e:
                logging.error(
                    'Exception : json : %s',
                    self.tx_json
                )
                logging.exception(
                    e,
                    exc_info=True
                )
                sys.exit(1)

            self.df = json_normalize(
                self.df["Entries"]
            )

        self.df["bkdate"] = pd.to_datetime(self.df["bkdate"]).dt.date
        self.df["date"] = pd.to_datetime(self.df["date"]).dt.date
        self.df[["bkerror", "bkmsg"]] = self.df[
            ["bkerror", "bkmsg"]
        ].fillna("PAID")

        self.set_bkdates()

        return self.df

    def get_bkerror_status_options(self):
        """
        get unique [bkerrors, bkmsg] in a list
        """
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")
        return [
            {"label": str(self.get_bkerrors()[bkerror_status]),
             "value": str(bkerror_status)}
            for bkerror_status in self.get_bkerrors()
        ]

    def get_bkerrors_only(self):
        """
        get all bk errors having a state==error in a dict
        All bk errors except PAID
        """
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")
        if self.bkerrors_only is None:
            self.bkerrors_only = dict(self.get_bkerrors())
            del self.bkerrors_only["PAID"]
        logging.info("self.bkerrors_only : %s ", self.bkerrors_only)
        return self.bkerrors_only

    def get_bkerrors(self):
        """
        get unique [bkerrors, bkmsg] in a dict
        """
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")
        if self.bkerrors is None:
            if self.df is None:
                self.df = self.get_df()
            bkerrors = self.df[["bkerror", "bkmsg"]].fillna("PAID")
            bkerrors = bkerrors.sort_values(by="bkerror")
            bkerrors = bkerrors.drop_duplicates(keep="first")
            bkerrors = bkerrors.set_index("bkerror")["bkmsg"].to_dict()
            self.bkerrors = bkerrors
        # logging.debug("get_bkerrors")
        # logging.debug(self.bkerrors)
        return self.bkerrors

    def get_contract_id_options(self):
        """
        get unique contract ids in a list
        """
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")
        return [
            {"label": str(contract_ids),
             "value": str(contract_ids)}
            for contract_ids in self.get_contract_ids()
        ]

    def get_contract_ids(self):
        """
        get unique contract ids in a dict
        """
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")

        if self.contract_ids is None:
            if self.df is None:
                self.df = self.get_df()
            contract_ids = self.df["contractId"]
            contract_ids = contract_ids.sort_values().unique()
            # contract_ids = contract_ids.sort_values()
            # contract_ids = contract_ids.drop_duplicates(keep="first")
            # contract_ids = contract_ids.to_dict()
            self.contract_ids = contract_ids

        return self.contract_ids

    def get_transactions_range(self):
        """
        get the range in months containing transactions in Twikey
        example: DatetimeIndex(["2019-01-01", "2019-02-01",
                "2019-03-01", "2019-04-01",
               "2019-05-01", "2019-06-01", "2019-07-01", "2019-08-01",
               "2019-09-01", "2019-10-01", "2019-11-01", "2019-12-01"],
        """
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")
        if self.transactions_range is None:
            self.transactions_range = pd.date_range(
                start=self.bkdate_start,
                end=self.bkdate_end,
                freq=pd.offsets.MonthBegin(n=1)
            )
        return self.transactions_range

    def get_transactions(self):
        """
        download and serialize the transactions for the logged user
        """
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")

        # e.g. "https://dunningcashflow-api.azurewebsites.net/creditor/transaction"
        url = f"{os.environ['serverUrl']}/creditor/transaction"
        # "Host": "dunningcashflow-api.azurewebsites.net",
        headers = {
            "User-Agent": "altf1bepython/0.0.0",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "cache-control": "no-cache"
        }

        try:
            response = requests.request("GET", url=url, headers=headers)
        except requests.exceptions.ConnectionError as e:
            logging.exception(e)
            logging.warning("Check the internet connectivity")
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            logging.exception(
                e
            )
            logging.warning(
                "Run Python 3.7 at least"
            )
            logging.warning(
                "Install the SSL Module if the SSL module IS NOT available : `pip install pyOpenSSL`"
            )
            sys.exit(1)

        logging.info(f'Fetched. Code: {response.status_code}')
        logging.info(f'Fetched. headers: {response.headers}')
        logging.info(f'Response.txt: {response.text[:100]}')
        self.tx_json_raw = response.text
        self.tx_json = json.loads(response.text)

    def transactions_per_countries(self):
        if self.df is None:
            self.df = self.get_df()
        country_iso_list, self.country_iso_set = countries_utils.get_list_of_countries_in_text(
            self.df,
            "place",
            languages_to_check=["en", "fr", "nl"]
        )
        self.country_iso_set = np.array(self.country_iso_set)
        logging.debug(
            f"country_iso_set : {self.country_iso_set}"
        )

        self.df["country_iso"] = country_iso_list

        self.df_pivot = pd.pivot_table(
            self.df,
            values="amount",
            index="country_iso",
            # index=["bkerror"],
            aggfunc=np.sum,
            fill_value=0
        )
        self.df_pivot.reset_index(level=0, inplace=True)
        return self.df_pivot

    def get_output_directory(self):
        """
        return the path where temporary files are stored
        """
        out_directory = os.path.join(os.getcwd(), "app", "output-generated")
        if not os.path.exists(out_directory):
            os.makedirs(out_directory)

        logging.debug("output directory is {}".format(out_directory))
        return out_directory

    def export_to_json(self, data, filename="export_to_json.json"):
        """
        export a DataFrame in a json file using filename as parameter
        """
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")

        out_directory = self.get_output_directory()
        logging.debug("data : %s", data)
        try:
            with open(
                os.path.join(out_directory, "_str_" + filename), "w", encoding='utf-8'
            ) as outfile:
                outfile.write(json.loads(data))

        except IOError:
            logging.warning("Could not save the file!, %s", sys.exc_info()[0])

        try:
            with open(
                os.path.join(out_directory, "_obj_" + filename), "w", encoding='utf-8'
            ) as write_file:
                json.dump(data, write_file)

        except IOError:
            logging.warning("Could not save the file! %s", sys.exc_info()[0])

    def export_to_excel(self, df, filename="export_to_excel.xlsx"):
        """
        export a DataFrame in a xlsx file using filename as parameter
        """
        logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")
        out_directory = self.get_output_directory()

        try:
            df.to_excel(os.path.join(out_directory, filename))
        except IOError:
            logging.warning("Could not save the file! Please close Excel!")


if __name__ == "__main__":
    Auth = Authentication()
    # {"code":"err_not_authorised","message":"Not authorised"}
    if 'twikeyApiToken' not in os.environ:
        print(f"set the twikeyApiToken environment variable")
        exit(1)

    Auth.login(api_token=os.environ['twikeyApiToken'])
    authorization = Auth.authorization

    if authorization is None:
        # TODO: indicate that the authorization code or the URL is incorrect
        print(f"authorization {None}")
    else:
        print(f"authorization  : {authorization}")

    if hasattr(authorization, "code"):
        print(f"code {authorization['code']}")
    # elif hasattr(authorization, "Authorization"):
    #     print(f"authorization %s", authorization["Authorization"])
    if hasattr(authorization, "message"):
        print(f"message {authorization['message']}")
    