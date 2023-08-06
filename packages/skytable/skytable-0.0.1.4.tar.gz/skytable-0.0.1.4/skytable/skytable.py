import sys
import pymongo
from collections import OrderedDict
import posixpath
import urllib.parse
import time
# import json
from bson import ObjectId
from six.moves.urllib.parse import unquote, quote
#
from .auth import SkytableAuth
from .params import SkytableParams


class Skytable:

    VERSION = "v0"
    API_BASE_URL = "mongodb://localhost"
    API_LIMIT = 1.0 / 5  # 5 per second
    API_URL = API_BASE_URL
    PAGE_SIZE = 100

    FRAGMENTS = urllib.parse.urlparse(API_BASE_URL)
    API_PATH = '{scheme}://%s{domain}'.format(
        scheme = FRAGMENTS.scheme,
        domain = FRAGMENTS.netloc
    )

    def __init__(self, base_key, table_name, api_key=None):
        auth = SkytableAuth(api_key=api_key)
        session = pymongo.MongoClient(self.API_PATH % (auth and auth+'@' or '',))
        self.session = session
        self.db_name = base_key
        self.table_name = table_name
        url_safe_table_name = quote(table_name, safe="")
        self.url_table = posixpath.join(self.API_URL, base_key, url_safe_table_name)
        self.table = self.session[self.db_name][self.table_name]

    def _process_params(self, params):

        new_params = OrderedDict()
        for param_name, param_value in sorted(params.items()):
            param_value = params[param_name]
            ParamClass = SkytableParams._get(param_name)
            new_params.update(ParamClass(param_value).to_param_dict())
        return new_params

    # ok
    def _process_response(self, response):

        if isinstance(response, dict):
            _id = response.pop('_id')
            fields = response
            result = {
                'id': str(_id),
                'createdTime': _id.generation_time.isoformat(),
                'fields': fields
            }
            return result

        return response

    # ok
    def record_url(self, record_id):
        return posixpath.join(self.url_table, record_id)

    # ok
    def url_id(self, url):
        object_id = url.rsplit('/', 1)[-1]
        return ObjectId(object_id)

    # ok
    def _request(self, method, url, params=None, json_data=None):

        # Later to move to (params).SkytableParams
        formula = {}
        projection = {}
        maxRecords = None

        def to_mongo_filter(formula):

            if isinstance(formula, dict):
                return formula

            elif isinstance(formula, str):
                # TBD: Use the below examples to create a converter for formulas specified in this pattern.
                if formula == "NOT({Active} = '')":
                    return {'$and': [{'Active': {'$ne': False}, 'Active': {'$ne': ''}}]}

                if formula == "AND(NOT({Active} = ''), {Priority} >= 0)":
                    return {'$and': [{'Active': {'$ne': False}, 'Active': {'$ne': ''}}, {'Priority': {'$gte': 0}}]}

                if formula == "AND({FoundByKeyphraseID} = 'MyPhraseName', {Status} = 'New', NOT(OR(FIND('UK', {GroupName}), FIND('Fashion', {GroupName}), FIND('Fashion', {GroupName}))))":
                    return {}

                if formula == "AND({Status} = 'Joined')":
                    return {'$and': [{'Status': 'Joined'}]}

                if formula == "AND({LinkedinUserURL} = 'http://specific_user_url', {Status} = 'Invitation sent')":
                    return {'$and': [{'LinkedinUserURL': 'http://specific_user_url'}, {'Status': 'Invitation sent'}]}

                if formula == "AND({Status} = 'New', NOT({GroupRole} = 'Manager'))":
                    return {'$and': [{'Status': 'New'}, {'GroupRole': {'$ne': 'Manager'}}]}

                if formula == "AND({Status} = 'Connected', NOT(OR({GroupRole} = 'Owner', {GroupRole} = 'Manager')))":
                    return {'$and': [{'Status': 'Connected'}],
                            '$or': [{'GroupRole': 'Owner'}, {'GroupRole': 'Manager'}]}
            else:
                return {}

        if params is not None:
            if 'fields[]' in params:
                projection = {field: 1.0 for field in params['fields[]']}
            else:
                projection = {}

            if 'filterByFormula' in params:
                formula = params['filterByFormula']
            else:
                formula = {}

            if 'maxRecords' in params:
                maxRecords = params['maxRecords']

        formula = to_mongo_filter(formula)

        if params is not None:
            sort = [
                (params[param.replace('direction', 'field')], {'desc': -1, 'asc': 1}.get(params[param]))
                for param in params if (param.startswith('sort') and 'direction' in param)
            ]
        else:
            sort = []

        if method == 'get':

            # FIND_MANY
            if url.endswith(self.url_table):

                offset = params.get('offset', None) or 0

                if maxRecords is not None:
                    if offset + self.PAGE_SIZE > maxRecords:
                        correction = maxRecords - offset
                    else:
                        correction = 0

                    if maxRecords < self.PAGE_SIZE:
                        correction = self.PAGE_SIZE - maxRecords
                else:
                    correction = 0

                if sort:
                    response = {'records': [
                        self._process_response(it)
                        for it in self.table.find(formula, projection or None).sort(sort).skip(offset).limit(self.PAGE_SIZE - correction)
                    ]} #, params=params, json=json_data)
                else:
                    response = {'records': [
                        self._process_response(it)
                        for it in self.table.find(formula, projection or None).skip(offset).limit(self.PAGE_SIZE - correction)
                    ]} #, params=params, json=json_data)


                if len(response['records']) >= self.PAGE_SIZE:
                    response['offset'] = offset + self.PAGE_SIZE

                if correction > 0:
                    response['offset'] = None

                return response

            # FIND_ONE
            else:
                response = self.table.find_one({'_id': self.url_id(url)}) #, params=params, json=json_data)
                return self._process_response(response)

        elif method == 'post':

            # INSERT_ONE
            response = self.table.insert_one(json_data['fields'])#, params=params)
            return response

            # INSERT_MANY

        elif method == 'patch':

            # UPDATE_ONE
            response = self.table.update_one(
                {'_id': self.url_id(url)},
                {'$set': json_data['fields']}
            )
            return response

            # UPDATE_MANY

    # ok
    def _get(self, url, **params):
        processed_params = self._process_params(params)
        return self._request("get", url, params=processed_params)

    def _post(self, url, json_data):
        return self._request("post", url, json_data=json_data)

    def _put(self, url, json_data):
        raise NotImplementedError

        return self._request("put", url, json_data=json_data)

    def _patch(self, url, json_data):
        return self._request("patch", url, json_data=json_data)

    def _delete(self, url):
        raise NotImplementedError

        return self._request("delete", url)

    # ok
    def get(self, record_id):
        record_url = self.record_url(record_id)
        return self._get(record_url)

    def get_iter(self, **options):
        offset = None
        while True:
            data = self._get(self.url_table, offset=offset, **options)
            records = data.get("records", [])
            time.sleep(self.API_LIMIT)
            yield records
            offset = data.get("offset")
            if not offset:
                break

    # ok
    def get_all(self, **options):
        all_records = []
        for records in self.get_iter(**options):
            all_records.extend(records)
        return all_records

    def match(self, field_name, field_value, **options):
        raise NotImplementedError

        from_name_and_value = SkytableParams.FormulaParam.from_name_and_value
        formula = from_name_and_value(field_name, field_value)
        options["formula"] = formula
        for record in self.get_all(**options):
            return record
        else:
            return {}

    def search(self, field_name, field_value, record=None, **options):
        records = []
        from_name_and_value = SkytableParams.FormulaParam.from_name_and_value
        formula = from_name_and_value(field_name, field_value)
        options["formula"] = formula
        records = self.get_all(**options)
        return records

    # ok
    def insert(self, fields, typecast=False):
        result = self._post(
            self.url_table, json_data={"fields": fields, "typecast": typecast}
        )
        return self.get(str(result.inserted_id))

    def _batch_request(self, func, iterable):
        raise NotImplementedError

        responses = []
        for item in iterable:
            responses.append(func(item))
            time.sleep(self.API_LIMIT)
        return responses

    def batch_insert(self, records, typecast=False):
        raise NotImplementedError

        return self._batch_request(self.insert, records)

    # ok
    def update(self, record_id, fields, typecast=False):
        record_url = self.record_url(record_id)
        result = self._patch(
            record_url, json_data={"fields": fields, "typecast": typecast}
        )
        return self.get(record_id)

    def update_by_field(
        self, field_name, field_value, fields, typecast=False, **options
    ):
        raise NotImplementedError

        record = self.match(field_name, field_value, **options)
        return {} if not record else self.update(record["id"], fields, typecast)

    def replace(self, record_id, fields, typecast=False):
        raise NotImplementedError

        record_url = self.record_url(record_id)
        return self._put(record_url, json_data={"fields": fields, "typecast": typecast})

    def replace_by_field(
        self, field_name, field_value, fields, typecast=False, **options
    ):
        raise NotImplementedError

        record = self.match(field_name, field_value, **options)
        return {} if not record else self.replace(record["id"], fields, typecast)

    def delete(self, record_id):
        raise NotImplementedError

        record_url = self.record_url(record_id)
        return self._delete(record_url)

    def delete_by_field(self, field_name, field_value, **options):
        raise NotImplementedError

        record = self.match(field_name, field_value, **options)
        record_url = self.record_url(record["id"])
        return self._delete(record_url)

    def batch_delete(self, record_ids):
        raise NotImplementedError

        return self._batch_request(self.delete, record_ids)

    def mirror(self, records, **options):
        raise NotImplementedError

        all_record_ids = [r["id"] for r in self.get_all(**options)]
        deleted_records = self.batch_delete(all_record_ids)
        new_records = self.batch_insert(records)
        return (new_records, deleted_records)

    def __repr__(self):
        return "<Skytable table:{}>".format(self.table_name)
