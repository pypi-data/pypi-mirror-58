#!/usr/bin/env python3
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

import copy
import os
import shutil
import subprocess
import sys
import unittest

from sos import execute_workflow
from sos.eval import interpolate
from sos.parser import SoS_Script
from sos.targets import file_target, path, paths, sos_targets, sos_step
from sos.utils import env
from sos.workflow_executor import Base_Executor


class TestTarget(unittest.TestCase):

    def setUp(self):
        env.reset()
        subprocess.call('sos remove -s', shell=True)
        # self.resetDir('~/.sos')
        self.temp_files = []

    def tearDown(self):
        for f in self.temp_files:
            if file_target(f).exists():
                file_target(f).unlink()

    def touch(self, files):
        '''create temporary files'''
        if isinstance(files, str):
            files = [files]
        #
        for f in files:
            with open(f, 'w') as tmp:
                tmp.write('test')
        #
        self.temp_files.extend(files)

    def testTargetLabel(self):
        '''Test labels of sos_targets'''
        a = sos_targets('a')
        self.assertEqual(a.labels, [''])
        b = sos_targets(['a', 'b'])
        self.assertEqual(b.labels, ['', ''])
        c = sos_targets(['a1', 'b1'], _source='here')
        self.assertEqual(c.labels, ['here', 'here'])
        c.extend(b)
        self.assertEqual(c.labels, ['here', 'here', '', ''])
        #
        self.assertEqual(c.select('').labels, ['', ''])
        self.assertEqual(c.select('here').labels, ['here', 'here'])
        self.assertEqual(c['here'], [file_target('a1'), file_target('b1')])
        self.assertTrue(isinstance(c['here'], sos_targets))
        #
        # function item
        self.assertTrue(isinstance(c.select(1), sos_targets))
        self.assertEqual(c.select(1).labels, ['here'])
        self.assertEqual(c.select(1), ['b1'])
        #
        # test slice of groups
        res = sos_targets(
            a=['a.txt', 'b.txt'], b=['c.txt', 'd.txt'], group_by=1)
        self.assertEqual(len(res.groups), 4)
        self.assertEqual(res.labels, ['a', 'a', 'b', 'b'])
        res_a = res['a']
        self.assertEqual(len(res_a), 2)
        self.assertEqual(res_a.labels, ['a', 'a'])
        self.assertEqual(len(res_a.groups), 4)
        self.assertEqual(len(res_a.groups[0]), 1)
        self.assertEqual(len(res_a.groups[1]), 1)
        self.assertEqual(len(res_a.groups[2]), 0)
        self.assertEqual(len(res_a.groups[3]), 0)

    def testRemoveTargets(self):
        '''Test sos_target.remove_targets()'''
        a = sos_targets(sos_step('1'), 'a.txt')._group(by=1)
        a.remove_targets(type=sos_step)
        self.assertEqual(len(a), 1)
        self.assertEqual(len(a.groups), 2)
        self.assertEqual(len(a._groups[0]._indexes), 0)
        self.assertEqual(len(a._groups[0]._labels), 0)
        self.assertEqual(a._groups[1]._indexes, [0])
        self.assertEqual(len(a._groups[1]._labels), 1)

    def testSoSTargetsSignature(self):
        '''Test save and validate signatures of sos_targets'''
        with open('a.txt', 'w') as a:
            a.write('text1')
        with open('b.txt', 'w') as b:
            b.write('text2')
        t = sos_targets('a.txt', 'b.txt')
        sig = t.target_signature()
        self.assertTrue(t.validate(sig))
        # variables does not affect signature
        t[0].set('a', 2)
        self.assertEqual(sig, t.target_signature())
        #
        t.set('cc', 'another string')
        self.assertTrue(t.validate(sig))

    def testTargetSetGet(self):
        '''Test set and get attributes from targets'''
        a = file_target('a')
        a.set(b=1)
        self.assertEqual(a.b, 1)
        self.assertEqual(a.get('b'), 1)
        self.assertRaises(Exception, a.set, 'touch', 1)

    def testTargetGroupBy(self):
        '''Test new option group_by to sos_targets'''
        res = sos_targets(
            'e.txt',
            'f.ext',
            a=['a.txt', 'b.txt'],
            b=['c.txt', 'd.txt'],
            group_by=1)
        self.assertEqual(len(res.groups), 6)
        self.assertEqual(res.labels, ['', '', 'a', 'a', 'b', 'b'])
        #
        res = sos_targets(res, group_by=2)
        self.assertEqual(len(res.groups), 3)

    def testTargetPairedWith(self):
        '''Test paired_with targets with vars'''
        res = sos_targets(
            'e.txt',
            'f.ext',
            a=['a.txt', 'b.txt'],
            b=['c.txt', 'd.txt'],
            group_by=1).paired_with('_name', ['e', 'f', 'a', 'b', 'c', 'd'])
        for i, n in enumerate(['e', 'f', 'a', 'b', 'c', 'd']):
            self.assertEqual(res[i]._name, n)
        #
        res = copy.deepcopy(res)
        for i, n in enumerate(['e', 'f', 'a', 'b', 'c', 'd']):
            self.assertEqual(res[i]._name, n)
        #
        # test assert for length difference
        self.assertRaises(Exception,
                          sos_targets('e.txt', 'f.ext').paired_with, 'name',
                          ['e', 'f', 'a', 'b', 'c', 'd'])

    def testTargetGroupWith(self):
        '''Test group_with targets with vars'''
        res = sos_targets(
            'e.txt',
            'f.ext',
            a=['a.txt', 'b.txt'],
            b=['c.txt', 'd.txt'],
            group_by=2).group_with('name', ['a1', 'a2', 'a3'])
        for i, n in enumerate(['a1', 'a2', 'a3']):
            self.assertEqual(res.groups[i].name, n)
        #
        res = copy.deepcopy(res)
        for i, n in enumerate(['a1', 'a2', 'a3']):
            self.assertEqual(res.groups[i].name, n)
        #
        # test assert for length difference
        self.assertRaises(Exception,
                          sos_targets('e.txt', 'f.ext', group_by=1).group_with,
                          'name', ['e', 'f', 'g'])

    def testGroupWithWithNoOutput(self):
        execute_workflow(r'''
[10]
input: for_each=dict(i=range(3))
output: group_with=dict(var=['A', 'B', 'C'])
print(i)

[20]
print(f'Input is {_input} {var}')
''')

    def testMergingOfSoSTargets(self):
        '''Test merging of multiple sos targets'''
        # merge 0 to 0
        res = sos_targets('a.txt', 'b.txt',
                          sos_targets('c.txt', 'd.txt', group_by=1))
        self.assertEqual(len(res), 4)
        self.assertEqual(len(res.groups), 2)
        self.assertEqual(res.groups[0], ['a.txt', 'b.txt', 'c.txt'])
        self.assertEqual(res.groups[1], ['a.txt', 'b.txt', 'd.txt'])
        # merge N to N
        N1 = sos_targets('c.txt', 'd.txt', group_by=1)
        N2 = sos_targets('a1.txt', 'a2.txt', 'a3.txt', 'a4.txt', group_by=2)
        res = sos_targets(N1, N2)
        self.assertEqual(len(res), 6)
        self.assertEqual(len(res.groups), 2)
        self.assertEqual(res.groups[0], ['c.txt', 'a1.txt', 'a2.txt'])
        self.assertEqual(res.groups[1], ['d.txt', 'a3.txt', 'a4.txt'])
        # test N to M
        N1 = sos_targets('c.txt', 'd.txt', group_by=1)
        N2 = sos_targets('a1.txt', 'a2.txt', 'a3.txt', 'a4.txt', group_by=1)
        self.assertRaises(Exception, sos_targets, N1, N2)
        # merge 1 to N
        N1 = sos_targets('c.txt', 'd.txt', group_by='all')
        N2 = sos_targets('a1.txt', 'a2.txt', 'a3.txt', 'a4.txt', group_by=2)
        res = sos_targets(N1, N2)
        self.assertEqual(len(res), 6)
        self.assertEqual(len(res.groups), 2)
        self.assertEqual(res.groups[0], ['c.txt', 'd.txt', 'a1.txt', 'a2.txt'])
        self.assertEqual(res.groups[1], ['c.txt', 'd.txt', 'a3.txt', 'a4.txt'])
        # merge N to 1
        res = sos_targets(N2, N1)
        self.assertEqual(len(res), 6)
        self.assertEqual(len(res.groups), 2)
        self.assertEqual(res.groups[0], ['a1.txt', 'a2.txt', 'c.txt', 'd.txt'])
        self.assertEqual(res.groups[1], ['a3.txt', 'a4.txt', 'c.txt', 'd.txt'])

    def testTargetFormat(self):
        '''Test string interpolation of targets'''
        for target, fmt, res in [
            ('a.txt', '', 'a.txt'),
            (sos_targets('a.txt'), '', 'a.txt'),
            (sos_targets(['a.txt']), '', 'a.txt'),
            (sos_targets([r'c:\path\a.txt']), 'p', '/c/path/a.txt'),
            (sos_targets([r'c:path\a.txt']), 'p', '/c/path/a.txt'),
            (sos_targets('/a/b/a.txt'), 'b', 'a.txt'),
            (sos_targets('a b.txt'), 'q', ("'a b.txt'", '"a b.txt"')),
            (sos_targets('a b.txt'), 'x', ".txt"),
        ]:
            if isinstance(res, str):
                self.assertEqual(
                    interpolate('{{target:{}}}'.format(fmt), globals(),
                                locals()), res,
                    "Interpolation of {}:{} should be {}".format(
                        target, fmt, res))
            else:
                self.assertTrue(
                    interpolate('{{target:{}}}'.format(fmt), globals(),
                                locals()) in res,
                    "Interpolation of {}:{} should be one of {}".format(
                        target, fmt, res))

    def testIterTargets(self):
        '''Test iterator interface of targets'''
        t = sos_targets('1', '2', ['3', '4'])
        self.assertEqual(len(t), 4)
        for idx, i in enumerate(t):
            self.assertEqual(str(i), str(idx + 1))

    def testExpandWildcard(self):
        '''test wildcard expansion of sos_targets'''
        a = sos_targets('*.py')
        self.assertGreater(len(a), 1)
        #
        a = paths('*.py')
        self.assertGreater(len(a), 1)

    def resetDir(self, dirname):
        if os.path.isdir(os.path.expanduser(dirname)):
            shutil.rmtree(os.path.expanduser(dirname))
        os.mkdir(os.path.expanduser(dirname))

    def testShared(self):
        '''Test option shared'''
        script = SoS_Script(r"""
parameter: res = 1

[0]
res = 2

[1]
res = 3
""")
        wf = script.workflow()
        Base_Executor(wf).run()
        self.assertEqual(env.sos_dict['res'], 1)
        #
        env.sos_dict.pop('res', None)
        script = SoS_Script(r"""
parameter: res = 1

[0: shared='res']
res = 2

[1]
res = 3
""")
        wf = script.workflow()
        Base_Executor(wf).run()
        self.assertEqual(env.sos_dict['res'], 2)
        #
        env.sos_dict.pop('res', None)
        script = SoS_Script(r"""
parameter: res = 1
parameter: a = 30

[0: shared='a']
res = 2

[1: shared='res']
res = 3
a = 5

""")
        wf = script.workflow()
        Base_Executor(wf).run()
        self.assertEqual(env.sos_dict['res'], 3)
        self.assertEqual(env.sos_dict['a'], 30)
        # test multiple vars
        env.sos_dict.pop('res', None)
        script = SoS_Script(r"""
parameter: res = 1
parameter: a = 30

[1: shared=('res', 'a')]
res = 3
a = 5

""")
        wf = script.workflow()
        Base_Executor(wf).run()
        self.assertEqual(env.sos_dict['res'], 3)
        self.assertEqual(env.sos_dict['a'], 5)
        #
        # test expression
        env.sos_dict.pop('res', None)
        script = SoS_Script(r"""
parameter: res = 1
parameter: a = 30

[1: shared={'res': 'res + 6', 'c': 'a'}]
res = 3
a = 5

""")
        wf = script.workflow()
        Base_Executor(wf).run()
        self.assertEqual(env.sos_dict['res'], 9)
        self.assertEqual(env.sos_dict['c'], 5)
        # test mixed vars and mapping
        env.sos_dict.pop('res', None)
        script = SoS_Script(r"""
parameter: res = 1
parameter: a = 30

[1: shared=['res', {'c': 'a'}]]
res = 3
a = 5

""")
        wf = script.workflow()
        Base_Executor(wf).run()
        self.assertEqual(env.sos_dict['res'], 3)
        self.assertEqual(env.sos_dict['c'], 5)
        # test the step_ version of variables
        script = SoS_Script(r"""
parameter: res = 1
parameter: a = 30

[1: shared=['res', {'c': 'sum(step_a)'}]]
input: for_each={'i': range(10)}
a = _index**2

""")
        wf = script.workflow()
        Base_Executor(wf).run()
        self.assertEqual(env.sos_dict['c'], sum(x**2 for x in range(10)))


#    def testSectionOptionWorkdir(self):
#        '''Test section option workdir'''
#        script = SoS_Script(r"""
#
# [1: workdir='tmp']
# run:
#    touch 'a.txt'
# """)
#        wf = script.workflow()
#        Base_Executor(wf).run()
#        self.assertTrue(os.path.isfile('tmp/a.txt'))
#        shutil.rmtree('tmp')

    def testDependsExecutable(self):
        '''Testing target executable.'''
        script = SoS_Script('''
[0]
depends: executable('python --version', '3.')
run:
    touch a.txt
''')
        wf = script.workflow()
        if file_target('a.txt').exists():
            file_target('a.txt').unlink()
        Base_Executor(wf).run()
        self.assertTrue(os.path.isfile('a.txt'))
        file_target('a.txt').unlink()

    @unittest.skipIf(sys.platform == 'win32',
                     'Windows executable cannot be created with chmod.')
    def testOutputExecutable(self):
        '''Testing target executable.'''
        # change $PATH so that lls can be found at the current
        # directory.
        os.environ['PATH'] += os.pathsep + '.'
        script = SoS_Script('''
[0]
output: executable('lls')
run:
    touch lls
    chmod +x lls
''')
        wf = script.workflow()
        if file_target('lls').exists():
            file_target('lls').unlink()
        env.config['sig_mode'] = 'force'
        Base_Executor(wf).run()
        # test validation
        env.config['sig_mode'] = 'default'
        Base_Executor(wf).run()
        if file_target('ls').exists():
            file_target('lls').unlink()

    def testDependsEnvVariable(self):
        '''Testing target env_variable.'''
        if file_target('a.txt').exists():
            file_target('a.txt').unlink()
        if sys.platform == 'win32':
            script = SoS_Script('''
[0]
depends: env_variable('AA')
output:  'a.txt'
run:
    echo %AA% > a.txt
''')
        else:
            script = SoS_Script('''
[0]
depends: env_variable('AA')
output:  'a.txt'
run:
    echo $AA > a.txt
''')
        wf = script.workflow()
        os.environ['AA'] = 'A1'
        Base_Executor(wf).run()
        with open('a.txt') as at:
            self.assertEqual(at.read().strip(), 'A1')
        # test validation
        Base_Executor(wf).run()
        # now if we change var, it should be rerun
        os.environ['AA'] = 'A2'
        Base_Executor(wf).run()
        # allow one second variation
        with open('a.txt') as at:
            self.assertEqual(at.read().strip(), 'A2')
        file_target('a.txt').unlink()

    @unittest.skipIf(sys.platform == 'win32',
                     'Windows executable cannot be created with chmod.')
    def testProvidesExecutable(self):
        '''Testing provides executable target.'''
        # change $PATH so that lls can be found at the current
        # directory.
        os.environ['PATH'] += os.pathsep + '.'
        if file_target('lls').exists():
            file_target('lls').unlink()
        script = SoS_Script('''
[lls: provides=executable('lkls')]
run:
    touch lkls
    chmod +x lkls

[c]
depends: executable('lkls')

''')
        wf = script.workflow('c')
        Base_Executor(wf).run()
        file_target('lkls').unlink()

    def testSharedVarInPairedWith(self):
        self.touch(['1.txt', '2.txt'])
        for file in ('1.out', '2.out', '1.out2', '2.out2'):
            if file_target(file).exists():
                file_target(file).unlink()
        script = SoS_Script('''
[work_1: shared = {'data': 'step_output'}]
input: "1.txt", "2.txt", group_by = 'single', pattern = '{name}.{ext}'
output: expand_pattern('{_name}.out')
run: expand=True
  touch {_output}

[work_2]
depends: sos_variable('data')
input: "1.txt", "2.txt", group_by = 'single', pattern = '{name}.{ext}', paired_with = dict(data1=data)
output: expand_pattern('{_name}.out2')
run: expand=True
  touch {data1[0]} {_output}
''')
        wf = script.workflow()
        Base_Executor(wf).run()
        for file in ('1.out', '2.out', '1.out2', '2.out2'):
            if file_target(file).exists():
                file_target(file).unlink()

    def testSharedVarInForEach(self):
        self.touch(['1.txt', '2.txt'])
        for file in ('1.out', '2.out', '1.out2', '2.out2'):
            if file_target(file).exists():
                file_target(file).unlink()
        script = SoS_Script('''
[work_1: shared = {'data': 'step_output'}]
input: "1.txt", "2.txt", group_by = 'single', pattern = '{name}.{ext}'
output: expand_pattern('{_name}.out')
run: expand=True
  touch {_output}

[work_2]
depends: sos_variable('data')
input: "1.txt", "2.txt", group_by = 'single', for_each = dict(data=data),  pattern = '{name}.{ext}'
output: expand_pattern('{data}_{_name}.out2')
run: expand=True
  touch {_output}

''')
        wf = script.workflow()
        Base_Executor(wf).run()

    def testRemovedDepends(self):
        '''Test a case where a dependent file has signature, but
        gets removed before the next run.'''
        script = SoS_Script('''
[tet: provides='a.txt']
run:
    echo "something" > a.txt

[20]
depends: 'a.txt'
output: 'b.txt'
run:
    cat a.txt > b.txt
''')
        wf = script.workflow()
        # this should be ok.
        Base_Executor(wf).run()
        # now let us remove a.txt (but the signature is still there)
        os.remove('a.txt')
        os.remove('b.txt')
        Base_Executor(wf).run()

    def testSoSStep(self):
        '''Test target sos_step'''
        for file in ['t1.txt', 't2.txt', '5.txt', '10.txt', '20.txt']:
            if file_target(file).exists():
                file_target(file).unlink()
        script = SoS_Script('''
[t1]
run:
    touch t1.txt

[t2: provides='t2.txt']
depends: sos_step('t1')
run:
    touch t2.txt

[5]
run:
    touch 5.txt

[10]
depends: sos_step('t2')
run:
    touch 10.txt

[20]
depends: sos_step('t1')
run:
    touch 20.txt
''')
        wf = script.workflow()
        env.config['sig_mode'] = 'force'
        # this should be ok.
        Base_Executor(wf).run()
        for file in ['t1.txt', 't2.txt', '5.txt', '10.txt', '20.txt']:
            self.assertTrue(
                file_target(file).target_exists(), file + ' should exist')
            if file_target(file).exists():
                file_target(file).unlink()

    def testZap(self):
        '''Test zap'''
        with open('testzap.txt', 'w') as sf:
            sf.write('some text')
        path('testzap.txt').zap()
        self.assertTrue(os.path.isfile('testzap.txt.zapped'))
        self.assertFalse(os.path.isfile('testzap.txt'))
        # re-zap is ok
        file_target('testzap.txt').zap()
        self.assertTrue(os.path.isfile('testzap.txt.zapped'))
        self.assertFalse(os.path.isfile('testzap.txt'))
        # non-existent file
        os.remove('testzap.txt.zapped')
        self.assertRaises(FileNotFoundError, path('testzap.txt').zap)
        #
        with open('testzap.txt', 'w') as sf:
            sf.write('some text')
        with open('testzap1.txt', 'w') as sf:
            sf.write('some text')
        paths('testzap.txt', 'testzap1.txt').zap()
        self.assertTrue(os.path.isfile('testzap.txt.zapped'))
        self.assertFalse(os.path.isfile('testzap.txt'))
        self.assertTrue(os.path.isfile('testzap1.txt.zapped'))
        self.assertFalse(os.path.isfile('testzap1.txt'))
        #
        os.remove('testzap.txt.zapped')
        os.remove('testzap1.txt.zapped')
        with open('testzap.txt', 'w') as sf:
            sf.write('some text')
        with open('testzap1.txt', 'w') as sf:
            sf.write('some text')
        sos_targets(['testzap.txt', 'testzap1.txt']).zap()
        self.assertTrue(os.path.isfile('testzap.txt.zapped'))
        self.assertFalse(os.path.isfile('testzap.txt'))
        self.assertTrue(os.path.isfile('testzap1.txt.zapped'))
        self.assertFalse(os.path.isfile('testzap1.txt'))

    def testZapRun(self):
        '''Test run with zapped input files'''
        with open('zap1.txt', 'w') as sf:
            sf.write('seomething')
        script = SoS_Script('''\
[1]
input: 'zap1.txt'
output: "zap2.txt"
run:
  echo asd>zap2.txt
_input.zap()
''')
        wf = script.workflow()
        env.config['sig_mode'] = 'force'
        Base_Executor(wf).run()
        self.assertTrue(os.path.isfile('zap1.txt.zapped'))
        self.assertFalse(os.path.isfile('zap1.txt'))
        self.assertTrue(os.path.isfile('zap2.txt'))
        # can run again
        env.config['sig_mode'] = 'default'
        Base_Executor(wf).run()
        # now if we remove target
        os.remove('zap2.txt')
        self.assertRaises(Exception, Base_Executor(wf).run)

    def testSystemResource(self):
        '''Test targtet system_resource'''
        script = SoS_Script('''\
[1: shared='a']
depends: system_resource(mem='1M',disk='1M')
a = 1
''')
        wf = script.workflow()
        Base_Executor(wf).run()
        self.assertEqual(env.sos_dict['a'], 1)
        #
        script = SoS_Script('''\
[1: shared='a']
depends: system_resource(mem='1T')
a = 1
''')
        wf = script.workflow()
        self.assertRaises(Exception, Base_Executor(wf).run)
        #
        script = SoS_Script('''\
[1: shared='a']
depends: system_resource(disk='10P')
a = 1
''')
        wf = script.workflow()
        self.assertRaises(Exception, Base_Executor(wf).run)

    def testOptionNameOfPath(self):
        '''Test the use of option name of path'''
        script = SoS_Script('''
import os
# windows might not have HOME
if 'HOME' in os.environ:
    assert path(name='home') == os.environ['HOME']
assert path(name='nonexisting', default='whatever') == 'whatever'
assert path.names() == ['home']
assert path.names('docker') == ['home']
''')
        wf = script.workflow()
        Base_Executor(
            wf,
            config={
                'config_file':
                    os.path.join(os.path.expanduser('~'), 'docker.yml')
            }).run()

if __name__ == '__main__':
    unittest.main()
