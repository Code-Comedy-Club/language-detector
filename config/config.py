dataset = {
    "path": "./data",
    "path_raw": "raw",
    "path_processed": "processed",
    "path_cache": "cache",
    "path_train": "train",
    "path_test": "test",
    "webs": [
        # CA
        {
            "category": "ca",
            "name": "vidalibarraquer",
            "url": "https://www.vidalibarraquer.net/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//url/loc/text()",
            "options": {
                "container": "article",
                "container_attrs": {"class": "item"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },



    ],

    "headers": {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
    },
    "split_ratio": 0.8,
    "limit": 1_000
}

model = {
    "path": "./data",
    "path_model": "model",
    "nnet": {
        "path": "nnet",
        "name": "model.h5"
    },
    "svm": {
        "path": "svm",
        "name": "model.joblib"
    },
    "forest": {
        "path": "forest",
        "name": "model.joblib"
    },
    "decision": {
        "path": "decision",
        "name": "model.joblib"
    }
}
