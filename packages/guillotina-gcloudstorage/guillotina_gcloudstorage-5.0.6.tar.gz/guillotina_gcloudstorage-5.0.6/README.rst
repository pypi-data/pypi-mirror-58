GUILLOTINA_GCLOUDSTORAGE
========================

GCloud blob storage for guillotina.


Example config.json entry::

    ...
    "cloud_storage": "guillotina_gcloudstorage.interfaces.IGCloudFileField",
    "cloud_datamanager": "redis",
    "load_utilities": {
        "gcloud": {
            "provides": "guillotina_gcloudstorage.interfaces.IGCloudBlobStore",
            "factory": "guillotina_gcloudstorage.storage.GCloudBlobStore",
            "settings": {
                "json_credentials": "/path/to/credentials.json",
                "bucket": "name-of-bucket",
                "bucket_name_format": "{container}-foobar{delimiter}{base}",
                "bucket_labels": {
                    "foo": "bar"
                }
            }
        }
    }
    ...
