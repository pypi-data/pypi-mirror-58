# sphinx-aimms-theme

This Sphinx theme was designed to provide a great reader experience for documentation users on both desktop and mobile devices for AIMMS projects.

**This theme also includes:** 
- an **[AIMMS pygment lexer](docs/AIMMS Lexer.md)** to highlight your AIMMS [code blocks in sphinx](http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block) 
- an **[AIMMS Domain](docs/AIMMS Domain.md)** to document your own AIMMS code.

Please find the documentation of those 2 elements following the links above.

This theme is inherited from the great [Read the Docs](https://github.com/readthedocs/sphinx_rtd_theme) but can work with any Sphinx project. 

You can find a working demo of the theme on AIMMS documentation websites:
- [AIMMS Function reference](https://documentation.aimms.com/functionreference)
- [AIMMS How-to](https://how-to.aimms.com)
- [AIMMS Documentation](https://documentation.aimms.com)

Installation
===============

This theme is distributed on [PyPI](https://pypi.org/project/sphinx-aimms-theme/) and can be installed with pip:

`pip install sphinx-aimms-theme`

To use the theme in your Sphinx project, you will need to add the following to your conf.py file:

``` python
extensions = [
    ...
    "sphinx_aimms_theme",
]

html_theme = "sphinx_aimms_theme"
```


Configuration
================

Theme options
----------------

The following options can be defined in your project’s conf.py file, using the html_theme_options configuration option.

For example:

``` python
html_theme_options = {
    'doc_title': 'Title of my docs',
    'home_page_description': 'my meta description',
}
```

*(if not specified, the option is a string)*

* **doc_title** 

    Title you will see on the top left corner of your docs

* **home_page_title** 

    HTML Title that will appear in the html meta title of your home page 

* **home_page_description** 

    Description that will appear in the html meta description of your home page
    
* **display_community_help_link** 

    Boolean - Displays a link at the bottom of every article redirecting to the [AIMMS community](https://community.aimms.com/) search page filled with the title of the current page.
    
* **display_community_embeddable** 

    Boolean - Displays an embbedable from the AIMMS Community, showing topics filtered with the title of the current page 
    
    > Send an email to support@aimms.com if you would like to activate the community embeddable on your docs.

* **display_local_toc** 

    Boolean - Displays a dynamic local table of content for each file, except top index files.

* **generate_google_analytics**
    
    Boolean - generates a google analytics HTML code as follows on every page:
    
    ``` html
        
        <script async src="https://www.googletagmanager.com/gtag/js?id={{ google_analytics_id }}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
        
            function gtag() {
                dataLayer.push(arguments);
            }
            gtag('js', new Date());
        
            gtag('config', '{{ google_analytics_id }}');
        </script>
        
    ```
    Where ``google_analytics_id`` is the following option

* **google_analytics_id**

    Change the Google Analytics ID that is included on every page

* **display_algolia_search**
    
    Replace the current default search box with an Algolia extension. 
    You must have registered your docs website on https://community.algolia.com/docsearch/#join-docsearch-program, and thus obtain from Algolia the following 3 options:

* **algolia_appid**
* **algolia_appkey**
* **algolia_indexname**
    
Use, contribute, fix, improve the theme
===================================

Run the theme locally
----------------------

If you would like to modify the theme, or correct something, you may build the theme locally. 

To do so, please download the theme repo on your computer, and run in the repo location:

`python setup.py develop`

> First, you may want to uninstall the theme installed, by running `python -m pip uninstall sphinx-aimms-theme`

Contribution and support
------------------------------

If you would like to propose a change, or if something's not clear, just send an e-mail to support@aimms.com

Note
---------

**All readthedocs options are available as well !**

https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html

This theme is highly customizable on both the page level and on a global level. See https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html 


