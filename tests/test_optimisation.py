"""Garanties de factorisation et d’export autonome, sans publication ni build."""
from pathlib import Path
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from verifier_optimisation import verify


def run(tool,*args):
    return subprocess.run([sys.executable,str(tool),*(str(a) for a in args)],capture_output=True,text=True,encoding='utf-8',timeout=30)


class OptimisationTests(unittest.TestCase):
    def test_shared_tools_and_courses_integrity(self):
        self.assertEqual(verify(ROOT)['points_entree_partages'],205)
    def test_all_local_entrypoints(self):
        shared=json.loads((ROOT/'outils/kristal-partage.json').read_text(encoding='utf-8'))
        for rel in shared['entrypoints']:
            with self.subTest(path=rel):
                result=run(ROOT/rel,'--help');self.assertEqual(result.returncode,0,result.stderr)
                self.assertIn('build-v9',result.stdout)
    def test_inspect_is_the_same_as_pinned_tool(self):
        root=ROOT/'kristals/qc-pri-fr-002'
        shared=json.loads((ROOT/'outils/kristal-partage.json').read_text(encoding='utf-8'))
        a=run(root/'tools/kristal.py','inspect',root,'--compact')
        b=run(ROOT/shared['source'],'inspect',root,'--compact')
        self.assertEqual(a.returncode,0,a.stderr);self.assertEqual(b.returncode,0,b.stderr)
        self.assertEqual(json.loads(a.stdout),json.loads(b.stdout))
    def test_pack_stays_standalone_and_deterministic(self):
        root=ROOT/'kristals/qc-pri-fr-002';shared=json.loads((ROOT/'outils/kristal-partage.json').read_text(encoding='utf-8'))
        with tempfile.TemporaryDirectory() as td:
            folder=Path(td);archive=folder/'portable.zip';second=folder/'portable-again.zip'
            for target in (archive,second):
                p=run(root/'tools/kristal.py','pack',root,'--output',target);self.assertEqual(p.returncode,0,p.stderr)
            self.assertEqual(archive.read_bytes(),second.read_bytes())
            with zipfile.ZipFile(archive) as z:
                self.assertEqual(z.read(root.name+'/tools/kristal.py'),(ROOT/shared['source']).read_bytes())
                z.extractall(folder/'standalone')
            exported=folder/'standalone'/root.name
            p=run(exported/'tools/kristal.py','inspect',exported,'--compact')
            self.assertEqual(p.returncode,0,p.stderr);self.assertEqual(json.loads(p.stdout)['workspace']['slug'],root.name)
            self.assertEqual(len(list((exported/'tools/_templates').iterdir())),9)
    def test_init_creates_an_independent_tool(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'test-workspace';p=run(ROOT/'kristals/qc-pri-fr-002/tools/kristal.py','init',root,'--title','Test temporaire')
            self.assertEqual(p.returncode,0,p.stderr)
            self.assertNotIn(b'ekole.shared-kristal/1',(root/'tools/kristal.py').read_bytes())
            p=run(root/'tools/kristal.py','check',root);self.assertEqual(p.returncode,0,p.stderr)
    def test_different_version_remains_standalone(self):
        tool=ROOT/'kristals/modele-organisation-humaine/tools/kristal.py'
        result=run(tool,'--help');self.assertEqual(result.returncode,0,result.stderr)
        self.assertNotIn(b'ekole.shared-kristal/1',tool.read_bytes())

if __name__=='__main__':unittest.main()
