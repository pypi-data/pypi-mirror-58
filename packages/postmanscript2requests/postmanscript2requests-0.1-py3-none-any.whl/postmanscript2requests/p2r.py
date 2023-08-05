"""
__author__ = Tser@xiaobaiit.com
__time__ = 2019/12/12 12:12
__file__ = p2r.py
"""
from argparse import ArgumentParser
from json import load
from time import ctime

class P2R:
    def __init__(self, postmanScript, fileName):
        self._p = load(open(postmanScript, 'r', encoding='utf-8'))
        self._head_code = "'''" \
                     "\n__author__ = Tser\n" \
                     f"__time__ = {ctime()}\n" \
                     f"__file__ = {fileName}.py\n" \
                     "'''\n\n"
        self._import_code = "from requests import "
        self._import_list = []
        self._code = '\n\n"""\n\t请将代码中所有{{变量}}单独替换成数据或者进行变量定义均可 \n' \
                     '\t断言的表达是中需要替换字段名为实际的返回值中的字段值接口\n' \
                     '\t例如：#assert 预期结果 == _apiName["字段名"] 改为 assert 100 == _apiName["code"]\n"""\n\n'
        self._file = fileName
        try:
            _ = self._p['item']
        except Exception as e:
            raise ("你的文件格式不正确，", e)

    def _checkScript(self):
        apis = self._p['item'][0]['item']
        for index, api in enumerate(apis):
            _apiName = api['name']
            _apiMethod = api['request']['method']
            _apiHeader = {}
            for h in api['request']['header']:
                _apiHeader[h['key']] = h['value']
            _apiBody = api['request']['body']
            _apiParams = {}
            _apiPath = api['request']['url']['raw']
            _apiReturnName = api['request']['url']['path'][-1]
            if _apiMethod == 'GET':
                self._code += f"#{_apiName}#\n" \
                    f"_{_apiReturnName} = get(url='{_apiPath}', headers={_apiHeader}).json()\n" \
                    f"#assert 预期结果 == 实际结果\n#assert 预期结果 == _{_apiReturnName}['字段名']\n\n"
            elif _apiMethod == 'POST':
                self._code += f"#{_apiName}#\n" \
                    f"_{_apiReturnName} = post(url='{_apiPath}', json={_apiBody}, headers={_apiHeader}).json()\n" \
                    f"#assert 预期结果 == 实际结果\n#assert 预期结果 == _{_apiReturnName}['字段名']\n\n"
            self._import_list.append(_apiMethod.lower())
        with open(self._file, 'w', encoding='utf-8') as f:
            f.write(self._head_code + self._import_code + ', '.join(list(set(self._import_list))) + self._code)
        f.close()

para = ArgumentParser(description="欢迎使用小白科技之PostMan Script转Python Code V0.1【目前版本仅支持GET与POST】")
para.add_argument('-f', '--file', help='PostMan脚本名, *.json')#, default='1.json', action='store_true')
para.add_argument('-p', '--pyScript',
                  help='Python脚本名,默认为：api_test_script.py',
                  default='api_test_script.py',
                  action='store_true')
args = para.parse_args()
P2R(args.file, args.pyScript)._checkScript()