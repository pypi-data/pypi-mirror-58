"""The csv parsing interface."""

import ast

import pandas

from ..core.modelisotherm import ModelIsotherm
from ..core.pointisotherm import PointIsotherm
from ..modelling import get_isotherm_model


def _is_float(s):
    """Check if a value is a float."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def _is_bool(s):
    """Check a value is a CSV bool."""
    if s == 'True' or s == 'False':
        return True
    else:
        return False


def _to_bool(s):
    """Convert a value into a CSV bool."""
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        raise ValueError('String cannot be converted to bool')


def _is_list(s):
    """Check a value is a CSV list."""
    if s[0] == '[' and s[-1] == ']':
        return True
    else:
        return False


def _from_list(s):
    """Convert a value into a CSV list."""
    # note that the function will fail if the list has other spaces
    return ast.literal_eval(s.replace(' ', ","))


def _to_string(s):
    """Convert a value into a CSV-safe string."""
    if isinstance(s, list):
        return '[' + ' '.join([str(x) for x in s]) + "]"
    return str(s)


def isotherm_to_csv(isotherm, path, separator=','):
    """
    Convert isotherm into a CSV file.

    Parameters
    ----------
    isotherm : Isotherm
        Isotherm to be written to csv.
    path : str
        Path to the file to be written.
    separator : str, optional
        Separator used int the csv file. Defaults to '',''.

    """
    with open(path, mode='w', newline='\n') as file:

        isotherm_data = isotherm.to_dict()

        file.writelines([x + separator + _to_string(y) + '\n'
                         for (x, y) in isotherm_data.items()])

        if isinstance(isotherm, PointIsotherm):

            # get headings in an ordered way
            headings = [
                isotherm.pressure_key,
                isotherm.loading_key,
            ]
            if isotherm.other_keys:
                headings.extend(isotherm.other_keys)

            # also get the branch data in a regular format
            headings.append('branch')
            data = isotherm.data(raw=True)[headings]
            data['branch'] = data['branch'].replace(False, 'ads').replace(True, 'des')

            file.write('data:[pressure,loading,[otherdata],branch data]\n')
            data.to_csv(file, sep=separator, index=False, header=True)

        elif isinstance(isotherm, ModelIsotherm):

            file.write('model:[name and parameters]\n')
            file.write(('name' + separator + isotherm.model.name + '\n'))
            file.write(('rmse' + separator + _to_string(isotherm.model.rmse) + '\n'))
            file.write(('pressure range' + separator + _to_string(isotherm.model.pressure_range) + '\n'))
            file.write(('loading range' + separator + _to_string(isotherm.model.loading_range) + '\n'))
            file.writelines([param + separator + str(isotherm.model.params[param]) + '\n'
                             for param in isotherm.model.params])


def isotherm_from_csv(path, separator=',', **isotherm_parameters):
    """
    Load an isotherm from a CSV file.

    Parameters
    ----------
    path : str
        Path to the file to be read.
    separator : str, optional
        Separator used int the csv file. Defaults to `,`.
    isotherm_parameters :
        Any other options to be overridden in the isotherm creation.

    Returns
    -------
    Isotherm
        The isotherm contained in the csv file.

    """
    with open(path) as file:
        line = file.readline().rstrip()
        raw_dict = {}

        while not (line.startswith('data') or line.startswith('model') or line == ""):
            values = line.split(sep=separator)

            if _is_bool(values[1]):
                val = _to_bool(values[1])
            elif _is_float(values[1]):
                val = float(values[1])
            elif _is_list(values[1]):
                val = _from_list(values[1])
            else:
                val = values[1]
            raw_dict.update({values[0]: val})
            line = file.readline().rstrip()

        if line.startswith('data'):
            data = pandas.read_csv(file, sep=separator)

            # process isotherm branches if they exist
            raw_dict['branch'] = 'guess'
            if 'branch' in data.columns:
                raw_dict['branch'] = data['branch'].replace('ads', False).replace('des', True).values

            # generate other keys
            other_keys = [column for column in data.columns.values
                          if column not in [data.columns[0], data.columns[1], 'branch']]

            # Update dictionary with any user parameters
            raw_dict.update(isotherm_parameters)

            isotherm = PointIsotherm(
                isotherm_data=data,
                pressure_key=data.columns[0],
                loading_key=data.columns[1],
                other_keys=other_keys,
                **raw_dict)

        if line.startswith('model'):

            model = {}
            line = file.readline().rstrip()
            model['name'] = line.split(sep=separator)[1]
            line = file.readline().rstrip()
            model['rmse'] = line.split(sep=separator)[1]
            line = file.readline().rstrip()
            model['pressure_range'] = _from_list(line.split(sep=separator)[1])
            line = file.readline().rstrip()
            model['loading_range'] = _from_list(line.split(sep=separator)[1])
            line = file.readline().rstrip()
            model['parameters'] = {}
            while line != "":
                values = line.split(sep=separator)
                model['parameters'][values[0]] = float(values[1])
                line = file.readline().rstrip()

            new_mod = get_isotherm_model(model['name'])
            new_mod.rmse = model['rmse']
            new_mod.pressure_range = model['pressure_range']
            new_mod.loading_range = model['loading_range']
            for param in new_mod.params:
                try:
                    new_mod.params[param] = model['parameters'][param]
                except KeyError as err:
                    raise KeyError("The CSV is missing parameter {}".format(param)) from err

            # Update dictionary with any user parameters
            raw_dict.update(isotherm_parameters)

            isotherm = ModelIsotherm(model=new_mod, **raw_dict)

    return isotherm
