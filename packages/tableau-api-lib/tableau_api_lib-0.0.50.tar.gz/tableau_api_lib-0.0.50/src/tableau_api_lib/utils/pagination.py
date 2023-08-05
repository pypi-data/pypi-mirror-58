from tableau_api_lib.exceptions import ContentNotFound


def get_page_attributes(query):
    """
    Get the page attributes (pageNumber, pageSize, totalAvailable) from a query and return their values.

    :param query:   The results of the GET request query, containing paginated data.
    :type query:    JSON or dict
    :return:        page_number, page_size, total_available
    """
    try:
        pagination = query['pagination']
        page_number = int(pagination['pageNumber'])
        page_size = int(pagination['pageSize'])
        total_available = int(pagination['totalAvailable'])
        return page_number, page_size, total_available
    except KeyError:
        print("The query provided does not contain paged results.")


def validate_kwargs(kwargs):
    valid = True
    valid_kwargs = [
        'group_id',
        'user_id',
        'view_id',
        'workbook_id',
        'site_id'
    ]
    if len(kwargs.keys()) > 1:
        valid = False
    for kwarg in kwargs.keys():
        if kwarg not in valid_kwargs:
            valid = False
    if not valid:
        raise ValueError("""
        {} is not a valid argument to the extract_pages function. Valid arguments are as follows: \n{}
        """.format(list(kwargs.keys()).pop(), valid_kwargs))
    return list(kwargs.keys())[0], list(kwargs.values())[0]


def extract_pages(query_func,
                  starting_page=1,
                  page_size=100,
                  limit=None,
                  parameter_dict={},
                  **kwargs):
    """
    :param query_func:          A callable function that will issue a GET request to Tableau Server.
    :type query_func:           function
    :param starting_page:       The page number to start on. Defaults to the first page (page_number = 1).
    :type starting_page:        int
    :param page_size:           The number of objects per page. If querying users, this is the number of users per page.
    :type page_size:            int
    :param limit:               The maximum number of objects to return. Default is no limit.
    :type limit:                int
    :param parameter_dict:      A dict whose values are appended to the REST API URL endpoint as URL parameters.
    :type parameter_dict:       dict
    :return: extracted_pages    JSON or dict
    """
    if kwargs:
        arg_key, arg_value = validate_kwargs(kwargs)
    extracted_pages = []
    page_number = starting_page
    extracting = True

    while extracting:
        params = parameter_dict.copy()
        paginating_params = {
            'pageNumber': 'pageNumber={}'.format(page_number),
            'pageSize': 'pageSize={}'.format(page_size)
        }
        params.update(paginating_params)
        if kwargs:
            query = query_func(arg_value, parameter_dict=params).json()
        else:
            query = query_func(parameter_dict=params).json()
        page_number, page_size, total_available = get_page_attributes(query)

        if total_available == 0:
            raise ValueError('The Tableau Server content being queried has at least one empty entity. Please Verify.')
        else:
            try:
                outer_key = [key for key in query.keys() if key != 'pagination'].pop()
                inner_key = list(query[outer_key].keys()).pop()
                extracted_pages += query[outer_key][inner_key]
            except IndexError:
                raise ContentNotFound()

            if limit:
                if limit <= len(extracted_pages):
                    extracted_pages = extracted_pages[:limit]
                    extracting = False
            elif total_available <= (page_number * page_size):
                extracting = False
            else:
                page_number += 1

    return extracted_pages
