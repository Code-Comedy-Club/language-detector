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
            "name": "gencat",
            "url": "https://www.idescat.cat/novetats/?m=rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "ApartCont"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "gencat",
            "url": "https://govern.cat/salapremsa/api/v1/rss/search?objectType=1",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "body-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "elpuntavui",
            "url": "http://www.elpuntavui.cat/barcelona/nacional.feed?type=rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "elpuntavui",
            "url": "http://www.elpuntavui.cat/territori.feed?type=rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "elpuntavui",
            "url": "http://www.elpuntavui.cat/societat.feed?type=rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "elpuntavui",
            "url": "http://www.elpuntavui.cat/politica.feed?type=rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
{
            "category": "ca",
            "name": "elpuntavui",
            "url": "http://www.elpuntavui.cat/economia.feed?type=rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "elpuntavui",
            "url": "http://www.elpuntavui.cat/comunicacio.feed?type=rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "elpuntavui",
            "url": "http://www.elpuntavui.cat/esports.feed?type=rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "catalunya_diari",
            "url": "https://catalunyadiari.com/rss/cat/actualitat",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "content_text"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
         {
            "category": "ca",
            "name": "e_noticies",
            "url": "https://e-noticies.cat/rss/cat/actualitat",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "content_text"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "el_periodico",
            "url": "https://www.elperiodico.cat/ca/rss/rss_portada.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "ep-detail-body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "xcatalunya",
            "url": "https://xcatalunya.cat/rss/last-posts",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "content_text"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "macba",
            "url": "https://www.macba.cat/ca/feeds/activities",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "container"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "macba",
            "url": "https://www.macba.cat/ca/feeds/expos",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "container"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "macba",
            "url": "https://www.macba.cat/ca/feeds/free_admission",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "container"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "macba",
            "url": "https://www.macba.cat/ca/feeds/edu",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "container"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        # {
        #     "category": "ca",
        #     "name": "macba",
        #     "url": "https://www.macba.cat/ca/feeds/publi",
        #     "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
        #     "xpath": "//item/link/text()",
        #     "options": {
        #         "container": "article",
        #         "container_attrs": {"class": "u-spacer-padding-top"},
        #         "elements_to_extract": "p",
        #         "elements_ignore_last": False,
        #     },
        #     "limit": 1000
        # },
        {
            "category": "ca",
            "name": "ajuntament_barcelona",
            "url": "https://ajuntament.barcelona.cat/comerc/rss-ca",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "field-body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "icgc",
            "url": "http://www.icgc.cat/ca/rss/feed/actualitat",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "ezxmltext-field"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
        {
            "category": "ca",
            "name": "catalunyameteo",
            "url": "https://catalunyameteo.com/rss/cat/astronomia",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "content_text"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },
       {
            "category": "ca",
            "name": "vidalibarraquer",
            "url": "https://www.vidalibarraquer.net/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "article",
                "container_attrs": {"class": "item"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000
        },


        # ES
          {
            "category": "es",
            "name": "investing",
            "url": "https://es.investing.com/rss/news_301.rss",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "WYSIWYG" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "es",
            "name": "investing",
            "url": "https://es.investing.com/rss/news_1.rss",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "WYSIWYG" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "es",
            "name": "el_dia",
            "url": "https://www.eldia.es/rss/section/12701",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "article-body" },
                "elements_to_extract": "p",
                "elements_ignore_last": True
            }
        },
        {
            "category": "es",
            "name": "el_periodico_de_aragon",
            "url": "https://www.elperiodicodearagon.com/rss/section/23589",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "ft-layout-grid-flex__colXs-12 ft-layout-grid-flex__colSm-11" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "es",
            "name": "el_periodico",
            "url": "https://www.elperiodico.com/es/rss/politica/rss.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "ft-layout-grid-flex__colXs-12 ft-layout-grid-flex__colSm-11" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "es",
            "name": "la_vanguardia",
            "url": "https://www.lavanguardia.com/rss/politica.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "article-modules" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "es",
            "name": "el_periodico",
            "url": "https://www.elperiodico.com/es/rss/tecnologia/rss.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "ft-layout-grid-flex__colXs-12 ft-layout-grid-flex__colSm-11"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "es",
            "name": "el_pais",
            "url": "https://motor.elpais.com/rss",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "content__main__content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "es",
            "name": "diario_de_sevilla",
            "url": "https://www.diariodesevilla.es/rss/ocio/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "div",
                "container_attrs": {"class":"mce-body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 1000,
        },
        {
            "category": "es",
            "name": "la_vanguardia",
            "url": "https://www.lavanguardia.com/rss/politica.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "article-modules" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "es",
            "name": "el_diario_cantabria",
            "url": "https://eldiariocantabria.publico.es/rss/politica/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "content-body" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
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
