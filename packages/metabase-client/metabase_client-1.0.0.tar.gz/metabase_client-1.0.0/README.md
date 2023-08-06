# Metabase Client
A production-ready metabase client to spare you from handling HTTP requests directly.

## Install

```
$ pip install metabase_client
```

## Start

You can provide username and password to authenticate...

```
from metabase_client import MetabaseClient

client = MetabaseClient("http://my-metabase-service.com", username="user", password="pass")
client.auth()
```

... or just provide an already-authenticated token.

```
from metabase_client import MetabaseClient

client = MetabaseClient("http://my-metabase-service.com", token="mytoken1q2w3e4r")
```

**Obs:** Since metabase limits the number of logins made through its API, using the second approach enables you to cache the token and avoid many logins.

## Contributions
Any contributions are welcome. Fork this project and follow the steps below:

1. Create a virtual env.
2. Implement the feature along with the automated tests.
3. Apply makefile commands (`make [test|flake|black]`)
4. Open a Pull Request.

## Help or Suggestions 
Please, open an issue at the [Github Issues page](https://github.com/victormartinez/metabase_client/issues).
