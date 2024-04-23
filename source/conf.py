# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Forthink Product Documentation'
copyright = '2019 - 2024, Chengdu forthink tech. Co., Ltd'
author = 'luochao'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_rtd_theme", "recommonmark", "sphinxcontrib.mermaid", "sphinx.ext.mathjax", "sphinx_markdown_tables"]

templates_path = ['_templates']
exclude_patterns = []

mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS-MML_HTMLorMML"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_static_path = ['_static']

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# support Markdown
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

# 源文件所在的目录，通常是包含.rst文件的目录  
# 确保这个路径指向的文件夹位于与你的输出目录相同的驱动器上  
# source_dir = 'E:/预研/车钥匙/产品设计/软件设计/user docs/ForthinkDocs/source/Datasheet.rst' 

# 构建目录，即输出HTML等文件的目录  
# 确保这个路径也位于与你的源文件相同的驱动器上  
# build_dir = 'E:/预研/车钥匙/产品设计/软件设计/user docs/ForthinkDocs/build/directory'  

# Autostructify
from recommonmark.transform import AutoStructify
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'enable_auto_toc_tree': True,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)

