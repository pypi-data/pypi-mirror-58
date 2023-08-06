# Written by K1DV5
'''
Module document

provides the document class

In the latex file,
    use hashtags(#tagname) to reserve places for contents that
    will come from the python script.
In a separate python script,
    import this class.
    use methods tag('tagname') for something like tags(placeholders)
    write your calculations under those tags using ins(contents) to choose
        what goes to the document tag place.
    Finally use the write() method to write the final file.

when the python file is run, it writes a tex file with the tags
replaced by contents from the python file.
'''

import ast
# for tag replacements
import re
# for path manips
from os import path
# for word file handling
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape
from zipfile import ZipFile, ZIP_DEFLATED
# for temp directory
import tempfile
# for status tracking
import logging
# for included word template access
from pkg_resources import resource_filename
from shutil import move, rmtree
# for working with the document's variables and filename
try:
    from __main__ import __dict__ as DICT
except ImportError:
    DICT = {}
from .calculation import cal, _process_options
from .parsing import UNIT_PF, eqn, to_math, build_eqn, select_syntax, _parens_balanced, DEFAULT_MAT_SIZE

DEFAULT_FILE = 'Untitled.tex'
# the tag pattern
PATTERN = re.compile(r'(?s)([^\w\\]|^)#(\w+?)(\W|$)')
# for excel file handling
NS = {
    'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
    'x14ac': 'http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac',
}
# surrounding of the content sent for reversing (something that doesn't
# change the actual content of the document, and works inside lines)
SURROUNDING = ['{} {{ {}', '{} }} {}']
EXCEL_SEP = '|'

LOG_FORMAT = '%(levelname)s: %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger(__name__)


class latexFile:
    '''handles the latex files'''

    # name for this type (for to_math)
    name = 'latex'

    # warning for tag place protection in document:
    warning = ('BELOW IS AN AUTO GENERATED LIST OF TAGS. '
               'DO NOT DELETE IT IF REVERSING IS DESIRED!!!\n%')

    def __init__(self, infile, to_clear):

        self.to_clear = to_clear
        if infile:
            self.infile = self.outfile = infile
            with open(self.infile, encoding='utf-8') as file:
                self.file_contents = file.read()
            # the collection of tags at the bottom of the file for reversing
            self.tagline = re.search(fr'\n% *{re.escape(self.warning)}'
                                     r'*[\[[a-zA-Z0-9_ ]+\]\]',
                                     self.file_contents)
            # remove previous calculation parts
            if self.tagline:
                start = self.tagline.group(0).find('[[') + 2
                end = self.tagline.group(0).rfind(']]')
                self.tags = self.tagline.group(0)[start:end].split()
                self._revert_tags()
            self.tags = [tag.group(2)
                         for tag in PATTERN.finditer(self.file_contents)]
        else:
            self.file_contents = self.infile = self.tagline = self.tags = None
            self.outfile = DEFAULT_FILE
        self.calc_tags = []

    def _revert_tags(self):
        # remove the tagline
        file_str = (self.file_contents[:self.tagline.start()].rstrip() +
                    self.file_contents[self.tagline.end():])
        # replace the sent regions with their respective tags
        for tag in self.tags:
            file_str = re.sub(r'(?s)'
                              + re.escape(SURROUNDING[0])
                              + '.*?'
                              + re.escape(SURROUNDING[1]),
                              '#' + tag, file_str, 1)
        # for inplace editing
        self.file_contents = file_str
        return file_str

    def _subs_in_place(self, values: dict):
        file_str = self.file_contents + f'\n\n% {self.warning} [['
        file_str = PATTERN.sub(lambda x: self._repl(x, True, values),
                               file_str)
        for tag in self.calc_tags:
            file_str += tag + ' '
        file_str = file_str.rstrip('\n') + ']]'
        return file_str

    def _subs_separate(self, values: dict):
        return PATTERN.sub(lambda x: self._repl(x, False, values),
                           self.file_contents)

    def _repl(self, match_object, surround: bool, values: dict):
        start, tag, end = [m if m else '' for m in match_object.groups()]
        if tag in values:
            result = '\n'.join([val[1] for val in values[tag]])
            if surround:
                return (start
                        + SURROUNDING[0]
                        + (start if start == '\n' else '')
                        + result
                        + (end if end == '\n' else '')
                        + SURROUNDING[1]
                        + end)

            return start + result + end
        logger.error(f"There is nothing to send to #{tag}.")
        return start + '#' + tag + end

    def write(self, outfile=None, values={}):
        if outfile:
            self.outfile = outfile

        if not self.to_clear:
            if self.infile:
                for tag in values:
                    if tag in self.tags:
                        self.calc_tags.append(tag)
                    else:
                        logger.error(f'#{tag} not found in the document.')
                if path.abspath(self.outfile) == path.abspath(self.infile):
                    self.file_contents = self._subs_in_place(values)
                else:
                    self.file_contents = self._subs_separate(values)
            else:
                self.file_contents = '\n'.join([
                    '\n'.join([v[1] for v in val]) for val in values.values()
                ])

        logger.info('[writing file] %s', self.outfile)
        with open(self.outfile, 'w', encoding='utf-8') as file:
            file.write(self.file_contents)


class wordFile:

    # name for this type (for to_math)
    name = 'word'
    # the xml declaration
    declaration = '<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n'
    # always required namespaces
    namespaces = {
        "wpc": "http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas",
        "cx": "http://schemas.microsoft.com/office/drawing/2014/chartex",
        "cx1": "http://schemas.microsoft.com/office/drawing/2015/9/8/chartex",
        "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006",
        "o": "urn:schemas-microsoft-com:office:office",
        "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
        "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
        "v": "urn:schemas-microsoft-com:vml",
        "wp14": "http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing",
        "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
        "w10": "urn:schemas-microsoft-com:office:word",
        "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
        "w14": "http://schemas.microsoft.com/office/word/2010/wordml",
        "w15": "http://schemas.microsoft.com/office/word/2012/wordml",
        "w16se": "http://schemas.microsoft.com/office/word/2015/wordml/symex",
        "wpg": "http://schemas.microsoft.com/office/word/2010/wordprocessingGroup",
        "wpi": "http://schemas.microsoft.com/office/word/2010/wordprocessingInk",
        "wne": "http://schemas.microsoft.com/office/word/2006/wordml",
        "wps": "http://schemas.microsoft.com/office/word/2010/wordprocessingShape",
    }

    # the internal form of the parsed tags for internal use to avoid normal # usage
    tag_alt_form = '#{%s}'

    def __init__(self, infile, to_clear=False):
        # temp folder for converted files
        # self.temp_dir = path.join(environ['TMP'], '.docalTemp')
        self.temp_dir = tempfile.mkdtemp()
        # file taken as input file when not explicitly set:
        if infile:
            self.infile = infile
            base, ext = path.splitext(self.infile)
            self.outfile = base + '-out' + ext
            with ZipFile(infile, 'r') as zin:
                file_contents = zin.read('word/document.xml')
                self.tmp_file = ZipFile(path.join(
                    self.temp_dir, path.splitext(path.basename(self.infile))[0]),
                    'w', compression=ZIP_DEFLATED)
                self.tmp_file.comment = zin.comment
                for file in zin.namelist():
                    if file != 'word/document.xml':
                        self.tmp_file.writestr(file, zin.read(file))

            # the xml tree representation of the document contents
            self.doc_tree = ET.fromstring(file_contents)
            for prefix, uri in self.namespaces.items():
                ET.register_namespace(prefix, uri)

            # the tags in the document (stores tags, their addresses, and whether inline)
            self.tags_info = self.extract_tags_info(self.doc_tree)
            self.tags = [info['tag'] for info in self.tags_info]
        else:
            self.tmp_file = path.join(
                self.temp_dir, path.splitext(
                    path.basename(DEFAULT_FILE))[0])
            self.infile = self.doc_tree = self.tags_info = self.tags = None
            self.outfile = DEFAULT_FILE.replace('.tex', '.docx')

    def normalized_contents(self, paragraph):
        pref_w = f'{{{self.namespaces["w"]}}}'
        ignored = [pref_w + tag for tag in ['bookmarkStart', 'bookmarkEnd', 'proofErr']]
        conts = []
        for child in paragraph:
            if child.tag == pref_w + 'r':
                if conts:
                    if type(conts[-1]) == list:
                        conts[-1].append(child)
                    else:
                        conts.append(['', child])
                else:
                    conts.append(['', child])
                for t in child:
                    if t.tag == pref_w + 't':
                        conts[-1][0] += t.text
            elif conts and type(conts[-1]) != list or child.tag not in ignored:
                conts.append(child)
        return conts

    def extract_tags_info(self, tree):

        pref_w = f'{{{self.namespaces["w"]}}}'
        tags_info = []
        for index, child in enumerate(tree[0]):
            if child.tag == pref_w + 'p':
                # get its contents and clear it
                conts = self.normalized_contents(child)
                child.clear()
                for cont in conts:
                    if type(cont) == list:
                        if '#' in cont[0]:
                            # replace with a new element
                            w_r = ET.SubElement(child, pref_w + 'r')
                            w_t = ET.SubElement(w_r, pref_w + 't',
                                                {'xml:space': 'preserve'})
                            # store full info about the tags inside
                            for tag in PATTERN.finditer(cont[0]):
                                if cont[0].strip() == '#' + tag.group(2):
                                    position = 'para'
                                else:
                                    position = 'inline'
                                tags_info.append({
                                    'tag': tag.group(2),
                                    'tag-alt': self.tag_alt_form % tag.group(2),
                                    'address': [child, w_r, w_t],
                                    'position': position,
                                    'index': index})
                            # remove \'s from the escaped #'s and change the tags form
                            w_t.text = (re.sub(r'\\#', '#', PATTERN.sub(
                                lambda tag:
                                    tag.group(1) +
                                    self.tag_alt_form % tag.group(2) +
                                    tag.group(3),
                                cont[0])))
                        else:  # preserve properties
                            for r in cont[1:]:
                                child.append(r)
                    else:
                        child.append(cont)

        return tags_info

    def _subs_tags(self, values={}):
        ans_info = {tag: self.para_elts(val) for tag, val in values.items()}

        added = 0  # the added index to make up for the added elements
        for tag, ans_parts in ans_info.items():
            matching_infos = [
                info for info in self.tags_info if info['tag'] == tag]
            if matching_infos:
                info = matching_infos[0]
                # remove this entry to revert the left ones from their alt form
                self.tags_info.remove(info)
                if info['position'] == 'para':
                    ans_parts.reverse()  # because they are inserted at the same index
                    for ans in ans_parts:
                        self.doc_tree[0].insert(info['index'] + added, ans)
                    self.doc_tree[0].remove(info['address'][0])
                    added += len(ans_parts) - 1  # minus the tag para (removed)
                else:
                    loc_para, loc_run, loc_text = info['address']
                    split_text = loc_text.text.split(info['tag-alt'], 1)
                    loc_text.text = split_text[1]
                    index_run = list(loc_para).index(loc_run)
                    pref_w = f'{{{self.namespaces["w"]}}}'
                    # if there is only one para, insert its contents into the para
                    if len(ans_parts) == 1:
                        ans_runs = list(ans_parts[0])
                        ans_runs.reverse()  # same reason as above
                        for run in ans_runs:
                            loc_para.insert(index_run, run)
                        beg_run = ET.Element(pref_w + 'r')
                        beg_text = ET.SubElement(beg_run, pref_w + 't',
                                                 {'xml:space': 'preserve'})
                        beg_text.text = split_text[0]
                        loc_para.insert(index_run, beg_run)
                    else:  # split the para and make new paras between the splits
                        beg_para = ET.Element(pref_w + 'p')
                        beg_run = ET.SubElement(beg_para, pref_w + 'r')
                        beg_text = ET.SubElement(beg_run, pref_w + 't',
                                                 {'xml:space': 'preserve'})
                        beg_text.text = split_text[0]
                        ans_parts.reverse()  # same reason as above
                        for ans in ans_parts:
                            self.doc_tree[0].insert(info['index'] + added, ans)
                        beg_index = info['index'] + added
                        self.doc_tree[0].insert(beg_index, beg_para)
                        added += len(ans_parts) + 1
            else:
                logger.warning(f'#{tag} not found in the document.')
        # revert the rest of the tags from their alt form
        for info in self.tags_info:
            logger.warning(f'There is nothing to send to #{info["tag"]}.')
            loc_text = info['address'][2]
            loc_text.text = loc_text.text.replace(
                info['tag-alt'], '#' + info['tag'])

    def collect_txt(self, content):
        paras = []
        para = [['text', '']]
        for cont in content:
            # so that it has a space before the inline eqn
            space = '' if para[-1][1].endswith(' ') or not para[-1][1] else ' '
            if para[-1][0] == 'text':
                if cont[0] == 'text':
                    if cont[1].strip():
                        para[-1][1] += space + escape(cont[1])
                    elif para[-1][1].strip():
                        paras.append(para)
                        para = [['text', '']]
                else:
                    if cont[0] == 'inline':
                        if para[-1][1].strip():
                            para[-1][1] += space
                        para.append(cont)
                    else:
                        if para[0][1].strip() or len(para) > 1:
                            paras.append(para)
                            para = [['text', '']]
                        paras.append([cont])
            else:
                if cont[0] == 'inline':
                    para.append(['text', space])
                    para.append(cont)
                elif cont[0] == 'text':
                    if cont[1].strip():
                        para.append(['text', space + escape(cont[1])])
                    elif len(para) > 1 or para[0][1].strip():
                        paras.append(para)
                        para = [['text', '']]
                else:
                    if para[0][1].strip() or len(para) > 1:
                        paras.append(para)
                        para = [['text', '']]
                    paras.append([cont])
        if para[0][1].strip() or len(para) > 1:
            paras.append(para)
        return paras

    def para_elts(self, content: list):
        w = self.namespaces['w']
        m = self.namespaces['m']
        para_start = f'<w:p xmlns:w="{w}" xmlns:m="{m}">'
        para_form = para_start + '{}</w:p>'
        run_form = '<w:r><w:t xml:space="preserve">{}</w:t></w:r>'
        paras = []
        for para in self.collect_txt(content):
            para_xml_ls = []
            for part in para:
                if part[0] == 'text':
                    if part[1].strip():
                        para_xml_ls.append(run_form.format(part[1]))
                else:
                    para_xml_ls.append(part[1])
            para_xml = para_form.format(''.join(para_xml_ls))
            paras.append(ET.fromstring(para_xml))

        return paras

    def write(self, outfile=None, values={}):

        if outfile:
            self.outfile = outfile

        if self.infile:
            self._subs_tags(values)
        else:
            tmp_fname = path.splitext(self.tmp_file)[0] + '.docx'
            with ZipFile(resource_filename(__name__, 'template.docx'), 'r') as zin:
                file_contents = zin.read('word/document.xml')
                self.tmp_file = ZipFile(tmp_fname, 'w', compression=ZIP_DEFLATED)
                for file in zin.namelist():
                    if file != 'word/document.xml':
                        self.tmp_file.writestr(file, zin.read(file))

            self.doc_tree = ET.fromstring(file_contents)
            for child in self.doc_tree[0]:
                self.doc_tree[0].remove(child)
            for val in values.values():
                for para in self.para_elts(val):
                    self.doc_tree[0].append(para)
            for prefix, uri in self.namespaces.items():
                ET.register_namespace(prefix, uri)
        # take care of namespaces and declaration
        doc_xml = ET.tostring(self.doc_tree, encoding='unicode')
        searched = re.match(r'\<w:document.*?\>', doc_xml).group(0)
        used_nses = re.findall(r'(?<=xmlns\:)\w+', searched)
        for prefix, uri in self.namespaces.items():
            if prefix not in used_nses:
                self.doc_tree.set('xmlns:' + prefix, uri)

        doc_xml = self.declaration + \
            ET.tostring(self.doc_tree, encoding='unicode')
        self.tmp_file.writestr('word/document.xml', doc_xml)
        tmp_fname = self.tmp_file.filename
        self.tmp_file.close()

        logger.info('[writing file] %s', self.outfile)
        move(tmp_fname, self.outfile)

        rmtree(self.temp_dir)


class calculations:
    '''
    accept an excel file, extract the calculations in it and incorporate
    it in the document.'''

    xl_cell_pat = re.compile(r'[A-Z]+[0-9]+')
    xl_func_pat = re.compile(r'[A-Z]+(?=\()')
    xl_params = ['file', 'sheet', 'range']
    dcl_pre_code = ['from math import *']

    def __init__(self, tags, doc_type, working_dict):
        self.tags = tags
        self.current_tag = self.tags[0] if self.tags else None
        if self.current_tag is None:
            logger.warning('There are no tags in the document')
        self.doc_type = doc_type
        # for temp saving states
        self.temp_var = {}
        self.working_dict = working_dict
        # default calculation options
        self.default_options = {
                    'steps': [],
                    'mat_size': DEFAULT_MAT_SIZE,
                    'unit': '',
                    'mode': 'default',
                    'vert': True,
                    'note': None,
                    'hidden': False
                }
        self.working_dict['__DOCAL_OPTIONS__'] = self.default_options

    def process(self, what, typ='python'):
        if typ == 'python':
            return self.process_content(what)
        elif typ == 'dcl':
            processed = []
            doc_tree = ET.fromstring(what)
            for child in doc_tree:
                if child.tag in ('ascii', 'python'):
                    if child.tag == 'ascii':
                        child.text = self.repl_asc(child.text)
                    for part in self.process_content(child.text):
                        processed.append(part)
                elif child.tag == 'excel':
                    for part in self.repl_xl(child.text):
                        processed.append(part)
            return processed
        elif typ == 'ascii':
            return self.process_content(self.repl_asc(what))
        elif typ == 'excel':
            # assuming what is a dict
            return self.xl_convert(**what)

    def repl_asc(self, lines: str):

        lines = lines.split('\n')
        # by value! not to repeat the last ones
        py_lines = self.dcl_pre_code[:]
        comment_pat = re.compile(r'^(?=[^#:].*?(\w+\s+?\w+)|(\\\w+).*?$)')
        for line in lines:
            # import statements and the like preceded with :
            line = comment_pat.sub('# ', line)
            py_lines.append(re.sub(r'^\:', '', line))
        py_legal = '\n'.join(py_lines)
        # change power symbol, not in comments
        py_legal = re.sub(r'(?sm)^([^\#].*?)\^', r'\1**', py_legal)
        # number coefficients like 2x
        py_legal = re.sub(r'(?<=[0-9])( ?[a-df-zA-Z_]|\()', '*\\1', py_legal)

        return py_legal

    def repl_xl(self, lines: str):
        lines = lines.strip().split('\n')
        params = {
                'file': '',
                'sheet': 1,
                'range': None,
                }
        for param in [line.split(EXCEL_SEP)[:2] for line in lines]:
            try:
                key, val = param
            except ValueError:
                raise SyntaxError('Invalid syntax, must be in the form [parameter]' + EXCEL_SEP + ' [value]')
            else:
                if key.strip() in self.xl_params:
                    params[key.strip()] = val.strip()
        return self.xl_convert(file=params['file'],
                               sheet=params['sheet'],
                               range=params['range'])

    def xl_convert(self, file='', sheet=1, range=None):

        with ZipFile(file, 'r') as zin:
            sheet_xml = zin.read(f'xl/worksheets/sheet{int(sheet)}.xml').decode('utf-8')
            str_xml = zin.read('xl/sharedStrings.xml').decode('utf-8')

        sheet_tree = ET.fromstring(sheet_xml)
        str_tree = ET.fromstring(str_xml)
        rows = sheet_tree.find('{%s}sheetData' % NS['main'])
        self.temp_var['strs'] = [node[0].text for node in str_tree]
        range = self.xl_find_range(rows, self.temp_var['strs'], range)
        self.temp_var['info'] = self.xl_extract_info(rows, range)

        return self.xl_info_2_script(self.temp_var['info'])

    def xl_info_2_script(self, info):
        tag = self.current_tag
        script = []
        for key, content in info.items():
            if content[0][0] == 'txt':
                para = content[0][1]
                if para.lstrip().startswith('#'):
                    # means its a tag
                    tag = self.current_tag = part[0]
                    logger.info('[Change tag] #%s', tag)
                else:
                    for part in self._process_comment(para):
                        script.append((tag, part))
            elif content[0][0] == 'var':
                var_name = content[0][1]
                if len(content[1]) == 2:
                    steps = [content[1][1]]
                else:
                    steps = [self.xl_form2expr(0, 1, content), self.xl_form2expr(1, -1, content)]
                steps.append(content[1][-1])
                opt = content[-1][-1].replace('^', '**') if content[-1][0] == 'opt' else ''
                try:  # check if the var name is python legal
                    to_math(var_name + '=' + steps[-1])
                except SyntaxError:
                    eqn_xl = cal([f'"{var_name}"', steps, opt], working_dict=self.working_dict, typ=self.doc_type)
                else:
                    eqn_xl = cal([var_name, steps, opt], working_dict=self.working_dict, typ=self.doc_type)
                script.append((tag, (eqn_xl[1], eqn_xl[0])))

        return script

    def xl_find_range(self, rows, strs, given_range):
        '''convert a given range to a more useful one:
        (the letter, the starting index in tree, the row number of last)'''

        if given_range:
            if type(given_range) == str:
                # must be in the form "A, 1-10"
                col_let, n_range = [r.strip() for r in given_range.split(',')]
                r_start, r_end = [int(r) for r in n_range.split('-')]
                given_range = (col_let, r_start, r_end)
            for i_row, row in enumerate(rows):
                if int(row.attrib['r']) == given_range[1]:
                    xlrange = (given_range[0], i_row, given_range[2])
        else:
            found = False
            for i_row, row in enumerate(rows):
                for cell in row:
                    if 't' in cell.attrib and cell.attrib['t'] == 's' \
                            and strs[int(cell[0].text)]:
                        col_let = ''.join(
                            [c for c in cell.attrib['r'] if c.isalpha()])
                        xlrange = (col_let, i_row, int(rows[-1].attrib['r']))
                        found = True
                        break
                if found:
                    break

        return xlrange

    def xl_process_cell(self, cell, line, current_col, current_key):
        cont = ['txt', '']
        if 't' in cell.attrib and cell.attrib['t'] == 's':
            cont = ['txt', self.temp_var['strs'][int(cell[0].text.strip())]]
        elif cell.findall('{%s}f' % NS['main']):
            cont = ['expr', cell[0].text, cell[1].text]
        elif len(cell):
            cont = ['val', cell[0].text]

        if current_col == 0:
            line.append(cont)
            current_col += 1
        elif current_col == 1:
            if line[0][0] == 'txt' and cont[1].strip():
                line[0][0] = 'var'
                line[0][1] = f'{line[0][1]}'
                if cont[0] == 'txt':
                    cont[1] = f'"{cont[1]}"'
                line.append(cont)
                current_key = cell.attrib['r']
                current_col += 1
        else:
            if line[0][0] == 'var':
                if cont[0] == 'txt':
                    line.append(['opt', cont[1]])
                    current_col += 1
        
        return line, current_col, current_key

    def xl_extract_info(self, rows, range):

        # store calcs in dict with cell addreses as keys
        info = {}

        for i_row, row in enumerate(rows[range[1]:]):
            if int(row.attrib['r']) <= range[2]:
                line = []
                # default key unless changed (below)
                current_key = f'para{i_row}'
                current_col = -1
                for cell in row:
                    col_let = ''.join(
                        [c for c in cell.attrib['r'] if c.isalpha()])
                    if col_let == range[0]:
                        current_col = 0
                    if current_col in [0, 1, 2]:
                        line, current_col, current_key = \
                                self.xl_process_cell(cell, line, current_col, current_key)
                info[current_key] = line
        return info
    
    def xl_form2expr(self, ins1, ins2, content):
        try:
            correct = self.xl_cell_pat.sub(
                lambda x: self.temp_var['info'][x.group(0)][ins1][ins2],
                content[1][1]).replace('^', '**')
        except KeyError as err:
            raise ReferenceError(f'Cell reference \'{err.args[0]}\' outside of scanned range')
        correct = self.xl_func_pat.sub(lambda x: x.group(0).lower(), correct)
        return correct.replace('^', '**')

    def process_content(self, parts):
        tag = self.current_tag
        processed = []
        for part in self._split_module(parts):
            if part[1] == 'tag':
                tag = self.current_tag = part[0]
                logger.info('[Change tag] #%s', tag)
            elif part[1] in ['assign', 'expr']:
                processed.append(
                    (tag, self._process_assignment(part[0])))
            elif part[1] == 'comment':
                for part in self._process_comment(part[0]):
                    processed.append((tag, part))
            elif part[1] == 'stmt':
                # if it does not appear like an equation or a comment,
                # just execute it
                logger.info('[Executing] %s', part[0])
                exec(part[0], self.working_dict)
                if part[0].startswith('del '):
                    # also delete associated unit strings
                    variables = [v.strip()
                                 for v in part[0][len('del '):].split(',')]
                    for v in variables:
                        if v + UNIT_PF in self.working_dict:
                            del self.working_dict[v + UNIT_PF]
            elif part[1] == 'options':
                # set options for calculations that follow
                self.working_dict['__DOCAL_OPTIONS__'] = \
                        _process_options(part[0], self.default_options)
        return processed

    def _contin_type(self, accumul: str, line: str) -> bool:
        '''
        determine whether the line is part of a multi line part
        (for _split_module)
        '''
        if accumul and any([
            not _parens_balanced(accumul),
            accumul.rstrip()[-1] in ['\\', ':'],
            # or the line is indented and not a comment
            line and line[0].isspace() and not line.lstrip().startswith('#'),
            not line.strip()
        ]):
            return 'contin'
        elif (not _parens_balanced(line) or
                line.strip() and not line.lstrip().startswith(
                    '#') and line.rstrip()[-1] in ['\\', ':']):
            return 'begin'

    def _identify_part(self, part, comments):
        '''get the type of a string piece (assignment, expression, etc.)
        (for _split_module)
        '''

        part_ast = ast.parse(part).body
        if not part_ast:
            tag_match = PATTERN.match(part.strip())
            if tag_match and tag_match.group(0) == part.strip():
                return (part.strip()[1:], 'tag')
            elif part.lstrip().startswith('##'):
                if comments:
                    return (part.lstrip()[2:], 'real-comment')
                else:
                    return ('', 'comment')
            elif part.lstrip().startswith('#@'):
                return (part.lstrip()[2:], 'options')
            elif not part:
                return ('', 'comment')
            else:
                return (part.lstrip()[1:], 'comment')
        elif isinstance(part_ast[0], ast.Assign):
            return (part, 'assign')
        elif isinstance(part_ast[0], ast.Expr):
            return (part, 'expr')

        return (part, 'stmt')

    def _split_module(self, module: str, char='\n', comments=False):
        '''
        split the given script string with the character/str using the rules
        '''
        returned = []
        # incomplete lines accululation, stored as [<accumululated>, <contin type>]
        accumul = ['', None]
        for part in module.split('\n'):
            contin_type = self._contin_type(accumul[0], part)
            if contin_type:
                if contin_type == 'contin':
                    accumul[0] += '\n' + part
                else:
                    if accumul[0]:
                        returned.append(self._identify_part(accumul[0], comments))
                    accumul = [part, contin_type]
            else:
                if accumul[0]:
                    returned.append(self._identify_part(accumul[0], comments))
                    accumul[0] = ''
                returned.append(self._identify_part(part, comments))
        if accumul[0]:
            returned.append(self._identify_part(accumul[0], comments))

        return returned

    def _format_value(self, var, srnd=True):
        syntax = select_syntax(self.doc_type)
        if var in self.working_dict:
            unit_name = var + UNIT_PF
            unit = to_math(self.working_dict[unit_name],
                           div="/",
                           working_dict=self.working_dict,
                           typ=self.doc_type,
                           ital=False) \
                if unit_name in self.working_dict.keys() and self.working_dict[unit_name] \
                and self.working_dict[unit_name] != '_' else ''
            result = to_math(self.working_dict[var], typ=self.doc_type)
            return build_eqn([[result + syntax.txt.format(syntax.halfsp) + unit]],
                             disp=False, vert=False, srnd=srnd,
                             typ=self.doc_type)
        else:
            raise KeyError(f"'{var}' is an undefined variable.")

    def _process_comment(self, line):
        '''
        convert comments to latex paragraphs
        '''

        logger.info('[Processing] %s', line)
        if line.startswith('$'):
            patt = r'(?a)#(\w+)'
            # term beginning with a number unlikely to be used
            pholder = '111.111**PLACEHOLDER00'
            vals = []
            for v in re.finditer(patt, line):
                vals.append(self._format_value(v.group(1), False))
            line = re.sub(patt, pholder, line)
            if line.startswith('$$'):
                line = ('disp', eqn(line[2:], typ=self.doc_type))
            else:
                line = ('inline', eqn(line[1:], disp=False, typ=self.doc_type))
            for v in vals:
                line[1] = line[1].replace(to_math(pholder, typ=self.doc_type), v, 1)
            parts = [line]
        else:
            parts = []
            ref = False
            for part in re.split(r'(?a)(#\w+)', line.strip()):
                if ref:
                    parts.append(('inline', self._format_value(part[1:])))
                    ref = False
                else:
                    parts.append(('text', part))
                    ref = True
        return parts

    def _process_assignment(self, line):
        '''
        evaluate assignments and convert to latex form
        '''
        logger.info('[Processing] %s', line)
        # the cal function will execute it so no need for exec
        result = cal(line, self.working_dict, typ=self.doc_type)
        return (result[1], result[0])


class LogRecorder(logging.Handler):
    def __init__(self):
        super().__init__()
        self.log = []

    def emit(self, record):
        self.log.append(self.format(record))


class document:
    '''organize the process by taking tags from the filetype-specific classes,
    making a dictionary for them, and calling the write method of those classes
    giving them the dictionary'''

    file_handlers = {
        '.docx': wordFile,
        '.tex': latexFile,
    }

    def __init__(self, infile=None, outfile=None, to_clear=False, log_level=None, log_file=False):
        '''initialize'''

        self.to_clear = to_clear
        # clear previous handlers so the logs are only for the current run
        log_formatter = logging.Formatter(LOG_FORMAT)
        # log messages
        self.log = []
        self.log_recorder = LogRecorder()
        self.log_recorder.setFormatter(log_formatter)
        # to avoid repeatedly adding the same handler
        logger.handlers = []
        logger.addHandler(self.log_recorder)
        if log_level:
            logger.setLevel(getattr(logging, log_level.upper()))
        # the document
        if infile:
            infile = path.abspath(infile)
            basename, ext = path.splitext(infile)
            self.document_file = self.file_handlers[ext](infile, to_clear)
            # the calculations object that will convert given things to a list and store
            self.calc = calculations(self.document_file.tags, self.document_file.name, DICT)
            if log_file:
                file_logger = logging.FileHandler(basename + '.log', 'w')
                file_logger.setFormatter(logging.Formatter(LOG_FORMAT))
                logger.addHandler(file_logger)
        elif outfile:
            ext = path.splitext(outfile)[1]
            self.document_file = self.file_handlers[ext](
                None, self.to_clear)
            self.calc = calculations([], self.document_file.name, DICT)
        else:
            raise ValueError('Need to specify at least one document')
        if outfile:
            self.outfile = outfile
        else:
            self.outfile = None
        if log_level:
            logger.setLevel(getattr(logging, log_level.upper()))
        # the calculations corresponding to the tags
        self.contents = {}
        # temp storage for assignment statements where there are unmatched parens
        self.incomplete_assign = ''
        # temp storage for block statements like if and for
        self.incomplete_stmt = ''

    def send(self, content, typ='python'):
        '''add the content to the tag, which will be sent to the document.
        Where it will be inserted is decided by the most recent tag.'''

        if not self.to_clear:
            for tag, part in self.calc.process(content, typ):
                if tag not in self.contents.keys():
                    self.contents[tag] = []
                self.contents[tag].append(part)

    def write(self):
        '''replace all the tags with the contents of the python script.
        then if the destination file is given, write a typeset-ready latex
        file or word file.
        If the destination file is not given, perform an in-place
        substitution on the input file without destroying the chance of
        reverting changes. If this function is run on an in-place substituted
        file, it will revert the file to its original state (with tags).'''

        self.document_file.write(self.outfile, self.contents)
        logger.info('SUCCESS!!!')
        self.log = self.log_recorder.log
