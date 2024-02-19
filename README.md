# Peasys Python Library

[![pypi]()]()
[![Build Status]()
[![Coverage Status]()]()

The Stripe Python library provides convenient access to the Stripe API from
applications written in the Python language. It includes a pre-defined set of
classes for API resources that initialize themselves dynamically from API
responses which makes it compatible with a wide range of versions of the Stripe
API.

## Documentation

See the [Python API docs](https://dips400.com/docs).

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install --upgrade peasys
```

### Requirements

- Python 3.6+ (PyPy supported)

## Usage

### License key
Peasys is a tool used along a license that should be found on the [dips400](https://dips400.com) website. This license key is required for the use of the service Peasys.

### Connexion to the server
Stripe authenticates API requests using your account’s secret key, which you can find in the Stripe Dashboard. By default, secret keys can be used to perform any API request without restriction.

```python
from peasys import pea_client

conn = pea_client.PeaClient("PARTITION_NAME", PORT, "USERNAME", "PASSWORD", "FUTUR_LICENSE_KEY", False)
```

### Query the DB2
For example, use the ExecuteCreate method of the PeaClient class in order to create a a new table in the database.

```python
create_response = conn.execute_create("CREATE TABLE schema_table/table_name (name CHAR(10), age INT)")
print(create_response.returnedSQLMessage)
print(create_response.returnedSQLState)
```

### Deconnexion

It is important to always disconnect from the server after you used the connexion.

```python
conn.disconnect()
```

### Handling exceptions

Unsuccessful requests raise exceptions. The class of the exception will reflect
the sort of error that occurred. Please see the [documentation](https://stripe.com/docs) for a description of
the error classes you should handle, and for information on how to inspect
these errors.

## Support

New features and bug fixes are released on the latest major version of the Peasys Python library. If you are on an older major version, 
we recommend that you upgrade to the latest in order to use the new features and bug fixes including those for security vulnerabilities. 
Older major versions of the package will continue to be available for use, but will not be receiving any updates.