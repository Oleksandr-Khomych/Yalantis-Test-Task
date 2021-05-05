import json
import pytest


data = [({'name': 'Course1', 'start_date': '2018-01-01', 'end_date': '2020-01-01', 'lectures_count': -100},
         400,
         'lectures_count',
         'The parameter lectures_count can`t be less than 1. You give the value: -100'),

        ({'name': 'Course2', 'start_date': '2018-01-01', 'end_date': '2017-01-01', 'lectures_count': 10},
         400,
         'date',
         'The parameter start_date must be less than end_date'),

        ({'name': 'Course2', 'start_date': '2019-04-20', 'end_date': '2022-04-30', 'lectures_count': 'some text'},
         400,
         'lectures_count',
         f"The parameter lectures_count is not int. You give the value type: {type('some text')}"
         ),

        ({'name': 'Course3', 'start_date': 'incorrect_date', 'end_date': '2022-04-02', 'lectures_count': 10},
         400,
         'start_date',
         "time data 'incorrect_date' does not match format '%Y-%m-%d'"),

        ({'name': 'Course3', 'start_date': '2020-01-02', 'end_date': '01-01-2021', 'lectures_count': 10},
         400,
         'end_date',
         "time data '01-01-2021' does not match format '%Y-%m-%d'"),

        ({'start_date': '2021-05-05', 'end_date': '2022-05-15', 'lectures_count': 10},
         400,
         'name',
        'Missing required parameter in the JSON body or the post body or the query '
         'string'
         ),

        ({'name': 'Course_without_start_date', 'end_date': '2022-05-15', 'lectures_count': 10},
         400,
         'start_date',
         'Missing required parameter in the JSON body or the post body or the query '
         'string'
         ),

        ({'name': 'Course_without_end_date', 'start_date': '2022-05-15', 'lectures_count': 10},
         400,
         'end_date',
         'Missing required parameter in the JSON body or the post body or the query '
         'string'
         ),

        ({'name': 'Course_without_lectures_count', 'start_date': '2022-05-15', 'end_date': '2022-06-15'},
         400,
         'lectures_count',
         'Missing required parameter in the JSON body or the post body or the query '
         'string'
         ),

        ({},
         400,
         'name',
         'Missing required parameter in the JSON body or the post body or the query string')
        ]


create_course_corect_data = [
    ({'name': 'Course1', 'start_date': '2018-01-01', 'end_date': '2018-01-30', 'lectures_count': 30}),
    ({'name': 'Course2', 'start_date': '2019-04-20', 'end_date': '2022-04-30', 'lectures_count': 10}),
    ({'name': 'Course3', 'start_date': '2020-01-20', 'end_date': '2022-04-02', 'lectures_count': 50}),
    ({'name': 'Course4', 'start_date': '2021-04-20', 'end_date': '2022-04-27', 'lectures_count': 74}),
    ({'name': 'Course5', 'start_date': '2021-05-05', 'end_date': '2022-05-15', 'lectures_count': 10})
]


@pytest.mark.parametrize("data, expected_status_code, key_in_response, expected_response", data)
def test_create_course_incorrect_data(test_client, data, expected_status_code, key_in_response, expected_response):
    r = test_client.post('/create', data=data)
    response = json.loads(r.get_data(as_text=True))
    assert r.status_code == expected_status_code
    assert response['message'][key_in_response] == expected_response


@pytest.mark.parametrize("d", create_course_corect_data)
def test_create_course(test_client, d):
    r = test_client.post('/create', data=d)
    response = json.loads(r.get_data(as_text=True))
    assert r.status_code == 201
    assert 'id' in response['message']
    assert response['message']['name'] == d['name']
    assert response['message']['start_date'] == d['start_date']
    assert response['message']['end_date'] == d['end_date']
    assert response['message']['lectures_count'] == d['lectures_count']


@pytest.mark.parametrize("course_id", [-1, 0, 99999, 'text'])
def test_course_info_incorrect_data(test_client, course_id):
    response = test_client.get(f'/course/{course_id}')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 404
    assert data['message'] == f"Course {course_id} doesn't exist!"


def test_home_page(test_client):
    response = test_client.get('/')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['message'] == 'CatalogAPI home page'


def test_catalog(test_client):
    response = test_client.get('/catalog')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert type(data['message']['courses']) == list
