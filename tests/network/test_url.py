#  Copyright 2019 SURF.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from more_ds.network.url import URL


def test_url() -> None:  # noqa: D103
    base_url = URL("http://example.org/")

    assert "http://example.org/" == base_url
    assert "URL('http://example.org/')" == repr(base_url)

    assert base_url / "api" == base_url / "/api"

    api_url = base_url / "api"
    assert "http://example.org/api" == api_url

    url = api_url / "ip" / "address" // {"version": 4}
    assert "http://example.org/api/ip/address?version=4" == url

    # paths don't need to be strings
    url = api_url / 1 / 2 / 3
    assert "http://example.org/api/1/2/3" == url

    # query string properly url encoded?
    url = api_url // {"query": ' "%-.<>\\^_`{|}~'}
    assert "http://example.org/api?query=+%22%25-.%3C%3E%5C%5E_%60%7B%7C%7D~" == url
