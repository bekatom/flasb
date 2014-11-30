__author__ = 'Beka'
import os
import string
import errno
from appmaker.config import MODULES_FOLDER, TEMPLATE_DIR, APPMAKER_PATTERNS
from appmaker.helpers import make_file


def exec_modul_constructor(module_name):
    try:
        module_folder = MODULES_FOLDER + "/" + module_name
        if not os.path.exists(module_folder):
            os.makedirs(module_folder)
            os.makedirs(TEMPLATE_DIR + "/" + module_name)
            make_file(MODULES_FOLDER, '__init__.py')
            make_file(module_folder, '__init__.py')
            make_file(module_folder, 'views.py')
            make_file(module_folder, 'models.py')
            module_template_maker(module_name)
            module_view_creator(module_name)
    except OSError, e:
        if e.errno != errno.EEXIST:
            raise


def module_template_maker(module_name):
    try:

        filename = APPMAKER_PATTERNS + '/' + 'module_index.html'
        f = open(filename, "r")
        text_pattern = f.read()
        text_pattern = text_pattern.replace('module_name', module_name)
        template_file = "%s/%s/%s" % (TEMPLATE_DIR, module_name, "index.html")
        fo = open(template_file, "w+")
        fo.write(text_pattern)
        fo.close()

    except OSError, e:
        if e.errno != errno.EEXIST:
            raise

def module_view_creator(module_name):
    try:
        filename = APPMAKER_PATTERNS + '/' + 'view.py'
        f = open(filename, "r")
        text_pattern = f.read()
        text_pattern = text_pattern.replace('module_name', module_name)
        template_file = "%s/%s/%s" % (MODULES_FOLDER, module_name, "views.py")
        fo = open(template_file, "w+")
        fo.write(text_pattern)
        fo.close()
    except OSError,e:
        if e.errno != errno.EEXIST:
            raise
