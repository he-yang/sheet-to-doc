# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sheet to Doc'
copyright = '2022~2026, WTSolutions'
author = 'WTSolutions'
release = '2.5.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



#  启用自动编号（关键配置：开启toctree的层级编号）
toc_num_entries = True  # 核心：开启目录项数字编号

extensions = [
    'myst_parser',
    'sphinx_sitemap',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]

# 3. 可选：配置编号样式（部分主题支持）
html_theme_options = {
    'numbered_headings': True,  # 适配 sphinx_rtd_theme 等主题的序号显示
    'collapse_navigation': False,
    'sticky_navigation': True,
}

html_baseurl = 'https://sheet-to-doc.wtsolutions.cn/en/latest/'
sitemap_url_scheme = "{link}"
html_extra_path = ['robots.txt','ads.txt']
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
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']