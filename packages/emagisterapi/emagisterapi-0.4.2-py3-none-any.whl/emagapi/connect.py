import requests
import json
import numpy as np
from typing import List, Dict, Optional, Union
from urllib.parse import urlencode
from http import HTTPStatus


class Api:
    DOMAINS = {'es': 'www.emagister.com',
               'uk': 'www.emagister.co.uk',
               'fr': 'www.emagister.fr',
               'mx': 'www.emagister.com.mx'}

    BASE_API_URL = 'https://{}/api/'
    MAX_NUM_OF_CONSECUTIVE_ERRORS = 5
    ENCODING = 'utf-8'

    def __init__(self,
                 country: str = 'es',
                 version: str = '1.0',
                 page_size: int = 25,
                 silent: bool = True):
        """Api class constructor
        :param country: Country site
        :param version: Api version
        :param page_size: Number of records per page
        :param silent: Whether or not messages will be printed on the screen
        """
        self.country = country
        self.version = version
        self.page_size = page_size
        self.records = []
        self.silent = silent
        self.errors = 0
        self.url = None

    def get(self,
            subset: Optional[Union[List[str], Dict]] = None,
            filters: Optional[Dict] = None,
            max_records: Optional[int] = None) -> List:
        raise NotImplementedError

    def __record_data__(self, record: Dict, subset: Optional[Union[List[str], Dict]] = None) -> Dict:
        """ Takes specific values from a record and returns it
        :param record: A record from response
        :param subset: Fields to take from record. If it is empty, the complete record will be returned
        :return: A record
        """
        if not subset:
            return record

        data = {}

        if isinstance(subset, list):
            for key in subset:
                data[key] = record[key]

            return data

        if isinstance(subset, dict):
            for key, value in subset.items():
                data[key] = record[value]

            return data

        raise Exception('subset must be of type Dictionary or List')

    def __build_url__(self, resource: str, path: str = None, filters=None, page: int = 1):
        """ Builds the endpoint url with the base server url and adding parameters
        :param resource: API resource (courses, users, leads...)
        :param path: Endpoint path
        :param filters: Filters to apply, query parameters
        :param page: Page number
        """
        base_api_url = self.BASE_API_URL.format(self.DOMAINS[self.country])

        parameters = 'page={}&size={}'.format(page, self.page_size)

        if filters:
            parameters = '{}&{}'.format(parameters, urlencode(filters))

        url = '{}{}/'.format(base_api_url, self.version)

        if path:
            url = '{}{}/'.format(url, path.strip('/'))

        self.url = '{}{}?{}'.format(url, resource.strip('/'), parameters)

    def __read__(self) -> Dict:
        """ Gets response from API
        :return: JSON-formatted response from server
        """
        if not self.url:
            raise ValueError('url cannot be empty')

        response = requests.get(self.url)

        if response.status_code == HTTPStatus.OK:
            if not self.silent:
                print('GET: {} [{}]'.format(self.url, response.status_code))

            self.errors = 0

            return json.loads(response.content.decode(self.ENCODING))

        self.errors += 1
        error_message = 'GET: {} [{}] {}'.format(self.url, response.status_code, response.reason)
        if self.silent:
            print(error_message)

            if self.errors == self.MAX_NUM_OF_CONSECUTIVE_ERRORS:
                raise Exception('Maximum number of consecutive errors reached')

            return {}

        raise Exception(error_message)

    def __add_record__(self, record: Dict):
        """ Add a record to collection
        :param record: A record
        """
        self.records.append(record)

    def __get_records__(self) -> List:
        """ Return all records
        :return: A collection (list) of records
        """
        records = self.records
        self.records = []

        return records


class Courses(Api):
    def get(self,
            subset: Optional[Union[List[str], Dict]] = None,
            filters: Optional[Dict] = None,
            max_records: Optional[int] = None) -> List:
        """ Get courses collection from API
        :param subset: Subset of fields to retrieve. If None, all fields will be retrieved.
        :param filters: Dictionary of filters to apply. See https://www.emagister.com/api/doc#get--api-{version}-courses
        :param max_records: Maximum number of records to retrieve. If None, all records will be retrieved.
        :return: A list of dictionaries representing records
        """

        if not self.url:
            self.__build_url__('courses', filters=filters)

        courses = self.__read__()
        total_records = max_records if max_records else courses['total_count']

        next_url = courses['_links']['next']['href']

        for course in courses['courses']:
            course_data = self.__record_data__(course, subset)

            self.__add_record__(course_data)

            if max_records and len(self.records) >= max_records:
                return self.__get_records__()

        if not self.silent:
            print('Records: {}/{}'.format(len(self.records), total_records))

        if next_url:
            self.url = next_url

            return self.get(subset, max_records=max_records)

        self.url = None

        return self.__get_records__()


class Desmond(Api):
    __PARAM_TOKEN__ = 'token'

    def __init__(self,
                 auth_token: str,
                 country: str = 'es',
                 version: str = '1.0',
                 page_size: int = 25,
                 silent: bool = True):
        """Api class constructor
        :param auth_token: Authentication token
        :param country: Country site
        :param version: Api version
        :param page_size: Number of records per page
        :param silent: Whether or not messages will be printed on the screen
        """
        self.auth_token = auth_token

        super(Desmond, self).__init__(country, version, page_size, silent)

    def center_stats(self,
                     filters: Optional[Dict] = None,
                     max_records: Optional[int] = None) -> List:
        """ Retrieve centers' statistics
        :param filters: Applied filters
        :param max_records: Maximum number of records to retrieve
        :return: A collection of centers' statistics
        """
        if not self.url:
            self.__build_url__('stats', filters=filters, path='desmond/centers')
            self.__append_token_to_url__()

        stats = self.__read__()
        total_records = max_records if max_records else stats['total_count']

        next_url = stats['_links']['next']['href']

        for stat in stats['results']:
            course_data = self.__record_data__(stat, subset={'name': 'center'})

            self.__add_record__(course_data)

            if max_records and len(self.records) >= max_records:
                return self.__get_records__()

        if not self.silent:
            print('Records: {}/{}'.format(len(self.records), total_records))

        if next_url:
            self.url = next_url
            self.__append_token_to_url__()

            return self.center_stats(max_records=max_records)

        self.url = None

        return self.__get_records__()

    def get(self, subset: Optional[Union[List[str], Dict]] = None, filters: Optional[Dict] = None,
            max_records: Optional[int] = None, url: Optional[str] = None) -> List:
        pass

    def __record_data__(self, record: Dict, subset: Optional[Union[List[str], Dict]] = None) -> Dict:
        data = {
            'id': record['id'],
            subset['name']: record['name'],
            'market_leads': format_number(record['leads']['global']),
            'center_leads': np.nan,
            'market_courses': np.nan,
            'center_courses': np.nan,
            'market_enrolments': format_number(record['leads']['global']),
            'center_enrolments': np.nan
        }

        if 'center' in record['leads'].keys():
            data['center_leads'] = format_number(record['leads']['center'])

        if 'center' in record['enrolments'].keys():
            data['center_enrolments'] = format_number(record['leads']['center'])

        if 'courses' in record.keys():
            data['market_courses'] = format_number(record['courses']['global'])
            if 'center' in record['courses'].keys():
                data['center_courses'] = format_number(record['courses']['center'])

        return data

    def __append_token_to_url__(self):
        """ Append the authentication token parameter to url"""

        c = '&'

        if '?' not in self.url:
            c = '?'

        self.url = '{}{}{}={}'.format(self.url, c, self.__PARAM_TOKEN__, self.auth_token)


def format_number(number: Optional[str] = None):
    if not number:
        return np.nan

    return int(number.replace('.', ''))
