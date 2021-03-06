import requests
import pytest


class TestRemoveBuilds(object):

    def test_builds_url(self, monkeypatch, mock_post, advisory):
        monkeypatch.setattr(requests, 'post', mock_post)
        advisory.removeBuilds(['ceph-10.2.3-17.el7cp'])
        assert mock_post.response.url == 'https://errata.devel.redhat.com/api/v1/erratum/26175/remove_build'  # NOQA: E501

    def test_builds_flag_set(self, monkeypatch, mock_post, advisory):
        monkeypatch.setattr(requests, 'post', mock_post)
        advisory.removeBuilds(['ceph-10.2.3-17.el7cp'])
        assert advisory._buildschanged is True

    def test_builds_data(self, monkeypatch, mock_post, advisory):
        monkeypatch.setattr(requests, 'post', mock_post)
        advisory.removeBuilds(['ceph-10.2.3-17.el7cp'])
        expected = {
            "nvr": "ceph-10.2.3-17.el7cp",
        }
        assert mock_post.kwargs['data'] == expected

    def test_builds_name(self, monkeypatch, mock_post, advisory):
        monkeypatch.setattr(requests, 'post', mock_post)
        advisory.removeBuilds('ceph-10.2.3-17.el7cp')
        expected = {
            "nvr": "ceph-10.2.3-17.el7cp",
        }
        assert mock_post.kwargs['data'] == expected

    def test_builds_none(self, monkeypatch, mock_post, advisory):
        monkeypatch.setattr(requests, 'post', mock_post)
        with pytest.raises(IndexError):
            advisory.removeBuilds(None)
        assert advisory._buildschanged is False

    def test_builds_empty_string(self, monkeypatch, mock_post, advisory):
        monkeypatch.setattr(requests, 'post', mock_post)
        with pytest.raises(IndexError):
            advisory.removeBuilds('')
        assert advisory._buildschanged is False

    def test_builds_whitespace_string(self, monkeypatch, mock_post, advisory):
        monkeypatch.setattr(requests, 'post', mock_post)
        with pytest.raises(IndexError):
            advisory.removeBuilds(' ')
        assert advisory._buildschanged is False

    def test_builds_empty_set(self, monkeypatch, mock_post, advisory):
        monkeypatch.setattr(requests, 'post', mock_post)
        with pytest.raises(IndexError):
            advisory.removeBuilds(set())
        assert advisory._buildschanged is False

    def test_builds_empty_list(self, monkeypatch, mock_post, advisory):
        monkeypatch.setattr(requests, 'post', mock_post)
        with pytest.raises(IndexError):
            advisory.removeBuilds([])
        assert advisory._buildschanged is False

    def test_builds_empty_tuple(self, monkeypatch, mock_post, advisory):
        monkeypatch.setattr(requests, 'post', mock_post)
        with pytest.raises(IndexError):
            advisory.removeBuilds(())
        assert advisory._buildschanged is False
