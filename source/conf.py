# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sheet-to-Doc Documentation'
copyright = '2022~2026, WTSolutions'
author = 'WTSolutions'
release = '2.15.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



#  启用自动编号（关键配置：开启toctree的层级编号）
toc_num_entries = False  # 核心：开启目录项数字编号

extensions = [
    'myst_parser',
    'sphinx_sitemap',
    # 'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]

# 启用MyST扩展
myst_enable_extensions = [
    # "admonitions",  # 启用提示框功能
    "colon_fence",
    "deflist",
    "html_image",
]

# 3. 可选：配置编号样式（部分主题支持）
html_theme_options = {
    'numbered_headings': False,  # 适配 sphinx_rtd_theme 等主题的序号显示
    'collapse_navigation': False,
    'sticky_navigation': True,
}

html_baseurl = 'https://sheet-to-doc.wtsolutions.cn/en/latest/'
sitemap_url_scheme = "{link}"
html_extra_path = ['robots.txt','ads.txt','llms.txt']
html_js_files = ['custom.js']
html_css_files = ['custom.css']
language ='en'
templates_path = ['_templates']
exclude_patterns = [
    'requirements.txt','.DS_Store'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']

html_theme = "shibuya"
html_static_path = ['_static']

# 自定义导航链接
# shibuya 主题的导航链接配置项
html_theme_options = {
    "nav_links": [
        {
            "title": "Product File",
            "url": "https://s.wtsolutions.cn/sheet-to-doc-product.html"
        },
        {
            "title": "Sheet-to-Doc Web Version",
            "url": "https://s.wtsolutions.cn/sheet-to-doc.html"
        },
    ]
}

html_context = {
    "languages": [
        ("English", "/en/latest/%s/", "en"),
        ("中文", "/zh-cn/latest/%s/", "zh-cn"),
    ]
}