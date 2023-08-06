#！ /usr/bin/env python
# -*- coding=utf-8 -*-
"""
__author__      = 807447312@qq.com
__time__        = 2019-12-25 16:54:38
__file__        = p2r.py
__version__     = 0.2
"""
from argparse import ArgumentParser
from json import load
from time import localtime, strftime
from re import findall
from os import system

class P2R:
    def __init__(self, postmanScript):
        try:
            name = postmanScript.split('.')
            name[1] = 'py'
            fileName = '.'.join(name)
            self._p = load(open(postmanScript, 'r', encoding='utf-8'))
            self._head_code = "'''" \
                              "\n__author__ = Tser\n" \
                              f"__time__ = {strftime('%Y-%m-%d %H:%M:%S', localtime())}\n" \
                              f"__file__ = {fileName}\n" \
                              "'''\n\n"
            self._import_code = "from requests import request"
            self._import_list = []
            self._code = '\n\n"""\n\t请将代码中所有{{变量}}单独替换成数据或者进行变量定义均可\n"""\n\n'
            self._file = fileName
            self._apiReturnNameList = []
            try:
                _ = self._p['item']
            except Exception as e:
                raise ("你的文件格式不正确，", e)
        except:
            system("p2r -h")
            exit(0)

    def _header(self, _h, params):
        """解析header信息"""
        headers = {}
        for h in _h:
            try:
                params.append(findall('{{(.+?)}}', h['value'])[0])
            except:
                pass
            headers[h['key']] = h['value']
        return headers, params

    def _body(self, _b, params):
        """解析body信息"""
        _t = _b['mode']  # file raw formdata urlencoded
        if _t in ['formdata', 'urlencoded']:
            body = ""
            for d in _b[_t]:
                try:
                    params.append(findall('{{(.+?)}}', d['value'])[0])
                except:
                    pass
                body += d['key'] + "=" + d['value'] + "&"
            return body[:-1], params
        elif _t in ['raw', 'file']:
            try:
                params.append(findall('{{(.+?)}}', _b[_t])[0])
            except:
                pass
            return str(_b[_t]).replace('\n', '').replace('\t', ''), params
        else:
            return {}, params

    def _params(self, _p, params):
        """解析params信息"""
        pass

    def _url(self, _u, params):
        """解析url信息"""
        pass

    def _test(self, _t, _apiReturnName, params):
        """解析prerequest/test信息"""
        if _t.__len__() > 0:
            for e in _t:    # ['prerequest', 'test']
                if e['listen'] == 'prerequest':
                    return "", params
                elif e['listen'] == 'test':
                    result = ""
                    for line in e['script']['exec']:
                        try:
                            params.append(findall('{{(.+?)}}', line)[0])
                        except:
                            pass
                        xiangdeng_yuqi = findall('pm.expect\((.+?)\).to.eql\((.+?)\);', line)
                        if xiangdeng_yuqi.__len__() > 0:
                            result += f"#断言：\nassert {xiangdeng_yuqi[0][1]} == _{_apiReturnName}['{xiangdeng_yuqi[0][0].split('.')[-1]}']\n"
                        baohan_yuqi = findall('pm.expect\((.+?)\).to.include\((.+?)\);', line)
                        if baohan_yuqi.__len__() > 0:
                            result += f"#断言：\nassert {baohan_yuqi[0][1]} in _{_apiReturnName}['{baohan_yuqi[0][0].split('.')[-1]}']\n"
                    return result + "\n", params
                else:
                    return "#断言：\n", params
        else:
            return "#断言：\n#assert 预期结果 == 实际结果 或 assert 预期结果 in 实际结果\n\n", params

    def _checkScript(self):
        try:
            # swagger文档转为postman脚本格式，存在item
            apis = self._p['item'][0]['item']
        except:
            # 手动添加接口到postman脚本不存在第二层的item
            apis = self._p['item']
        for index, api in enumerate(apis):
            _apiName = api['name']
            _apiMethod = api['request']['method']
            _apiParams = []  # 暂时没用
            _apiHeader, p1 = self._header(api['request']['header'], _apiParams)
            _apiBody, p2 = self._body(api['request']['body'], p1)
            _apiPath = api['request']['url']['raw']
            _apiReturnName = api['request']['url']['path'][-1]
            new_apiReturnName = _apiReturnName
            _attr = 0
            while _apiReturnName in self._apiReturnNameList:
                _apiReturnName = new_apiReturnName + '_' + str(_attr)
                _attr += 1
            if _apiReturnName not in self._apiReturnNameList:
                self._apiReturnNameList.append(_apiReturnName)
            _apiTest, p3 = self._test(api['event'], _apiReturnName, p2)
            params = '#变量：\n'
            p3 = list(set(p3))
            for p in p3:
                params += f'{p} = "值"\n'
            self._code += \
                params + \
                f"#{_apiName}#\n_{_apiReturnName} = request('{_apiMethod}', url='{_apiPath}', data='{_apiBody}' ,headers={_apiHeader}).json()\n" + _apiTest
        with open(self._file, 'w', encoding='utf-8') as f:
            f.write(self._head_code +
                    self._import_code +
                    ', '.join(list(set(self._import_list))) +
                    self._code)
        f.close()

def main():
    para = ArgumentParser(description="欢迎使用小白科技之PostManScript转PythonCode")
    para.add_argument('-f', '--file', help='PostMan脚本名, *.json')
    args = para.parse_args()
    P2R(args.file)._checkScript()

if __name__ == '__main__':
    main()